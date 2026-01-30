init python:
    import random
    import datetime

    """
    Submod Notification Decision Logic
    
    This module serves as the intelligence layer for the notification system.
    It bridges the gap between in-game events (like farewells) and the Android backend.
    
    Key Responsibilities:
    Selecting the appropriate message text based on affection level and category.
    Determining the scheduling parameters (delay, interactivity) based on the user's farewell choice.
    """

    def MAS_AndroidNotifs_GetMessage(category):
        """
        Retrieves a context-aware notification message.
        
        This function queries the global notification data dictionary to find a message
        that matches the requested category (e.g., 'farewell_sleep') and the current
        affection level of Monika (e.g., 'normal', 'happy', 'love').
        
        It implements a fallback mechanism: if a message is not found for the current
        affection level, it degrades gracefully to 'normal' messages to ensure
        something is always displayed.
        
        IN:
            category (str) - The classification key for the desired message.
            
        RETURNS:
            str - The fully substituted, human-readable notification body text, 
                or None if no suitable message could be resolved.
        """
        
        """
        Affection Level Resolution
        Determine the highest active affection state to select the most appropriate tone.
        Logic proceeds from lowest (Normal) to highest (Love), overwriting the key
        as it climbs the ladder of affection.
        """
        aff_key = "normal"
        
        if store.mas_isMoniHappy(higher=True):
            aff_key = "happy"
            
        if store.mas_isMoniAff(higher=True):
            aff_key = "affectionate"

        if store.mas_isMoniEnamored(higher=True):
            aff_key = "enamored"

        if store.mas_isMoniLove(higher=True):
            aff_key = "love"
            
        """
        Dictionary Lookup
        Access the main data structure using the resolved affection key.
        """
        cat_dict = store.mas_android_notifs_data.get(aff_key, {})
        
        """
        Message Retrieval & Fallback Strategy
        First, attempt to find messages for the specific requested category.
        If empty, and the category is 'errand' or 'game' related, fallback to 'farewell_general'.
        """
        messages = cat_dict.get(category)
        
        if not messages:
            if category in ["farewell_short_errand", "mas_farewell_playgame"]:
                messages = cat_dict.get("farewell_general")
        
        if not messages:
            """
            Final Fallback:
            If the current affection level has no messages for this category (e.g., incomplete data),
            fallback to the 'normal' affection level to guarantee a result.
            """
            fallback_dict = store.mas_android_notifs_data.get("normal", {})
            messages = fallback_dict.get(category)
            
        if not messages:
            return None

        """
        Selection & Processing
        Randomly select one message from the list to provide variety.
        If the entry is a dictionary (common in MAS data structures), extract the string content.
        Finally, apply Ren'Py substitution to handle variables like [player].
        """
        final_text = random.choice(messages)
        
        if isinstance(final_text, dict):
            final_text = final_text.get("msg", "Te estaré esperando...")

        final_text = renpy.substitute(final_text)
        
        return final_text

    def MAS_AndroidNotifs_CheckFarewell(farewell_label):
        """
        Evaluates a farewell event and schedules a corresponding notification.
        
        This function categorizes the farewell type into 'Normal' (Passive) or 'Interactive' (Sticky),
        calculates the appropriate delay based on user settings, and dispatches the
        schedule request to the backend.
        
        IN:
            farewell_label (str) - The internal label of the farewell event that occurred.
        """
        
        """
        Pre-Flight Checks
        Abort if the global notification system is disabled or if the user has specifically
        opted out of return reminders.
        """
        if not persistent.mas_android_notif_enabled:
            return

        if not persistent.mas_android_return_reminders:
            return

        """
        Classification Lists
        
        1. NORMAL (Passive) Farewells:
            These result in a standard notification with no interaction buttons.
            Used for defined activities like sleeping, working, or classes.
        """
        NORMAL_FAREWELLS = [
            "bye_prompt_to_class",
            "bye_prompt_eat",
            "bye_prompt_sleep", 
            "bye_going_to_sleep",
            "bye_going_shopping",
            "bye_prompt_to_work"
        ]

        """
        2. INTERACTIVE (Sticky) Farewells:
            These result in a high-priority notification with 'ACTION' buttons.
            Used for shorter absences or generic goodbyes where Monika expects to check in.
        """
        INTERACTIVE_FAREWELLS = [
            "bye_prompt_housework",
            "bye_prompt_workout",
            "bye_prompt_game",
            "bye_prompt_hangout",
            # Group: Generic Goodbyes
            "bye_goodbye",
            "bye_sayanora",
            "bye_farewellfornow", 
            "bye_untilwemeetagain", 
            "bye_take_care"
        ]

        """
        Logic Initialization
        Set defaults for category, delay, and actions.
        """
        category = "farewell_general"
        delay_seconds = 60 
        actions = None

        """
        Delay Calculation
        Determines the wait time based on the user's 'Frequency' slider setting.
        
        Mapping:
        1: Passive (3 min)
        2: Normal (2 min)
        3: Attentive (1 min)
        4: Intense (30s)
        5: Possessive (15s)
        """
        idx = persistent.mas_android_frequency_index
        if idx == 1: interactive_delay = 180
        elif idx == 2: interactive_delay = 120
        elif idx == 3: interactive_delay = 60
        elif idx == 4: interactive_delay = 30
        else: interactive_delay = 15

        if farewell_label in NORMAL_FAREWELLS:
            """
            Branch: Passive Notification
            Calculates a realistic delay based on the activity type (e.g., 8 hours for sleep).
            Note: For testing purposes, some delays are currently shortened.
            """
            
            if farewell_label == "bye_prompt_to_class":
                category = "farewell_class"
                delay_seconds = 30 # Placeholder for testing (real logic would be ~hours)
            
            elif farewell_label in ["bye_prompt_sleep", "bye_going_to_sleep"]:
                category = "farewell_sleep"
                delay_seconds = random.randint(7 * 3600, 9 * 3600)
            
            elif farewell_label == "bye_prompt_to_work":
                category = "farewell_work"
                delay_seconds = random.randint(6 * 3600, 8 * 3600)
            
            elif farewell_label == "bye_going_shopping":
                category = "farewell_going_out" 
                delay_seconds = 30 
            
            elif farewell_label == "bye_prompt_eat":
                category = "farewell_general" 
                delay_seconds = random.randint(1 * 3600, 2 * 3600)

            # Explicitly disable actions for passive notifications
            actions = None 

        elif farewell_label in INTERACTIVE_FAREWELLS:
            """
            Branch: Interactive Notification
            Uses the user-configured 'interactive_delay'.
            Assigns action buttons (e.g., "I'm coming") to the notification.
            """
            
            delay_seconds = interactive_delay

            if farewell_label == "bye_prompt_housework":
                category = "farewell_going_out" 
            
            elif farewell_label == "bye_prompt_workout":
                category = "farewell_going_out" 

            elif farewell_label == "bye_prompt_game":
                category = "mas_farewell_playgame"

            elif farewell_label == "bye_prompt_hangout":
                category = "farewell_going_out"

            else:
                # Default for generic goodbyes
                category = "absence_short"

            # Assign interactive buttons
            actions = (u"Ya voy", u"Después")

        else:
            """
            Unrecognized Farewell
            If the farewell label is not in our allow-list, we do not schedule a notification.
            This prevents spamming for unknown or trivial events.
            """
            return


        """
        Execution
        Resolve the message text and dispatch the schedule command to the backend.
        Includes a safety check (`hasattr`) to prevent crashes on PC where the backend
        might be partially initialized.
        """
        message = MAS_AndroidNotifs_GetMessage(category)
        
        if message:
            if hasattr(store, "mas_android_schedule_notif"):
                store.mas_android_schedule_notif("[m_name]", message, delay_seconds, actions)
