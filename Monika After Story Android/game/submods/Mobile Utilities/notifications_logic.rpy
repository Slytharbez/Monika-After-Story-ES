init python:
    import random
    import datetime

    """
    Submod Notification Logic
    
    This file handles the decision-making process for scheduling notifications based on user actions (farewells).
    It acts as the bridge between MAS logic and the Android backend.
    """

    def MAS_AndroidNotifs_GetMessage(category):
        """
        Retrieves a notification message based on the current affection level and category.
        Handles text substitution for player and monika names.
        
        Args:
            category (str): The key in the notification dictionary (e.g., 'farewell_goodbye', 'farewell_sleep').
            
        Returns:
            str: The formatted notification body text, or None if no message found.
        """
        # Determine affection key mostly based on database keys
        # Fallback to 'normal' if affection level not explicitly handled or empty
        aff_key = "normal"
        if store.mas_isMoniEnamored(higher=True):
            aff_key = "enamored"
        elif store.mas_isMoniAff(higher=True):
            aff_key = "affectionate"
        elif store.mas_isMoniHappy(higher=True):
            aff_key = "happy"
            
        # Access the dictionary
        # store.mas_android_notifs_data is the main dict
        
        # Safe get for affection level
        cat_dict = store.mas_android_notifs_data.get(aff_key, {})
        
        # Get list of messages for the category
        # FALLBACK LOGIC: If specific category missing, try general fallback for short errands/playgame
        messages = cat_dict.get(category)
        
        if not messages:
            if category in ["farewell_short_errand", "mas_farewell_playgame"]:
                # Fallback to general if specific errand messages are missing
                messages = cat_dict.get("farewell_general")
        
        if not messages:
            # If still no messages, try 'normal' affection level as last resort
            fallback_dict = store.mas_android_notifs_data.get("normal", {})
            messages = fallback_dict.get(category)
            
        if not messages:
            return None

        # Pick a random message
        final_text = random.choice(messages)
        
        # TEXT SUBSTITUTION
        # Manually substitute common tags since we are outside Ren'Py dialogue engine
        final_text = renpy.substitute(final_text)
        
        return final_text

    def MAS_AndroidNotifs_CheckFarewell(farewell_label):
        """
        Determines the notification schedule based on the farewell label used.
        
        Args:
            farewell_label (str): The label of the farewell prompt selected by the user.
        """
        
        if not persistent.mas_android_notif_enabled:
            return

        # --- A. DO NOTHING GROUP ---
        #restart, taking somewhere
        if farewell_label in ["bye_restart", "bye_taking_somewhere"]:
            return

        delay_seconds = 0
        category = "farewell_general"
        
        # --- B. SLEEP GROUP (7-9 hours) ---
        if farewell_label in ["bye_prompt_sleep", "bye_going_to_sleep"]:
            category = "farewell_sleep"
            # Random delay between 7 and 9 hours (in seconds)
            delay_seconds = random.randint(7 * 3600, 9 * 3600)

        # --- C. WORK/SCHOOL GROUP (6-8 hours) ---
        elif farewell_label == "bye_prompt_to_work":
            category = "farewell_work"
            delay_seconds = random.randint(6 * 3600, 8 * 3600)
            
        elif farewell_label == "bye_prompt_to_class":
            category = "farewell_class"
            # TEST MODE: 1 minute
            delay_seconds = 60

        # --- D. SHORT ERRANDS GROUP (2-4 hours) ---
        # Mapping common short absence labels
        elif farewell_label in [
            "bye_prompt_eat", 
            "bye_prompt_shopping", 
            "bye_prompt_chores", 
            "bye_prompt_workout", 
            "bye_prompt_hangout", 
            "bye_prompt_game"
        ]:
            if farewell_label == "bye_prompt_game":
                # Use specific category if data exists, handled in GetMessage
                category = "mas_farewell_playgame" 
            else:
                # 'farewell_short_errand' does not exist in notifications.rpy data
                # Using 'farewell_going_out' instead which is defined.
                category = "farewell_going_out"
            
            # TEST MODE: 1 minute for Shopping and Chores
            if farewell_label in ["bye_prompt_shopping", "bye_prompt_chores"]:
                delay_seconds = 60
            else:
                delay_seconds = random.randint(2 * 3600, 4 * 3600)

        # --- E. LONG ABSENCE GROUP (3 days) ---
        elif farewell_label == "bye_long_absence":
            category = "absence_long"
            delay_seconds = 3 * 24 * 3600 # 3 days
            # TODO: Attach specific interactive buttons for this case in backend

        # --- F. GENERIC/DEFAULT GROUP ---
        # Covers 'bye_goodbye', 'bye_sayanora', etc.
        else:
            category = "absence_short"
            # Delay based on persistent.mas_android_frequency_index
            # 1: 3m, 2: 2m, 3: 1m, 4: 30s, 5: 15s
            idx = persistent.mas_android_frequency_index
            if idx == 1:
                delay_seconds = 180
            elif idx == 2:
                delay_seconds = 120
            elif idx == 3:
                delay_seconds = 60
            elif idx == 4:
                delay_seconds = 30
            else: # idx 5
                delay_seconds = 15

        # --- EXECUTION ---
        message = MAS_AndroidNotifs_GetMessage(category)
        
        if message:
            # Call backend to schedule
            # Check if backend function exists (to prevent PC errors)
            if hasattr(store, "mas_android_schedule_notif"):
                store.mas_android_schedule_notif("Monika", message, delay_seconds)

