init -5 python:
    # Try to import Pyjnius for Android interaction
    try:
        from jnius import autoclass, cast
        mas_android_backend_available = True
    except ImportError:
        mas_android_backend_available = False

init 5 python:
    if mas_android_backend_available and renpy.android:
        
        # --- ANDROID CLASSES ---
        Context = autoclass('android.content.Context')
        Intent = autoclass('android.content.Intent')
        PendingIntent = autoclass('android.app.PendingIntent')
        AlarmManager = autoclass('android.app.AlarmManager')
        try:
            PythonActivity = autoclass('org.renpy.android.PythonSDLActivity')
        except:
            PythonActivity = autoclass('org.renpy.android.PythonActivity')
        System = autoclass('java.lang.System')
        
        # Constants
        ALARM_SERVICE = Context.ALARM_SERVICE
        MAS_NOTIF_ID = 1001 
        
        # ACTION DEFINED IN MANIFEST
        NOTIF_ACTION = "com.monika.android.NOTIFICACION"
        
        def mas_android_schedule_notif(title, message, delay_seconds):
            """
            Schedules an Android notification using AlarmManager broadcasting to AlarmReceiver.
            """
            renpy.log("[MAS_ANDROID] DEBUG: mas_android_schedule_notif called with: '{}' ({}s)".format(message, delay_seconds))
            
            if not persistent.mas_android_notif_enabled:
                renpy.log("[MAS_ANDROID] DEBUG: Notifications DISABLED via persistent. Returning.")
                return

            try:
                context = PythonActivity.mActivity
                
                # 1. Create the Intent for our Receiver
                intent = Intent(NOTIF_ACTION)
                # Helper: Explicitly set package to ensure it goes to OUR app (security/robustness)
                intent.setPackage(context.getPackageName())
                
                # 2. Add Data
                intent.putExtra("title", title)
                intent.putExtra("message", message)
                intent.putExtra("id", MAS_NOTIF_ID)
                
                # 3. Create PendingIntent (Broadcast)
                # FLAG_UPDATE_CURRENT = 134217728 (0x08000000)
                # FLAG_IMMUTABLE = 67108864 (0x04000000)
                # We can pass the raw integer to be safe: 
                # 0x08000000 | 0x04000000 = 201326592
                flags = 201326592 
                
                pending_intent = PendingIntent.getBroadcast(
                    context, 
                    MAS_NOTIF_ID, 
                    intent, 
                    flags
                )
                
                # 4. Schedule Alarm
                alarm_manager = cast(AlarmManager, context.getSystemService(Context.ALARM_SERVICE))
                
                # Calculate Trigger Time
                trigger_time = System.currentTimeMillis() + (delay_seconds * 1000)
                
                # Use setExactAndAllowWhileIdle if available (API 23+) for reliability
                try:
                    alarm_manager.setExactAndAllowWhileIdle(0, trigger_time, pending_intent)
                except Exception as ex_alarm:
                    renpy.log("[MAS_ANDROID] Exact alarm failed (likely permission): " + str(ex_alarm))
                    # Fallback to stronger inexact alarm (Doze resistant)
                    # setAndAllowWhileIdle does NOT require SCHEDULE_EXACT_ALARM permissions
                    alarm_manager.setAndAllowWhileIdle(0, trigger_time, pending_intent)
                    renpy.log("[MAS_ANDROID] Fallback to setAndAllowWhileIdle() alarm used.")

                renpy.log("[MAS_ANDROID] Notification Scheduled via AlarmManager: {} in {}s".format(message, delay_seconds))
                print("[MAS_ANDROID] Scheduled Native Notif: {} in {}s".format(message, delay_seconds))

            except Exception as e:
                renpy.log("MAS Android Notif Error: " + str(e))
                print("MAS Android Notif Error: " + str(e))

        def mas_android_cancel_all_notifs():
            """
            Cancels the pending notification.
            """
            if not persistent.mas_android_notif_enabled:
                return
            try:
                context = PythonActivity.mActivity
                alarm_manager = cast(AlarmManager, context.getSystemService(Context.ALARM_SERVICE))
                
                intent = Intent(NOTIF_ACTION)
                intent.setPackage(context.getPackageName())
                
                # Must match flags
                flags = 201326592 
                
                pending_intent = PendingIntent.getBroadcast(
                    context, 
                    MAS_NOTIF_ID, 
                    intent, 
                    flags
                )
                
                alarm_manager.cancel(pending_intent)
                renpy.log("[MAS_ANDROID] Cancelled Native Notif")
                print("[MAS_ANDROID] Cancelled Native Notif")
            except Exception as e:
                renpy.log("MAS Android Cancel Error: " + str(e))
                print("MAS Android Cancel Error: " + str(e))

        # Expose functions
        store.mas_android_schedule_notif = mas_android_schedule_notif
        store.mas_android_cancel_all_notifs = mas_android_cancel_all_notifs
        
        # FORCE ENABLE FOR DEBUGGING
        if persistent.mas_android_notif_enabled is None:
            persistent.mas_android_notif_enabled = True
            renpy.log("[MAS_ANDROID] DEBUG: Persistent default enabled set to TRUE")

    else:
        # Fallback for PC or if Pyjnius missing
        def mas_android_schedule_notif(title, message, delay_seconds):
            # Just log it for debugging
            print("[MAS_ANDROID] Would schedule: '{}' in {} seconds.".format(message, delay_seconds))
            
        def mas_android_cancel_all_notifs():
            print("[MAS_ANDROID] Cancelling all notifications.")

        store.mas_android_schedule_notif = mas_android_schedule_notif
        store.mas_android_cancel_all_notifs = mas_android_cancel_all_notifs
