



default persistent._mas_apology_time_db = {}





default persistent._mas_apology_reason_use_db = {}

init -10 python in mas_apology:
    apology_db = {}



init python:
    def mas_checkApologies():
        
        if len(persistent._mas_apology_time_db) == 0:
            return
        
        
        current_total_playtime = persistent.sessions['total_playtime'] + mas_getSessionLength()
        
        _today = datetime.date.today()
        
        for ev_label in persistent._mas_apology_time_db.keys():
            if current_total_playtime >= persistent._mas_apology_time_db[ev_label][0] or _today >= persistent._mas_apology_time_db[ev_label][1]:
                
                store.mas_lockEVL(ev_label,'APL')
                persistent._mas_apology_time_db.pop(ev_label)
        
        return


init 5 python:
    addEvent(
       Event(
           persistent.event_database,
           eventlabel='monika_playerapologizes',
           prompt="I want to apologize...",
           category=['you'],
           pool=True,
           unlocked=True
        )
    )

label monika_playerapologizes:



    $ player_apology_reasons = {
        0: "something else.", 
        1: "saying I wanted to break up.",
        2: "joking about having another girlfriend.",
        3: "calling you a murderer.",
        4: "closing the game on you.",
        5: "entering your room without knocking.",
        6: "missing Christmas.",
        7: "forgetting your birthday.",
        8: "not spending time with you on your birthday.",
        9: "the game crashing.",
        10: "the game crashing.", 
        11: "not listening to your speech.",
        12: "calling you evil.",
        13: "not answering you seriously."
    }


    if len(persistent._mas_apology_time_db) > 0:

        $ mas_setEVLPropValues(
            "mas_apology_generic",
            prompt="...for {0}".format(player_apology_reasons.get(mas_apology_reason,player_apology_reasons[0]))
        )
    else:

        if mas_apology_reason == 0:
            $ mas_setEVLPropValues("mas_apology_generic", prompt="...for something.")
        else:

            $ mas_setEVLPropValues(
                "mas_apology_generic",
                prompt="...for {0}".format(player_apology_reasons.get(mas_apology_reason,"something."))
            )



    $ del player_apology_reasons


    python:
        apologylist = [
            (ev.prompt, ev.eventlabel, False, False)
            for ev_label, ev in store.mas_apology.apology_db.iteritems()
            if ev.unlocked and (ev.prompt != "...for something." and ev.prompt != "...for something else.")
        ]


        generic_ev = mas_getEV('mas_apology_generic')

        if generic_ev.prompt == "...for something." or generic_ev.prompt == "...for something else.":
            apologylist.append((generic_ev.prompt, generic_ev.eventlabel, False, False))


        return_prompt_back = ("Nevermind.", False, False, False, 20)


    show monika at t21
    call screen mas_gen_scrollable_menu(apologylist, mas_ui.SCROLLABLE_MENU_MEDIUM_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, return_prompt_back)


    $ apology =_return


    if not apology:
        if mas_apology_reason is not None or len(persistent._mas_apology_time_db) > 0:
            show monika at t11
            if mas_isMoniAff(higher=True):
                m 1ekd "[player], if you're feeling guilty about what happened..."
                m 1eka "You don't have to be afraid of apologizing, we all make mistakes after all."
                m 3eka "We just have to accept what happened, learn from our mistakes, and move on, together. Okay?"
            elif mas_isMoniNormal(higher=True):
                m 1eka "[player]..."
                m "If you want to apologize, go ahead. It'd mean a lot to me if you did."
            elif mas_isMoniUpset():
                m 2rkc "Oh..."
                m "I was kind of--"
                $ _history_list.pop()
                m 2dkc "Nevermind."
            elif mas_isMoniDis():
                m 6rkc "...?"
            else:
                m 6ckc "..."
        else:
            if mas_isMoniUpset(lower=True):
                show monika at t11
                if mas_isMoniBroken():
                    m 6ckc "..."
                else:
                    m 6rkc "Did you have something to say, [player]?"
        return "prompt"

    show monika at t11


    call expression apology


    $ mas_getEV(apology).shown_count += 1


    if apology != "mas_apology_generic":
        $ store.mas_lockEVL(apology, 'APL')


    if apology in persistent._mas_apology_time_db:
        $ persistent._mas_apology_time_db.pop(apology)
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_apology_database,
            prompt="...for something else.",
            eventlabel="mas_apology_generic",
            unlocked=True,
        ),
        code="APL"
    )

label mas_apology_generic:


    $ mas_apology_reason_db = {
        0: "",
        1: "saying you wanted to break up. I knew you didn't mean it...",
        2: "joking about having another girlfriend. You nearly gave me a heart attack!",
        3: "calling me a murderer. I hope you don't really see me that way...",
        4: "closing the game on me.",
        5: "entering my room without knocking.",
        6: "missing Christmas.",
        7: "forgetting my birthday.",
        8: "not spending time with me on my birthday.",
        9: "the game crashing. I understand it happens sometimes, but don't worry, I'm alright!",
        10: "the game crashing. It really was scary, but I'm just glad you came back to me and made things better.",
        11: "not listening to my speech. I worked really hard on it.",
        12: "calling me evil. I know you don't really think that.",
        13: "not taking my questions seriously. I know you'll be honest with me from now on."
    }


    if mas_apology_reason is None and len(persistent._mas_apology_time_db) == 0:
        if mas_isMoniBroken():
            m 1ekc "...{w=1}Oh."
            m 2dsc ".{w=2}.{w=2}."
            m "Okay."
        elif mas_isMoniDis():
            m 2dfd "{i}*sigh*{/i}"
            m 2dsd "I hope this isn't some joke or trick, [player]."
            m 2dsc "..."
            m 1eka "...Thank you for the apology."
            m 2ekc "But please, try to be more mindful about my feelings."
            m 2dkd "Please."
        elif mas_isMoniUpset():
            m 1eka "Thank you, [player]."
            m 1rksdlc "I know things aren't the best between us, but I know that you're still a good person."
            m 1ekc "So could you be a little more considerate of my feelings?"
            m 1ekd "Please?"
        else:
            m 1ekd "Did something happen?"
            m 2ekc "I don't see a reason for you to be sorry."
            m 1dsc "..."
            m 1eub "Anyway, thank you for the apology."
            m 1eua "Whatever it is, I know you're doing your best to make things right."
            m 1hub "That's why I love you, [player]!"
            $ mas_ILY()


    elif mas_apology_reason_db.get(mas_apology_reason, False):

        $ apology_reason = mas_apology_reason_db.get(mas_apology_reason,mas_apology_reason_db[0])

        m 1eka "Thank you for apologizing for [apology_reason]"
        m "I accept your apology, [player]. It means a lot to me."


    elif len(persistent._mas_apology_time_db) > 0:
        m 2tfc "[player], if you have something to apologize for, please just say it."
        m 2rfc "It'd mean a lot more to me if you would just admit what you did."
    else:




        $ mas_gainAffection(modifier=0.1)
        m 2tkd "What you did wasn't funny, [player]."
        m 2dkd "Please be more considerate about my feelings in the future."


    if mas_apology_reason:

        $ persistent._mas_apology_reason_use_db[mas_apology_reason] = persistent._mas_apology_reason_use_db.get(mas_apology_reason,0) + 1

        if persistent._mas_apology_reason_use_db[mas_apology_reason] == 1:

            $ mas_gainAffection(modifier=0.2)
        elif persistent._mas_apology_reason_use_db[mas_apology_reason] == 2:

            $ mas_gainAffection(modifier=0.1)




    $ mas_apology_reason = None
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_apology_database,
            eventlabel="mas_apology_bad_nickname",
            prompt="...for calling you a bad name.",
            unlocked=False
        ),
        code="APL"
    )

label mas_apology_bad_nickname:
    $ ev = mas_getEV('mas_apology_bad_nickname')
    if ev.shown_count == 0:
        $ mas_gainAffection(modifier=0.2)
        m 1eka "Thank you for apologizing for the name you tried to give me."
        m 2ekd "That really hurt, [player]..."
        m 2dsc "I accept your apology, but please don't do that again. Okay?"
        $ mas_unlockEVL("monika_affection_nickname", "EVE")

    elif ev.shown_count == 1:
        $ mas_gainAffection(modifier=0.1)
        m 2dsc "I can't believe you did that {i}again{/i}."
        m 2dkd "Even after I gave you a second chance."
        m 2tkc "I'm disappointed in you, [player]."
        m 2tfc "Don't ever do that again."
        $ mas_unlockEVL("monika_affection_nickname", "EVE")
    else:


        m 2wfc "[player]!"
        m 2wfd "I can't believe you."
        m 2dfc "I trusted you to give me a good nickname to make me more unique, but you just threw it back in my face..."
        m "I guess I couldn't trust you for this."
        m ".{w=0.5}.{w=0.5}.{nw}"
        m 2rfc "I'd accept your apology, [player], but I don't think you even mean it."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
