init offset = 5






init -5 python:
    def mas_setupIdleMode(brb_label=None, brb_callback_label=None):
        """
        Setups idle mode

        IN:
            brb_label - the label of this brb event, if None, use the current label
                (Default: None)
            brb_callback_label - the callback label of this brb event, if None, we build it here
                (Default: None)
        """
        
        if brb_label is None and renpy.has_label(mas_submod_utils.current_label):
            brb_label = mas_submod_utils.current_label
        
        
        mas_moni_idle_disp.add_by_tag("idle_mode_exps")
        
        
        mas_globals.in_idle_mode = True
        persistent._mas_in_idle_mode = True
        
        
        renpy.save_persistent()
        
        
        if brb_callback_label is None and brb_label is not None:
            brb_callback_label = brb_label + "_callback"
        if brb_callback_label is not None and renpy.has_label(brb_callback_label):
            mas_idle_mailbox.send_idle_cb(brb_callback_label)

    def mas_resetIdleMode(clear_idle_data=True):
        """
        Resets idle mode

        This is meant to basically clear idle mode for holidays or other
        things that hijack main flow

        IN:
            clear_idle_data - whether or not clear persistent idle data
                (Default: True)

        OUT:
            string with idle callback label
            or None if it was reset before
        """
        
        mas_moni_idle_disp.remove_by_tag("idle_mode_exps")
        
        
        mas_globals.in_idle_mode = False
        persistent._mas_in_idle_mode = False
        if clear_idle_data:
            persistent._mas_idle_data.clear()
        
        renpy.save_persistent()
        
        return mas_idle_mailbox.get_idle_cb()


init 5 python in mas_brbs:
    import random
    import store
    from store import (
        MASMoniIdleExp,
        MASMoniIdleExpGroup,
        MASMoniIdleExpRngGroup
    )

    idle_mode_exps = MASMoniIdleExpRngGroup(
        [
            
            MASMoniIdleExpGroup(
                [
                    MASMoniIdleExp("5rubla", duration=(10, 20)),
                    MASMoniIdleExp("5rublu", duration=(5, 10)),
                    MASMoniIdleExp("5rubsu", duration=(20, 30)),
                    MASMoniIdleExp("5rubla", duration=(5, 10)),
                ],
                weight=30
            ),
            
            MASMoniIdleExpGroup(
                [
                    MASMoniIdleExp("5rubla", duration=(10, 20)),
                    MASMoniIdleExp("5gsbsu", duration=(20, 30)),
                    MASMoniIdleExp("5tsbsu", duration=1),
                    MASMoniIdleExp("1hubfu", duration=(5, 10)),
                    MASMoniIdleExp("1hubsa", duration=(5, 10)),
                    MASMoniIdleExp("1hubla", duration=(5, 10))
                ],
                weight=30
            ),
            
            MASMoniIdleExpGroup(
                [
                    MASMoniIdleExp("1lublu", duration=(10, 20)),
                    MASMoniIdleExp("1msblu", duration=(5, 10)),
                    MASMoniIdleExp("1msbsu", duration=(20, 30)),
                    MASMoniIdleExp("1hubsu", duration=(5, 10)),
                    MASMoniIdleExp("1hubla", duration=(5, 10))
                ],
                weight=30
            ),
            
            MASMoniIdleExpGroup(
                [
                    MASMoniIdleExpRngGroup(
                        [
                            
                            MASMoniIdleExpGroup(
                                [
                                    MASMoniIdleExp("1gubla", duration=(0.9, 1.8)),
                                    MASMoniIdleExp("1mubla", duration=(0.9, 1.8)),
                                    MASMoniIdleExp("1gubla", duration=(0.9, 1.8)),
                                    MASMoniIdleExp("1mubla", duration=(0.9, 1.8)),
                                    MASMoniIdleExp("1gsbsu", duration=(0.9, 1.8)),
                                    MASMoniIdleExp("1msbsu", duration=(0.9, 1.8)),
                                    MASMoniIdleExp("1gsbsu", duration=(0.9, 1.8)),
                                    MASMoniIdleExp("1msbsu", duration=(0.9, 1.8))
                                ]
                            ),
                            
                            MASMoniIdleExpGroup(
                                [
                                    MASMoniIdleExp("1mubla", duration=(0.9, 1.8)),
                                    MASMoniIdleExp("1gubla", duration=(0.9, 1.8)),
                                    MASMoniIdleExp("1mubla", duration=(0.9, 1.8)),
                                    MASMoniIdleExp("1gubla", duration=(0.9, 1.8)),
                                    MASMoniIdleExp("1msbsu", duration=(0.9, 1.8)),
                                    MASMoniIdleExp("1gsbsu", duration=(0.9, 1.8)),
                                    MASMoniIdleExp("1msbsu", duration=(0.9, 1.8)),
                                    MASMoniIdleExp("1gsbsu", duration=(0.9, 1.8))
                                ]
                            )
                        ],
                        max_uses=1
                    ),
                    MASMoniIdleExp("1tsbfu", duration=1),
                    MASMoniIdleExp("1hubfu", duration=(4, 8)),
                    MASMoniIdleExp("1hubsa", duration=(4, 8)),
                    MASMoniIdleExp("1hubla", duration=(4, 8))
                ],
                weight=10
            )
        ],
        max_uses=1,
        aff_range=(store.mas_aff.AFFECTIONATE, None),
        weight=10,
        tag="idle_mode_exps"
    )

    WB_QUIPS_NORMAL = [
        _("So, what else did you want to do today?"),
        _("What else did you want to do today?"),
        _("Is there anything else you wanted to do today?"),
        _("What else should we do today?")
    ]

    def get_wb_quip():
        """
        Picks a random welcome back quip and returns it
        Should be used for normal+ quips

        OUT:
            A randomly selected quip for coming back to the spaceroom
        """
        return renpy.substitute(random.choice(WB_QUIPS_NORMAL))

    def was_idle_for_at_least(idle_time, brb_evl):
        """
        Checks if the user was idle (from the brb_evl provided) for at least idle_time

        IN:
            idle_time - Minimum amount of time the user should have been idle for in order to return True
            brb_evl - Eventlabel of the brb to use for the start time

        OUT:
            boolean:
                - True if it has been at least idle_time since seeing the brb_evl
                - False otherwise
        """
        brb_ev = store.mas_getEV(brb_evl)
        return brb_ev and brb_ev.timePassedSinceLastSeen_dt(idle_time)




label mas_brb_back_to_idle:

    if globals().get("brb_label", -1) == -1:
        return

    python:
        mas_idle_mailbox.send_idle_cb(brb_label + "_callback")
        persistent._mas_idle_data[brb_label] = True
        mas_globals.in_idle_mode = True
        persistent._mas_in_idle_mode = True
        renpy.save_persistent()
        mas_dlgToIdleShield()

    return "idle"



label mas_brb_generic_low_aff_callback:
    if mas_isMoniDis(higher=True):
        python:
            cb_line = renpy.substitute(renpy.random.choice([
                _("Oh...{w=0.3}you're back."),
                _("Oh...{w=0.3}welcome back."),
                _("All done?"),
                _("Welcome back."),
                _("Oh...{w=0.3}there you are."),
            ]))

        m 2ekc "[cb_line]"
    else:

        m 6ckc "..."

    return


init python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_idle_brb",
            prompt="I'll be right back",
            category=['be right back'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label monika_idle_brb:
    if mas_isMoniAff(higher=True):
        m 1eua "Alright, [player]."

        show monika 1eta at t21
        python:

            brb_reason_options = [
                (_("I'm going to get something."), True, False, False),
                (_("I'm going to do something."), True, False, False),
                (_("I'm going to make something."), True, False, False),
                (_("I have to check something."), True, False, False),
                (_("Someone's at the door."), True, False, False),
                (_("Nope."), None, False, False),
            ]

            renpy.say(m, "Doing anything specific?", interact=False)
        call screen mas_gen_scrollable_menu(brb_reason_options, mas_ui.SCROLLABLE_MENU_TALL_AREA, mas_ui.SCROLLABLE_MENU_XALIGN)
        show monika at t11

        if _return:
            m 1eua "Oh alright.{w=0.2} {nw}"
            extend 3hub "Hurry back, I'll be waiting here for you~"
        else:

            m 1hub "Hurry back, I'll be waiting here for you~"

    elif mas_isMoniNormal(higher=True):
        m 1hub "Hurry back, [player]!"

    elif mas_isMoniDis(higher=True):
        m 2rsc "Oh...{w=0.5}okay."
    else:

        m 6ckc "..."


    $ persistent._mas_idle_data["monika_idle_brb"] = True
    return "idle"

label monika_idle_brb_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    if mas_isMoniAff(higher=True):
        m 1hub "Welcome back, [player]. I missed you~"
        m 1eua "[wb_quip]"

    elif mas_isMoniNormal(higher=True):
        m 1hub "Welcome back, [player]!"
        m 1eua "[wb_quip]"
    else:

        call mas_brb_generic_low_aff_callback

    return

init python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_idle_writing",
            prompt="I'm going to write for a bit",
            category=['be right back'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label monika_idle_writing:
    if mas_isMoniNormal(higher=True):
        if (
            mas_isMoniHappy(higher=True)
            and random.randint(1,5) == 1
        ):
            m 1eub "Oh! You're going to{cps=*2} write me a love letter, [player]?{/cps}{nw}"
            $ _history_list.pop()
            m "Oh! You're going to{fast} go write something?"
        else:

            m 1eub "Oh! You're going to go write something?"

        m 1hua "That makes me so glad!"
        m 3eua "Maybe someday you could share it with me...{w=0.3} {nw}"
        extend 3hua "I'd love to read your work, [player]!"
        m 3eua "Anyway, just let me know when you're done."
        m 1hua "I'll be waiting right here for you~"

    elif mas_isMoniUpset():
        m 2esc "Alright."

    elif mas_isMoniDis():
        m 6lkc "I wonder what you have on your mind..."
        m 6ekd "Don't forget to come back when you're done..."
    else:

        m 6ckc "..."

    $ persistent._mas_idle_data["monika_idle_writing"] = True
    return "idle"

label monika_idle_writing_callback:

    if mas_isMoniNormal(higher=True):
        $ wb_quip = mas_brbs.get_wb_quip()
        m 1eua "Done writing, [player]?"
        m 1eub "[wb_quip]"
    else:

        call mas_brb_generic_low_aff_callback

    return

init python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_idle_shower",
            prompt="I'm going to take a shower",
            category=['be right back'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label monika_idle_shower:
    if mas_isMoniLove():
        m 1eua "Going to go shower?"

        if renpy.random.randint(1, 50) == 1:
            m 3tub "Can I come with you?{nw}"
            $ _history_list.pop()
            show screen mas_background_timed_jump(2, "bye_brb_shower_timeout")
            menu:
                m "Can I come with you?{fast}"
                "Yes.":

                    hide screen mas_background_timed_jump
                    m 2wubsd "Oh, uh...{w=0.5}you sure answered that fast."
                    m 2hkbfsdlb "You...{w=0.5}sure seem eager to let me tag along, huh?"
                    m 2rkbfa "Well..."
                    m 7tubfu "I'm afraid you'll just have to go without me while I'm stuck here."
                    m 7hubfb "Sorry, [player], ahaha!"
                    show monika 5kubfu zorder MAS_MONIKA_Z at t11 with dissolve_monika
                    m 5kubfu "Maybe another time~"
                "No.":

                    hide screen mas_background_timed_jump
                    m 2eka "Aw, you rejected me so fast."
                    m 3tubsb "Are you shy, [player]?"
                    m 1hubfb "Ahaha!"
                    show monika 5tubfu zorder MAS_MONIKA_Z at t11 with dissolve_monika
                    m 5tubfu "Alright, I won't follow you this time, ehehe~"
        else:

            m 1hua "I'm glad you're keeping yourself clean, [player]."
            m 1eua "Have a nice shower~"

    elif mas_isMoniNormal(higher=True):
        m 1eub "Going to go shower? Alright."
        m 1eua "See you when you're done~"

    elif mas_isMoniUpset():
        m 2esd "Enjoy your shower, [player]..."
        m 2rkc "Hopefully it'll help you clear your mind."

    elif mas_isMoniDis():
        m 6ekc "Hmm?{w=0.5} Have a nice shower, [player]."
    else:

        m 6ckc "..."

    $ persistent._mas_idle_data["monika_idle_shower"] = True
    return "idle"

label monika_idle_shower_callback:
    if mas_isMoniNormal(higher=True):
        if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=60), "monika_idle_shower"):
            m 2rksdlb "That sure was a long time for a shower..."

            m 2eud "Did you take a bath instead?{nw}"
            $ _history_list.pop()
            menu:
                m "Did you take a bath instead?{fast}"
                "Yes.":

                    m 7hub "Oh! {w=0.3}I see!"
                    m 3eua "I hope it was nice and relaxing!"
                "No.":

                    m 7rua "Oh...{w=0.3}maybe you just like really long showers..."
                    m 3duu "Sometimes it can be nice just to feel the water rushing over you...{w=0.3}it can be really soothing."
                    m 1hksdlb "...Or maybe I'm overthinking this and you just didn't come back right away, ahaha!"

        elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=5), "monika_idle_shower"):
            m 1eua "Welcome back, [player]."
            if (
                mas_isMoniLove()
                and renpy.seen_label("monikaroom_greeting_ear_bathdinnerme")
                and mas_getEVL_shown_count("monika_idle_shower") != 1 
                and renpy.random.randint(1,20) == 1
            ):
                m 3tubsb "Now that you've had your shower, would you like your dinner, or maybe{w=0.5}.{w=0.5}.{w=0.5}."
                m 1hubsa "You could just relax with me some more~"
                m 1hub "Ahaha!"
            else:

                m 3hua "I hope you had a nice shower."
                if mas_getEVL_shown_count("monika_idle_shower") == 1:
                    m 3eub "Now we can get back to having some good, {i}clean{/i} fun together..."
                    m 1hub "Ahaha!"
                else:
                    m 3rkbsa "Did you miss me?"
                    m 1huu "Of course you did, ehehe~"
        else:

            m 7rksdlb "That was a pretty short shower, [player]..."
            m 3hub "I guess you must just be really efficient, ahaha!"
            m 1euu "I certainly can't complain, it just means more time together~"

    elif mas_isMoniUpset():
        m 2esc "I hope you enjoyed your shower. {w=0.2}Welcome back, [player]."
    else:

        call mas_brb_generic_low_aff_callback

    return

label bye_brb_shower_timeout:
    hide screen mas_background_timed_jump
    $ _history_list.pop()
    m 1hubsa "Ehehe~"
    m 3tubfu "Nevermind that, [player]."
    m 1hubfb "I hope you have a nice shower!"

    $ persistent._mas_idle_data["monika_idle_shower"] = True
    $ mas_setupIdleMode("monika_idle_shower", "monika_idle_shower_callback")
    return

init python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_idle_game",
            category=['be right back'],
            prompt="I'm going to game for a bit",
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label monika_idle_game:
    if mas_isMoniNormal(higher=True):
        m 1eud "Oh, you're going to play another game?"
        m 1eka "That's alright, [player]."

        label monika_idle_game.skip_intro:
        python:
            gaming_quips = [
                _("Good luck, have fun!"),
                _("Enjoy your game!"),
                _("I'll be cheering you on!"),
                _("Do your best!")
            ]
            gaming_quip=renpy.random.choice(gaming_quips)

        m 3hub "[gaming_quip]"

    elif mas_isMoniUpset():
        m 2tsc "Enjoy your other games."

    elif mas_isMoniDis():
        m 6ekc "Please...{w=0.5}{nw}"
        extend 6dkc "don't forget about me..."
    else:

        m 6ckc "..."

    $ persistent._mas_idle_data["monika_idle_game"] = True

    $ mas_setupIdleMode("monika_idle_game")
    return

label monika_idle_game_callback:
    if mas_isMoniNormal(higher=True):
        m 1eub "Welcome back, [player]!"
        m 1eua "I hope you had fun with your game."
        m 1hua "Ready to spend some more time together? Ehehe~"

    elif mas_isMoniUpset():
        m 2tsc "Had fun, [player]?"

    elif mas_isMoniDis():
        m 6ekd "Oh...{w=0.5} You actually came back to me..."
    else:

        m 6ckc "..."

    return

init python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_idle_coding",
            prompt="I'm going to code for a bit",
            category=['be right back'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label monika_idle_coding:
    if mas_isMoniNormal(higher=True):
        m 1eua "Oh! Going to code something?"

        if persistent._mas_pm_has_code_experience is False:
            m 1etc "I thought you didn't do that."
            m 1eub "Did you pick up programming since we talked about it last time?"

        elif persistent._mas_pm_has_contributed_to_mas or persistent._mas_pm_wants_to_contribute_to_mas:
            m 1tua "Something for me, perhaps?"
            m 1hub "Ahaha~"
        else:

            m 3eub "Do your best to keep your code clean and easy to read."
            m 3hksdlb "...You'll thank yourself later!"

        m 1eua "Anyway, just let me know when you're done."
        m 1hua "I'll be right here, waiting for you~"

    elif mas_isMoniUpset():
        m 2euc "Oh, you're going to code?"
        m 2tsc "Well, don't let me stop you."

    elif mas_isMoniDis():
        m 6ekc "Alright."
    else:

        m 6ckc "..."

    $ persistent._mas_idle_data["monika_idle_coding"] = True
    return "idle"

label monika_idle_coding_callback:
    if mas_isMoniNormal(higher=True):
        $ wb_quip = mas_brbs.get_wb_quip()
        if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=20), "monika_idle_coding"):
            m 1eua "Done for now, [player]?"
        else:
            m 1eua "Oh, done already, [player]?"

        m 3eub "[wb_quip]"
    else:

        call mas_brb_generic_low_aff_callback

    return


init python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_idle_workout",
            prompt="I'm going to work out for a bit",
            category=['be right back'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label monika_idle_workout:
    if mas_isMoniNormal(higher=True):
        m 1hub "Okay, [player]!"

        if persistent._mas_pm_works_out is False:
            m 3eub "Working out is a great way to take care of yourself!"
            m 1eka "I know it might be hard to start out,{w=0.2}{nw}"
            extend 3hua " but it's definitely a habit worth forming."
        else:

            m 1eub "It's good to know you're taking care of your body!"

        m 3esa "You know how the saying goes, 'A healthy mind in a healthy body.'"
        m 3hua "So go work up a good sweat, [player]~"
        m 1tub "Just let me know when you've had enough."

    elif mas_isMoniUpset():
        m 2esc "Good to know you're taking care of{cps=*2} something, at least.{/cps}{nw}"
        $ _history_list.pop()
        m "Good to know you're taking care of{fast} yourself, [player]."
        m 2euc "I'll be waiting for you to get back."

    elif mas_isMoniDis():
        m 6ekc "Alright."
    else:

        m 6ckc "..."

    $ persistent._mas_idle_data["monika_idle_workout"] = True
    return "idle"

label monika_idle_workout_callback:
    if mas_isMoniNormal(higher=True):
        $ wb_quip = mas_brbs.get_wb_quip()
        if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=60), "monika_idle_workout"):



            m 2esa "You sure took your time, [player].{w=0.3}{nw}"
            extend 2eub " That must've been one heck of a workout."
            m 7eka "It's good to push your limits, but you shouldn't overdo it."

        elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=10), "monika_idle_workout"):
            m 1esa "Done with your workout, [player]?"
        else:

            m 1euc "Back already, [player]?"
            m 1eka "I'm sure you can go on for a bit longer if you try."
            m 3eka "Taking breaks is fine, but you shouldn't leave your workouts unfinished."
            m 3ekb "Are you sure you can't keep going?{nw}"
            $ _history_list.pop()
            menu:
                m "Are you sure you can't keep going?{fast}"
                "I'm sure.":

                    m 1eka "That's okay."
                    m 1hua "I'm sure you did your best, [player]~"
                "I'll try to keep going.":


                    m 1hub "That's the spirit!"


                    return "idle"

        m 3eua "Make sure to rest properly and maybe get a snack to get some energy back."
        m 3eub "[wb_quip]"

    elif mas_isMoniUpset():
        m 2euc "Done with your workout, [player]?"
    else:

        call mas_brb_generic_low_aff_callback

    return

init python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_idle_nap",
            prompt="I'm going to take a nap",
            category=['be right back'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label monika_idle_nap:
    if mas_isMoniNormal(higher=True):
        m 1eua "Going to take a nap, [player]?"
        m 3eua "They're a healthy way to rest during the day if you're feeling tired."
        m 3hua "I'll watch over you, don't worry~"
        m 1hub "Sweet dreams!"

    elif mas_isMoniUpset():
        m 2eud "Alright, I hope you feel rested afterwards."
        m 2euc "I hear naps are good for you, [player]."

    elif mas_isMoniDis():
        m 6ekc "Alright."
    else:

        m 6ckc "..."

    $ persistent._mas_idle_data["monika_idle_nap"] = True
    return "idle"

label monika_idle_nap_callback:
    if mas_isMoniNormal(higher=True):
        $ wb_quip = mas_brbs.get_wb_quip()
        if mas_brbs.was_idle_for_at_least(datetime.timedelta(hours=5), "monika_idle_nap"):
            m 2hksdlb "Oh, [player]! You're finally awake!"
            m 7rksdlb "When you said you were going to take a nap, I was expecting you take maybe an hour or two..."
            m 1hksdlb "I guess you must have been really tired, ahaha..."
            m 3eua "But at least after sleeping for so long, you'll be here with me for a while, right?"
            m 1hua "Ehehe~"

        elif mas_brbs.was_idle_for_at_least(datetime.timedelta(hours=1), "monika_idle_nap"):
            m 1hua "Welcome back, [player]!"
            m 1eua "Did you have a nice nap?"
            m 3hua "You were out for some time, so I hope you're feeling rested~"
            m 1eua "[wb_quip]"

        elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=5), "monika_idle_nap"):
            m 1hua "Welcome back, [player]~"
            m 1eub "I hope you had a nice little nap."
            m 3eua "[wb_quip]"
        else:

            m 1eud "Oh, back already?"
            m 1euc "Did you change your mind?"
            m 3eka "Well, I'm not complaining, but you should take a nap if you feel like it later."
            m 1eua "I wouldn't want you to be too tired, after all."

    elif mas_isMoniUpset():
        m 2euc "Done with your nap, [player]?"
    else:

        call mas_brb_generic_low_aff_callback

    return

init python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_idle_homework",
            prompt="I'm going to do some homework",
            category=['be right back'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label monika_idle_homework:
    if mas_isMoniNormal(higher=True):
        m 1eub "Oh, okay!"
        m 1hua "I'm proud of you for taking your studies seriously."
        m 1eka "Don't forget to come back to me when you're done~"

    elif mas_isMoniDis(higher=True):
        m 2euc "Alright...{w=0.5}"
        if random.randint(1,5) == 1:
            m 2rkc "...Good luck with your homework, [player]."
    else:

        m 6ckc "..."

    $ persistent._mas_idle_data["monika_idle_homework"] = True
    return "idle"

label monika_idle_homework_callback:
    if mas_isMoniDis(higher=True):
        m 2esa "All done, [player]?"

        if mas_isMoniNormal(higher=True):
            m 2ekc "I wish I could've been there to help you, but there isn't much I can do about that just yet, sadly."
            m 7eua "I'm sure we could both be a lot more efficient doing homework if we could work together."

            if mas_isMoniAff(higher=True) and random.randint(1,5) == 1:
                m 3rkbla "...Although, that's assuming we don't get {i}too{/i} distracted, ehehe..."

            m 1eua "But anyway,{w=0.2} {nw}"
            extend 3hua "now that you're done, let's enjoy some more time together."
    else:

        m 6ckc "..."

    return

init python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_idle_working",
            prompt="I'm going to work on something",
            category=['be right back'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label monika_idle_working:
    if mas_isMoniNormal(higher=True):
        m 1eua "Alright, [player]."
        m 1eub "Don't forget to take a break every now and then!"

        if mas_isMoniAff(higher=True):
            m 3rkb "I wouldn't want my sweetheart to spend more time on [his] work than with me~"

        m 1hua "Good luck with your work!"

    elif mas_isMoniDis(higher=True):
        m 2euc "Okay, [player]."

        if random.randint(1,5) == 1:
            m 2rkc "...Please come back soon..."
    else:

        m 6ckc "..."

    $ persistent._mas_idle_data["monika_idle_working"] = True
    return "idle"

label monika_idle_working_callback:
    if mas_isMoniNormal(higher=True):
        m 1eub "Finished with your work, [player]?"
        show monika 5hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        m 5hua "Then let's relax together, you've earned it~"

    elif mas_isMoniDis(higher=True):
        m 2euc "Oh, you're back..."
        m 2eud "...Was there anything else you wanted to do, now that you're done with your work?"
    else:

        m 6ckc "..."

    return

init python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_idle_screen_break",
            prompt="My eyes need a break from the screen",
            category=['be right back'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label monika_idle_screen_break:
    if mas_isMoniNormal(higher=True):
        if mas_timePastSince(mas_getEVL_last_seen("monika_idle_screen_break"), mas_getSessionLength()):

            if mas_getSessionLength() < datetime.timedelta(minutes=40):
                m 1esc "Oh,{w=0.3} okay."
                m 3eka "You haven't been here for that long but if you say you need a break, then you need a break."

            elif mas_getSessionLength() < datetime.timedelta(hours=2, minutes=30):
                m 1eua "Going to rest your eyes for a bit?"
            else:

                m 1lksdla "Yeah, you probably need that, don't you?"

            m 1hub "I'm glad you're taking care of your health, [player]."

            if not persistent._mas_pm_works_out and random.randint(1,3) == 1:
                m 3eua "Why not take the opportunity to do a few stretches as well, hmm?"
                m 1eub "Anyway, come back soon!~"
            else:

                m 1eub "Come back soon!~"
        else:

            m 1eua "Taking another break, [player]?"
            m 1hua "Come back soon!~"

    elif mas_isMoniUpset():
        m 2esc "Oh...{w=0.5} {nw}"
        extend 2rsc "Okay."

    elif mas_isMoniDis():
        m 6ekc "Alright."
    else:

        m 6ckc "..."

    $ persistent._mas_idle_data["monika_idle_screen_break"] = True
    return "idle"

label monika_idle_screen_break_callback:
    if mas_isMoniNormal(higher=True):
        $ wb_quip = mas_brbs.get_wb_quip()
        m 1eub "Welcome back, [player]."

        if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=30), "monika_idle_screen_break"):
            m 1hksdlb "You must've really needed that break, considering how long you were gone."
            m 1eka "I hope you're feeling a little better now."
        else:
            m 1hua "I hope you're feeling a little better now~"

        m 1eua "[wb_quip]"
    else:

        call mas_brb_generic_low_aff_callback

    return

init python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_idle_reading",
            prompt="I'm going to read",
            category=['be right back'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label monika_idle_reading:
    if mas_isMoniNormal(higher=True):
        m 1eub "Really? That's great, [player]!"
        m 3lksdla "I'd love to read with you, but my reality has its limits, unfortunately."
        m 1hub "Have fun!"

    elif mas_isMoniDis(higher=True):
        m 2ekd "Oh, alright..."
        m 2ekc "Have a good time, [player]."
    else:

        m 6dkc "..."

    $ persistent._mas_idle_data["monika_idle_reading"] = True
    return "idle"

label monika_idle_reading_callback:
    if mas_isMoniNormal(higher=True):
        if mas_brbs.was_idle_for_at_least(datetime.timedelta(hours=2), "monika_idle_reading"):
            m 1wud "Wow, you were gone for a while...{w=0.3}{nw}"
            extend 3wub "that's great, [player]!"
            m 3eua "Reading is a wonderful thing, so don't worry about getting too caught up in it."
            m 3hksdlb "Besides, it's not like I'm one to talk..."
            show monika 5ekbsa zorder MAS_MONIKA_Z at t11 with dissolve_monika
            m 5ekbsa "If I had my way, we'd be reading together all night long~"

        elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=30), "monika_idle_reading"):
            m 3esa "All done, [player]?"
            m 1hua "Let's relax, you've earned it~"
        else:

            m 1eud "Oh, that was fast."
            m 1eua "I thought you'd be gone a little while longer, but this is fine too."
            m 3ekblu "After all, it lets me spend more time with you~"
    else:

        call mas_brb_generic_low_aff_callback

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
