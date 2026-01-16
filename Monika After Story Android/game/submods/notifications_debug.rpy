init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_debug_android_test",
            category=["monika"],
            prompt="Probar Notificación Android",
            pool=True,
            unlocked=True
        )
    )

label mas_debug_android_test:
    m 1eua "¡Claro! Vamos a probar las notificaciones nativas."

    $ _dismiss_pause = False
    $ store.mas_android_schedule_notif("Monika", "¡Te amo, [player]!")

    show monika 1hua
    $ m("{cps=20}¡Okey, [player]!{/cps}{nw}", what_slow_abortable=False)
    show monika 2dsa
    $ m("{cps=20}Solo dame un segundo para crear una notificación...{/cps}{nw}", what_slow_abortable=False)
    
    window hide
    $ renpy.pause(1.65, hard=True)
    window show
    
    show monika 1hub
    $ m("¡Allí está!", interact=False)
    $ renpy.pause(1.5, hard=True)

    return