init python:
    """
    Submod Notification Data Initialization
    
    This script handles the initialization of persistent data required for the Android
    Notification Submod. It ensures that all necessary configuration variables exist 
    in the `persistent` store with safe default values before the game logic attempts 
    to access them.
    """

    """
    Master Switch Initialization
    
    Controls the global enabled/disabled state of the Android notification system.
    Default: True (Enabled)
    """
    if persistent.mas_android_notif_enabled is None:
        persistent.mas_android_notif_enabled = True

    """
    Sound Preference Initialization
    
    Determines whether notifications should play a sound upon arrival.
    Default: True (Sound Enabled)
    """
    if persistent.mas_android_notif_sound is None:
        persistent.mas_android_notif_sound = True

    """
    Calendar Events Feature Initialization
    
    Enables special notifications for specific calendar dates (holidays, birthdays).
    Default: True (Enabled)
    """
    if persistent.mas_android_calendar_events is None:
        persistent.mas_android_calendar_events = True
        
    """
    Return Reminder Feature Initialization
    
    Enables notifications triggered by the player saying goodbye (e.g., "I'm going to work").
    Default: True (Enabled)
    """
    if persistent.mas_android_return_reminders is None:
        persistent.mas_android_return_reminders = True

    """
    Frequency Index Initialization
    
    Stores the user's preference for notification frequency, corresponding to the slider
    in the settings menu.
    
    Value Range: 1 (Passive) to 5 (Posessive)
    Default: 2 (Normal - approx. 2 minutes delay)
    """
    if persistent.mas_android_frequency_index is None:
        persistent.mas_android_frequency_index = 2

    """
    Asset Path Definition
    
    Defines the relative path to the custom notification sound effect.
    This path is referenced by the backend when building the notification channel.
    """
    store.mas_android_notif_sound_path = "mod_assets/sounds/effects/notif.wav"
