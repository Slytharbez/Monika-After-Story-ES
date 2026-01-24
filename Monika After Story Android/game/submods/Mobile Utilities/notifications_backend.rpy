# NOTIFICATIONS BACKEND - CLEAN STUB
# This file previously contained AlarmManager/BroadcastReceiver logic.
# It has been cleaned for a future migration to WorkManager.
# Functions are kept as empty stubs to prevent NameErrors in other scripts.

init -5 python:
    # Try to import Pyjnius for Android interaction
    try:
        from jnius import autoclass, cast
        mas_android_backend_available = True
    except ImportError:
        mas_android_backend_available = False

init python:
    # --- STUBS & FAILSAFES (Priority 0) ---
    # We define these HERE to guarantee they exist before any label is called.
    # This prevents NameError even if the init 5 block fails or conditions aren't met.

    def mas_android_schedule_notif(title, message, delay_seconds=0):
        # Stub for logic
        pass

    def mas_android_cancel_all_notifs():
        # Stub for logic
        pass

    def mas_android_send_test_notif(title, message):
        # Default Fallback Stub
        # If the real function loads, this will be overwritten.
        # If not, this prevents the crash and logs the issue.
        print("[MAS_ANDROID] WARNING: Backend not loaded/available. Test call stubbed.")
        if renpy.substitute(title) and renpy.substitute(message):
            pass # Prevent unused var warning/error if strict
        # renpy.log("[MAS_ANDROID] WARNING: Backend not loaded/available. Test call stubbed.")

    # Expose to store immediately
    store.mas_android_schedule_notif = mas_android_schedule_notif
    store.mas_android_cancel_all_notifs = mas_android_cancel_all_notifs
    store.mas_android_send_test_notif = mas_android_send_test_notif
    
    # Ensure persistent default is set
    if persistent.mas_android_notif_enabled is None:
        persistent.mas_android_notif_enabled = True

init 5 python:
    # --- REAL IMPLEMENTATION (Priority 5) ---
    # WorkManager Implementation for Android Notifications
    
    if mas_android_backend_available and renpy.android:
        
        # 1. SCHEDULED NOTIFICATIONS (WorkManager) - For Closing App
        def mas_android_schedule_notif(title, message, delay_seconds, actions=None):
            """
            Schedules a notification using Android WorkManager.
            Args:
                actions (list/tuple, optional): List of labels for buttons. 
                                                Index 0 = Action 1 (Launch), Index 1 = Action 2 (Dismiss).
            """
            try:
                # --- FIX: Content & Title Parsing ---
                if isinstance(message, dict):
                    message = message.get("msg", "Te estaré esperando...")
                
                title = renpy.substitute(title)
                message = renpy.substitute(message)
                
                # Imports
                try: 
                    PythonActivity = autoclass('org.renpy.android.PythonSDLActivity')
                except: 
                    PythonActivity = autoclass('org.renpy.android.PythonActivity')
                    
                WorkManager = autoclass('androidx.work.WorkManager')
                OneTimeWorkRequest = autoclass('androidx.work.OneTimeWorkRequest$Builder')
                Data = autoclass('androidx.work.Data$Builder')
                TimeUnit = autoclass('java.util.concurrent.TimeUnit')
                ExistingWorkPolicy = autoclass('androidx.work.ExistingWorkPolicy')
                Collections = autoclass('java.util.Collections')
                
                # Worker Class
                WorkerClass = autoclass('com.monikaafterstory.tec.es.NotificationWorker')
                
                context = PythonActivity.mActivity
                
                # Prepare Data
                data_builder = Data()
                data_builder.putString("title", title)
                data_builder.putString("message", message)
                
                # Add Actions if present
                if actions and len(actions) >= 1:
                    data_builder.putString("action1_label", actions[0])
                if actions and len(actions) >= 2:
                    data_builder.putString("action2_label", actions[1])
                    
                input_data = data_builder.build()
                
                # Build Work Request
                delay_long = long(delay_seconds)
                
                work_request_builder = OneTimeWorkRequest(WorkerClass)
                work_request_builder.setInitialDelay(delay_long, TimeUnit.SECONDS)
                work_request_builder.setInputData(input_data)
                work_request_builder.addTag("mas_notification")
                
                work_request = work_request_builder.build()
                
                # Enqueue Unique Work
                work_list = Collections.singletonList(work_request)
                
                wm = WorkManager.getInstance(context)
                wm.enqueueUniqueWork("mas_notification_job", ExistingWorkPolicy.REPLACE, work_list)
                
                print("[MAS_ANDROID] Notification Scheduled: {}s - {}".format(delay_seconds, title))
                return True
                
            except Exception as e:
                print("[MAS_ANDROID] Schedule Notif Error: " + str(e))
                return False

        def mas_android_cancel_all_notifs():
            """
            Cancels all scheduled MAS notifications.
            """
            try:
                try: 
                    PythonActivity = autoclass('org.renpy.android.PythonSDLActivity')
                except: 
                    PythonActivity = autoclass('org.renpy.android.PythonActivity')
                    
                WorkManager = autoclass('androidx.work.WorkManager')
                
                context = PythonActivity.mActivity
                wm = WorkManager.getInstance(context)
                wm.cancelUniqueWork("mas_notification_job")
                
                print("[MAS_ANDROID] All Notifications Cancelled")
                
            except Exception as e:
                print("[MAS_ANDROID] Cancel Error: " + str(e))

        # 2. IMMEDIATE NOTIFICATIONS (Direct JNI) - For Introduction/Debug
        def mas_android_display_notif(title, message):
            """
            Sends an immediate notification using Android Native API (Pyjnius).
            Used for the introduction event sample.
            """
            try:
                # Text Substitution
                title = renpy.substitute(title)
                message = renpy.substitute(message)
                
                # Imports
                Context = autoclass('android.content.Context')
                Notification = autoclass('android.app.Notification')
                NotificationManager = autoclass('android.app.NotificationManager')
                NotificationChannel = autoclass('android.app.NotificationChannel')
                NotificationBuilder = autoclass('android.app.Notification$Builder')
                BigTextStyle = autoclass('android.app.Notification$BigTextStyle') 
                String = autoclass('java.lang.String')
                Build = autoclass('android.os.Build$VERSION')
                
                try: 
                    PythonActivity = autoclass('org.renpy.android.PythonSDLActivity')
                except: 
                    PythonActivity = autoclass('org.renpy.android.PythonActivity')

                context = PythonActivity.mActivity
                nm = cast(NotificationManager, context.getSystemService(Context.NOTIFICATION_SERVICE))
                
                # FIXED: Changed Channel ID to V2 to ensure sound settings are refreshed
                channel_id = "mas_test_channel_v2"
                
                # Resource Lookup (Dynamic)
                res = context.getResources()
                pkg = context.getPackageName()
                # Corrected Resource Names
                smallIconId = res.getIdentifier("ic_stat_smoll", "drawable", pkg)
                soundId = res.getIdentifier("notif", "raw", pkg)
                
                if smallIconId == 0:
                    smallIconId = 17301628 # Fallback: visible system icon
                    
                # Create Channel (Android 8.0+)
                if Build.SDK_INT >= 26:
                    name = String("MAS Test Channel")
                    description = String("Canal para pruebas de notificaciones")
                    importance = NotificationManager.IMPORTANCE_HIGH
                    
                    channel = NotificationChannel(String(channel_id), name, importance)
                    channel.setDescription(description)
                    channel.enableVibration(True)
                    
                    # Sound Setup for Channel
                    if soundId != 0:
                        Uri = autoclass('android.net.Uri')
                        AudioAttributes = autoclass('android.media.AudioAttributes$Builder')
                        
                        soundUri = Uri.parse("android.resource://" + pkg + "/" + str(soundId))
                        audioAttr = AudioAttributes().setUsage(5).setContentType(4).build() # USAGE_NOTIFICATION, CONTENT_TYPE_SONIFICATION
                        channel.setSound(soundUri, audioAttr)
                        
                    nm.createNotificationChannel(channel)
                    
                # Build Notification
                if Build.SDK_INT >= 26:
                    builder = NotificationBuilder(context, String(channel_id))
                else:
                    builder = NotificationBuilder(context)
                
                j_title = String(title)
                j_message = String(message)
                
                builder.setContentTitle(j_title)
                builder.setContentText(j_message)
                builder.setSmallIcon(smallIconId)
                
                style = BigTextStyle()
                style.bigText(j_message)
                style.setBigContentTitle(j_title)
                builder.setStyle(style)
                
                builder.setAutoCancel(True)
                
                if Build.SDK_INT >= 26:
                    builder.setTimeoutAfter(9000)
                
                # Defaults for pre-Oreo
                builder.setDefaults(Notification.DEFAULT_VIBRATE) 
                
                nm.notify(888, builder.build())
                
                print("[MAS_ANDROID] Display Notification Sent")
                return True
                
            except Exception as e:
                print("[MAS_ANDROID] Display Notif Error: " + str(e))
                return False

        # Overwrite Store Functions
        store.mas_android_schedule_notif = mas_android_schedule_notif
        store.mas_android_cancel_all_notifs = mas_android_cancel_all_notifs
        # New function name
        store.mas_android_display_notif = mas_android_display_notif

    else:
        # Fallback for PC Simulation
        def mas_android_schedule_notif(title, message, delay_seconds):
            print("[MAS_ANDROID] (Simulated) Scheduled in {}s: [{}] {}".format(delay_seconds, title, message))
        
        def mas_android_cancel_all_notifs():
            print("[MAS_ANDROID] (Simulated) All cancelled")
            
        def mas_android_display_notif(title, message):
            print("[MAS_ANDROID] (Simulated) DISPLAY: [{}] {}".format(title, message))
             
        store.mas_android_schedule_notif = mas_android_schedule_notif
        store.mas_android_cancel_all_notifs = mas_android_cancel_all_notifs
        store.mas_android_display_notif = mas_android_display_notif
