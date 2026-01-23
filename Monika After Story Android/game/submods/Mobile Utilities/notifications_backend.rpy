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
    # If environment is valid, we overwrite the stubs with the real deal.
    
    if mas_android_backend_available and renpy.android:
        
        def mas_android_send_test_notif(title, message):
            """
            Sends an immediate notification using Android Native API (Pyjnius).
            """
            try:
                # 0. Text Substitution (CRITICAL FIX)
                # Replaces [player] with the user's name
                title = renpy.substitute(title)
                message = renpy.substitute(message)

                # 1. Imports
                Context = autoclass('android.content.Context')
                NotificationManager = autoclass('android.app.NotificationManager')
                NotificationChannel = autoclass('android.app.NotificationChannel')
                NotificationBuilder = autoclass('android.app.Notification$Builder')
                # BigTextStyle for 2-line formatting
                BigTextStyle = autoclass('android.app.Notification$BigTextStyle') 
                
                String = autoclass('java.lang.String')
                Build = autoclass('android.os.Build$VERSION')
                
                try:
                    PythonActivity = autoclass('org.renpy.android.PythonSDLActivity')
                except:
                    PythonActivity = autoclass('org.renpy.android.PythonActivity')

                context = PythonActivity.mActivity
                nm = cast(NotificationManager, context.getSystemService(Context.NOTIFICATION_SERVICE))
                
                channel_id = "mas_test_channel"
                
                # 2. Create Channel (Android 8.0+ / API 26+)
                if Build.SDK_INT >= 26:
                    name = String("MAS Debug Channel")
                    description = String("Canal para pruebas de notificaciones en vivo")
                    importance = NotificationManager.IMPORTANCE_HIGH
                    
                    channel = NotificationChannel(String(channel_id), name, importance)
                    channel.setDescription(description)
                    # Enable Vibration to ensure heads-up
                    channel.enableVibration(True)
                    nm.createNotificationChannel(channel)
                    
                # 3. Build Notification
                if Build.SDK_INT >= 26:
                    builder = NotificationBuilder(context, String(channel_id))
                else:
                    builder = NotificationBuilder(context)
                
                # Apply Text & Style
                j_title = String(title)
                j_message = String(message)
                
                builder.setContentTitle(j_title)
                builder.setContentText(j_message)
                
                # STYLE: BigTextStyle
                # Forces expansion and usually ensures title/text separation
                style = BigTextStyle()
                style.bigText(j_message)
                style.setBigContentTitle(j_title)
                builder.setStyle(style)
                
                # Small Icon - System Chat Icon as safe fallback
                builder.setSmallIcon(17301628) 
                
                builder.setAutoCancel(True)
                
                # TIMEOUT: 9 Seconds (Requested)
                # Only works on API 26+ (Android 8.0)
                if Build.SDK_INT >= 26:
                    builder.setTimeoutAfter(9000)
                
                # Defaults for Sound/Vibration
                # Notification.DEFAULT_ALL = -1
                builder.setDefaults(-1) 
                
                # 4. Show it (ID 777)
                nm.notify(777, builder.build())
                
                print("[MAS_ANDROID] Debug Notification Sent Successfully")
                # renpy.log("[MAS_ANDROID] Debug Notification Sent Successfully")
                return True
                
            except Exception as e:
                print("[MAS_ANDROID] Debug Notif Error: " + str(e))
                # renpy.log("[MAS_ANDROID] Debug Notif Error: " + str(e))
                return False

        # Overwrite Store Function
        store.mas_android_send_test_notif = mas_android_send_test_notif

    else:
        # Fallback for PC Simulation
        def mas_android_send_test_notif(title, message):
            title = renpy.substitute(title)
            message = renpy.substitute(message)
            print("[MAS_ANDROID] (Simulated) Notification: [{}] {}".format(title, message))
            # renpy.log("[MAS_ANDROID] (Simulated) Notification: [{}] {}".format(title, message))
        
        store.mas_android_send_test_notif = mas_android_send_test_notif
