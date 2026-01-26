init python:
    """
    Submod Notification Data
    
    This file initializes the directory of data used for the notification system.
    Strictly follows the 'no hash comments' rule.
    """

    """
    Register persistent variables
    Default: Notifications Enabled = True
    """
    if persistent.mas_android_notif_enabled is None:
        persistent.mas_android_notif_enabled = True

    """
    Default: Sound/Vibration Enabled = True
    """
    if persistent.mas_android_notif_sound is None:
        persistent.mas_android_notif_sound = True

    """
    Default: Calendar Events (Birthdays, Holidays) = True
    """
    if persistent.mas_android_calendar_events is None:
        persistent.mas_android_calendar_events = True
        
    """
    Default: Action Buttons (Reply/Dismiss) = True
    """
    if persistent.mas_android_action_buttons is None:
        persistent.mas_android_action_buttons = True

    """
    Index for Notification Absence Frequency (Slider in UI)
    Range: 1 (Discreet) to 5 (Obsessive)
    Default: 2 (Normal)
    """
    if persistent.mas_android_frequency_index is None:
        persistent.mas_android_frequency_index = 2

    """
    Sound path for Android notifications
    """
    store.mas_android_notif_sound_path = "mod_assets/sounds/effects/notif.wav"
