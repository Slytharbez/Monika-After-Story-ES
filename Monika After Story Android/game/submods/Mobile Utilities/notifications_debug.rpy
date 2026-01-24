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

    m 1hua "¡Okey, [player]!"
    m 2dsa "Solo dame un segundo para hacer una notificación.{w=0.5}.{w=0.5}.{w=0.5}{nw}"
    $ mas_android_display_notif("¡Te amo, [player]!")
    m 1hub "¡Ahí está!"

    return