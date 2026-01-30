"""
Android Notification Backend System
   
This script handles the scheduling, cancellation, and display of Android notifications.
It accommodates both the Android runtime environment (via Pyjnius) and PC simulation.

Architecture:
- On Android: Utilizes Android's `WorkManager` API for reliable background scheduling.
- On PC: Provides simulated console output for debugging purposes.
"""

init -5 python:
    """
    Dependency Check: Pyjnius
    Attempts to import the `jnius` module to determine if the environment supports
    direct Android Java interactions.
    """
    try:
        from jnius import autoclass, cast
        mas_android_backend_available = True
    except ImportError:
        mas_android_backend_available = False

init python:
    """
    Function Stubs (Safe Initialization)
    
    These stubs are defined early to ensure that the global store variables exist 
    regardless of the execution environment or import success. This prevents `NameError`
    crashes during early game initialization sequences.
    """

    def mas_android_schedule_notif(title, message, delay_seconds=0, actions=None):
        """
        Stub for notification scheduling.
        This function is intended to be overwritten by the active implementation later.
        """
        pass

    def mas_android_cancel_all_notifs():
        """
        Stub for notification cancellation.
        This function is intended to be overwritten by the active implementation later.
        """
        pass

    def mas_android_send_test_notif(title, message):
        """
        Stub for immediate test notifications.
        Acts as a safe fallback; if the backend isn't loaded, it simply logs a warning
        instead of crashing the game.
        """
        print("[MAS_ANDROID] WARNING: Backend not loaded/available. Test call stubbed.")
        if renpy.substitute(title) and renpy.substitute(message):
            pass 
        

    """
    Exposition in Store
    Mapping stubs to the global store to make them accessible from anywhere in Ren'Py.
    """
    store.mas_android_schedule_notif = mas_android_schedule_notif
    store.mas_android_cancel_all_notifs = mas_android_cancel_all_notifs
    store.mas_android_send_test_notif = mas_android_send_test_notif
    
    """
    Default Configuration
    Ensures that the master switch for notifications is initialized.
    """
    if persistent.mas_android_notif_enabled is None:
        persistent.mas_android_notif_enabled = True

init 5 python:
    """
    Active Implementation (Priority 5)
    
    This block initializes the concrete implementations of the notification functions.
    It branches based on whether the Android backend (`jnius`) is available.
    """
    
    if mas_android_backend_available and renpy.android:
        
        """
        1. SCHEDULED NOTIFICATIONS (WorkManager)
        
        Uses `androidx.work.WorkManager` to schedule tasks that run even if the app
        is closed or the device reboots. This is essential for long-term delays
        (e.g., "I'll miss you" messages).
        """
        def mas_android_schedule_notif(title, message, delay_seconds, actions=None):
            """
            Schedules a future notification using Android's WorkManager API.
            
            IN:
                title (str) - The title of the notification.
                message (str/dict) - The body text or a specific message dictionary.
                delay_seconds (int) - Time in seconds to wait before showing the notification.
                actions (list) - Optional list of button labels [Action1, Action2].
            
            RETURNS:
                bool - True if scheduling was successful, False otherwise.
            """
            try:
                """
                Data Preparation
                Extracts the message text if a dictionary was provided and applies
                Ren'Py string substitution (for player naming, etc.).
                """
                if isinstance(message, dict):
                    message = message.get("msg", "Te estaré esperando...")
                
                title = renpy.substitute(title)
                message = renpy.substitute(message)
                
                """
                Java Class Imports (Pyjnius)
                Dynamically loads the necessary Android and Java classes.
                Includes a fallback for `PythonSDLActivity` vs `PythonActivity`.
                """
                try: 
                    PythonActivity = autoclass('org.renpy.android.PythonSDLActivity')
                except: 
                    PythonActivity = autoclass('org.renpy.android.PythonActivity')
                    
                WorkManager = autoclass('androidx.work.WorkManager')
                OneTimeWorkRequest = autoclass('androidx.work.OneTimeWorkRequest$Builder')
                Data = autoclass('androidx.work.Data$Builder')
                TimeUnit = autoclass('java.util.concurrent.TimeUnit')
                ExistingWorkPolicy = autoclass('androidx.work.ExistingWorkPolicy')
                OutOfQuotaPolicy = autoclass('androidx.work.OutOfQuotaPolicy')
                Collections = autoclass('java.util.Collections')
                
                """
                Worker Class Reference
                The custom Java Worker responsible for processing the notification request.
                """
                WorkerClass = autoclass('com.monikaafterstory.tec.es.NotificationWorker')
                
                context = PythonActivity.mActivity
                
                """
                Input Data Construction
                Packs all notification parameters (text, actions, settings) into a Data object
                that will be passed to the Worker.
                """
                data_builder = Data()
                data_builder.putString("title", title)
                data_builder.putString("message", message)
                
                if actions and len(actions) >= 1:
                    data_builder.putString("action1_label", actions[0])
                if actions and len(actions) >= 2:
                    data_builder.putString("action2_label", actions[1])

                """
                Preference Handling
                Passes the current sound/vibration user settings to the worker.
                Defaults to True (Sound/Vibration ON) if not explicitly set.
                """
                snd = True if persistent.mas_android_notif_sound is None else persistent.mas_android_notif_sound
                vib = True if persistent.mas_android_notif_vibration is None else persistent.mas_android_notif_vibration
                
                data_builder.putBoolean("sound_enabled", snd)
                data_builder.putBoolean("vibration_enabled", vib)
                    
                input_data = data_builder.build()
                
                """
                Work Request Construction
                Creates a OneTimeWorkRequest with the calculated delay.
                """
                delay_long = long(delay_seconds)
                
                work_request_builder = OneTimeWorkRequest(WorkerClass)
                work_request_builder.setInitialDelay(delay_long, TimeUnit.SECONDS)
                work_request_builder.setInputData(input_data)
                
                """
                Tagging
                Adds a tag to identifying this work request types.
                """
                work_request_builder.addTag("mas_notification")
                
                work_request = work_request_builder.build()
                
                """
                Work Enqueuing
                Queues the work with a UNIQUE policy ("mas_notification_job").
                REPLACE policy ensures that any previously scheduled notification is overwritten
                by this new one.
                """
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
            Uses the unique work name "mas_notification_job" to identify and stop pending work.
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

        """
        2. IMMEDIATE NOTIFICATIONS (Direct JNI)
        
        Uses a custom helper class to show a notification INSTANTLY.
        Typically used for debugging or immediate in-game events (like the introduction).
        """
        def mas_android_display_notif(title, message):
            """
            Sends an immediate notification via JNI for testing/intro.
            
            IN:
                title (str) - Notification title.
                message (str) - Notification body.
            
            RETURNS:
                bool - True if successful.
            """
            try:
                title = renpy.substitute(title)
                message = renpy.substitute(message)
                
                try: 
                    PythonActivity = autoclass('org.renpy.android.PythonSDLActivity')
                except: 
                    PythonActivity = autoclass('org.renpy.android.PythonActivity')
                
                NotificationHelper = autoclass('com.monikaafterstory.tec.es.NotificationHelper')
                
                context = PythonActivity.mActivity
                
                snd = True if persistent.mas_android_notif_sound is None else persistent.mas_android_notif_sound
                vib = True if persistent.mas_android_notif_vibration is None else persistent.mas_android_notif_vibration
                
                """
                Helper Call
                Invokes the static `showNotification` method.
                Parameters: context, id, title, text, action1, action2, style_type, sound, vibration, timeout
                """
                NotificationHelper.showNotification(
                    context,
                    888, # ID: Fixed ID for this specific test case
                    title,
                    message,
                    None, # No Action 1
                    None, # No Action 2
                    2,    # TYPE_INGAME_EVENT (2) -> Native Simple Style
                    snd,  # Sound Bool
                    vib,  # Vibration Bool
                    9000  # TIMEOUT: Auto-dismiss after 9 seconds
                )
                
                print("[MAS_ANDROID] Display Notification Sent via Helper")
                return True
                
            except Exception as e:
                print("[MAS_ANDROID] Display Notif Error: " + str(e))
                return False

        """
        Store Override
        Point the store variables to the real implementations.
        """
        store.mas_android_schedule_notif = mas_android_schedule_notif
        store.mas_android_cancel_all_notifs = mas_android_cancel_all_notifs
        store.mas_android_display_notif = mas_android_display_notif

    else:
        """
        Fallback Implementation (PC / No-Backend)
        
        Mock functions that print to the console instead of calling Java APIs.
        This allows development and testing of the logic on PC without crashing.
        """
        def mas_android_schedule_notif(title, message, delay_seconds, actions=None):
            print("[MAS_ANDROID] (Simulated) Scheduled in {}s: [{}] {}".format(delay_seconds, title, message))
            if actions:
                print("[MAS_ANDROID] (Simulated) With Actions: " + str(actions))
        
        def mas_android_cancel_all_notifs():
            print("[MAS_ANDROID] (Simulated) All cancelled")
            
        def mas_android_display_notif(title, message):
            print("[MAS_ANDROID] (Simulated) DISPLAY: [{}] {}".format(title, message))
             
        store.mas_android_schedule_notif = mas_android_schedule_notif
        store.mas_android_cancel_all_notifs = mas_android_cancel_all_notifs
        store.mas_android_display_notif = mas_android_display_notif
