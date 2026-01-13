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
