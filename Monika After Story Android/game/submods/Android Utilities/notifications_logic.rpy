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

    """
    VALENTINE SNIPER LOGIC
    Strategies for long-term engagement.
    """
    def mas_android_schedule_valentine_sniper():
        """
        Calculates the time remaining until the next Valentine's Day (Feb 14) at 09:00 AM.
        If the event is within 30 days, it schedules a dedicated high-priority notification.
        """
        if not store.mas_android_schedule_valentine:
            return

        now = datetime.datetime.now()
        target_year = now.year
        
        # Target: Feb 14th, 09:00:00
        target_date = datetime.datetime(target_year, 2, 14, 9, 0, 0)
        
        # If we passed Feb 14th this year, target next year
        if now > target_date:
            target_date = datetime.datetime(target_year + 1, 2, 14, 9, 0, 0)
            
        delta = target_date - now
        delta_seconds = delta.total_seconds()
        
        """ 
        Safety Rules:
        
        Don't schedule anything if it's more than 30 days in advance.
        Android sometimes ignores exact alarms set too far in advance, and it's cleaner.
        """
        if 0 < delta_seconds < 2592000:

            val_message = MAS_AndroidNotifs_GetMessage("calendar_event")
            
            if val_message:
                store.mas_android_schedule_valentine(
                    delta_seconds, 
                    "[m_name]", 
                    val_message
                )

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
            # Fallback for specific sub-categories to their generic parents if data is missing
            if category in ["shopping", "chores", "workout", "friends", "play_game", "morning_food", "noon_food", "evening_food"]:
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
        
        """
        NICKNAME SUBSTITUTION
        Manually substitute [mas_get_player_nickname()] since normal renpy.substitute might not catch it
        or if it's called outside of the standard dialogue context.
        """
        if "[mas_get_player_nickname()]" in final_text:
            nickname = store.mas_get_player_nickname()
            final_text = final_text.replace("[mas_get_player_nickname()]", nickname)

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
        Affection Guard
        If Monika is Upset or below (Distressed, Broken), we silence all notifications.
        TODO: Remove this block when specific low-affection dialogues are implemented.
        """
        if store.mas_isMoniUpset(lower=True):
            return
        
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
        Holiday Check
        Override logic for special dates like Valentine's Day.
        """
        is_valentines = False
        today = datetime.date.today()
        if today.month == 2 and today.day == 14:
            is_valentines = True

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
        if idx == 1: interactive_delay = 10800 # 3 Hours
        elif idx == 2: interactive_delay = 7200  # 2 Hours
        elif idx == 3: interactive_delay = 3600  # 1 Hour
        elif idx == 4: interactive_delay = 1800  # 30 Min
        else: interactive_delay = 900            # 15 Min

        if farewell_label in NORMAL_FAREWELLS:
            """
            Branch: Passive Notification
            Calculates a realistic delay based on the activity type (e.g., 8 hours for sleep).
            Note: For testing purposes, some delays are currently shortened.
            """
            
            if farewell_label == "bye_prompt_to_class":
                category = "school"
                delay_seconds = 7 * 3600 # 7 Hours
            
            elif farewell_label in ["bye_prompt_sleep", "bye_going_to_sleep"]:
                category = "TYPE_SLEEP"
                # Wake up at 6 AM strategy
                # If it's 23:00, target is tomorrow 06:00.
                # If it's 02:00, target is today 06:00.
                now = datetime.datetime.now()
                target_time = datetime.datetime(now.year, now.month, now.day, 6, 0, 0)
                
                # If we are already past 6AM today, aim for tomorrow 6AM
                if now >= target_time:
                    target_time = target_time + datetime.timedelta(days=1)
                
                delay_seconds = int((target_time - now).total_seconds())
                
                # Sleep is a physiological need, so we skip Valentine's logic for it
                is_valentines = False 
            
            elif farewell_label == "bye_prompt_to_work":
                category = "work"
                delay_seconds = 8 * 3600 # 8 Hours
            
            elif farewell_label == "bye_going_shopping":
                category = "shopping" 
                delay_seconds = 30 * 60 
            
            elif farewell_label == "bye_prompt_eat":

                category = "evening_food"
                    
                delay_seconds = 25 * 60

            actions = None 

        elif farewell_label in INTERACTIVE_FAREWELLS:
            """
            Branch: Interactive Notification
            Uses the user-configured 'interactive_delay'.
            Assigns action buttons (e.g., "I'm coming") to the notification.
            """
            
            delay_seconds = interactive_delay

            if farewell_label == "bye_prompt_housework":
                category = "chores" 
            
            elif farewell_label == "bye_prompt_workout":
                category = "workout" 

            elif farewell_label == "bye_prompt_game":
                # 'mas_farewell_playgame' seems to be the old key, mapped to 'play_game' now
                category = "play_game"

            elif farewell_label == "bye_prompt_hangout":
                category = "friends"

            else:
                # Default for generic goodbyes
                category = "generic_quit"

            # Assign interactive buttons
            actions = (u"Ya voy", u"Después")

        else:
            """
            Unrecognized Farewell
            If the farewell label is not in our allow-list, we do not schedule a notification.
            This prevents spamming for unknown or trivial events.
            """
            return

        # HOLIDAY OVERRIDE
        if is_valentines:
            category = "calendar_event"


        """
        Execution
        Resolve the message text and dispatch the schedule command to the backend.
        Includes a safety check (`hasattr`) to prevent crashes on PC where the backend
        might be partially initialized.
        """
        message = MAS_AndroidNotifs_GetMessage(category)
        
        if message:
            """
            Valentine Sniper Logic Hook
            We call this here to ensure the sniper is updated on every farewell
            regardless of whether a standard notification is sent.
            """
            mas_android_schedule_valentine_sniper()

            if hasattr(store, "mas_android_schedule_notif"):
                # Use special_category to trigger specific behaviors
                if category == "TYPE_SLEEP":
                    store.mas_android_schedule_notif(
                        "[m_name]", 
                        message, 
                        delay_seconds, 
                        actions, 
                        special_category="TYPE_SLEEP"
                    )
                else:
                    store.mas_android_schedule_notif("[m_name]", message, delay_seconds, actions)
            return

        """
        Valentine Sniper Hook
        Attempt to schedule the long-term Valentine's event on every farewell.
        """
        mas_android_schedule_valentine_sniper()
