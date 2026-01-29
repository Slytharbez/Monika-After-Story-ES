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
        # Determine affection key from Lowest to Highest (Overwriting)
        # 1. Normal (Default)
        aff_key = "normal"
        
        # 2. Happy (and higher)
        if store.mas_isMoniHappy(higher=True):
            aff_key = "happy"
            
        # 3. Affectionate (and higher)
        if store.mas_isMoniAff(higher=True):
            aff_key = "affectionate"

        # 4. Enamored (and higher)
        if store.mas_isMoniEnamored(higher=True):
            aff_key = "enamored"

        # 5. Love (and higher)
        if store.mas_isMoniLove(higher=True):
            aff_key = "love"
            
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
        
        # --- FIX: Extract Text from Dict ---
        # If the chosen item is a dictionary (common in MAS), extract 'msg'
        if isinstance(final_text, dict):
            final_text = final_text.get("msg", "Te estaré esperando...")

        # TEXT SUBSTITUTION
        # Manually substitute common tags since we are outside Ren'Py dialogue engine
        final_text = renpy.substitute(final_text)
        
        return final_text

    def MAS_AndroidNotifs_CheckFarewell(farewell_label):
        """
        Determines the notification schedule based on the farewell label used.
        Separates logic into NORMAL (Passive) and INTERACTIVE (Sticky) types.
        """
        
        if not persistent.mas_android_notif_enabled:
            return

        # FILTER: Return Reminders (Farewells)
        # If the user disabled "Recordatorios de Regreso", abort immediately.
        # This prevents Type B/C notifications from being scheduled.
        if not persistent.mas_android_return_reminders:
            return

        # --- LIST DEFINITIONS ---
        
        # 1. Normal Notifications (Passive - No Actions)
        # "Voy a clases", "Voy a comer...", "Voy a dormir", "Voy a ir de compras", "Voy a trabajar"
        NORMAL_FAREWELLS = [
            "bye_prompt_to_class",
            "bye_prompt_eat",
            "bye_prompt_sleep", 
            "bye_going_to_sleep", # Sleep variant
            "bye_going_shopping",
            "bye_prompt_to_work"
        ]

        # 2. Interactive Notifications (Sticky - Has Actions)
        # "Voy a hacer algunas tareas domésticas", "Voy a hacer ejercicio", "Voy a jugar otra cosa", 
        # "Voy a salir con mis amigos", "Adiós"
        INTERACTIVE_FAREWELLS = [
            "bye_prompt_housework",
            "bye_prompt_workout",
            "bye_prompt_game",
            "bye_prompt_hangout",
            # Group "Adiós" (Generic Goodbyes)
            "bye_goodbye",
            "bye_sayanora",
            "bye_farewellfornow", 
            "bye_untilwemeetagain", 
            "bye_take_care"
        ]

        # --- LOGIC ---

        category = "farewell_general"
        delay_seconds = 60 # Default delay
        actions = None

        # --- CALCULATE SLIDER DELAY ---
        # Based on persistent.mas_android_frequency_index
        # 1: 3m (180s), 2: 2m (120s), 3: 1m (60s), 4: 30s, 5: 15s
        idx = persistent.mas_android_frequency_index
        if idx == 1: interactive_delay = 180
        elif idx == 2: interactive_delay = 120
        elif idx == 3: interactive_delay = 60
        elif idx == 4: interactive_delay = 30
        else: interactive_delay = 15

        if farewell_label in NORMAL_FAREWELLS:
            # --- NORMAL (PASSIVE) LOGIC ---
            
            if farewell_label == "bye_prompt_to_class":
                category = "farewell_class"
                delay_seconds = 30 # Test duration (Normal: random 4-6h)
            
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
                # Use general or specific if available
                category = "farewell_general" 
                delay_seconds = random.randint(1 * 3600, 2 * 3600)

            # FORCE OFF ACTIONS for Normal types
            actions = None 

        elif farewell_label in INTERACTIVE_FAREWELLS:
            # --- INTERACTIVE (STICKY) LOGIC ---
            # ALL Interactive notifications now use the SLIDER variable
            
            delay_seconds = interactive_delay

            if farewell_label == "bye_prompt_housework":
                # Currently mapping to general/going_out in data, but we want the ACTIONS
                category = "farewell_going_out" 
            
            elif farewell_label == "bye_prompt_workout":
                category = "farewell_going_out" 

            elif farewell_label == "bye_prompt_game":
                category = "mas_farewell_playgame"

            elif farewell_label == "bye_prompt_hangout":
                category = "farewell_going_out"

            else:
                # Generic "Adiós" group
                category = "absence_short"

            # FORCE ACTIONS for Interactive types
            actions = (u"Ya voy", u"Después")

        else:
            # Farewell NOT in allowed lists -> IGNORE
            # As per instruction: "aquellas que no estén en esta lista las deberás quitar"
            return


        # --- EXECUTION ---
        message = MAS_AndroidNotifs_GetMessage(category)
        
        if message:
            # Call backend to schedule
            # Check if backend function exists (to prevent PC errors)
            if hasattr(store, "mas_android_schedule_notif"):
                store.mas_android_schedule_notif("[m_name]", message, delay_seconds, actions)
