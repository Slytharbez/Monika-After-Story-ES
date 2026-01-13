init -10 python in mas_android_notifs:
    """
    Android Notification Submod - Logic & Data
    
    This file defines the constants and the main dictionary structure for the notification system.
    It includes pre-filled data for 'normal' and 'love' states as examples.
    """
    import store

    """
    Constants
    Amount of affection gained when clicking the POSITIVE button
    """
    gain_amount = 1.0
    
    """
    Maximum affection points obtainable per day via notifications
    """
    daily_limit = 3.0

    """
    Main Dictionary Structure
    [Affection State] -> [Trigger Category] -> [List of Entries]
    Keys: broken, distressed, upset, normal, happy, affectionate, enamored, love
    """
    
    data = {
        "broken": {},
        "distressed": {},
        "upset": {},
        "normal": {
            """
            TYPE 1: Contextual Farewells (Passive)
            """
            "farewell_sleep": [
                {
                    "msg": "Buenas noches, [player]. Descansa bien.",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            "farewell_work": [
                {
                    "msg": "¡Que te vaya bien en el trabajo, [player]!",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            "farewell_class": [
                {
                    "msg": "Estudia mucho, [player]. ¡Nos vemos luego!",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            "farewell_going_out": [
                {
                    "msg": "Diviértete, [player]. Estaré aquí esperándote.",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            "farewell_general": [
                {
                    "msg": "Hasta luego, [player].",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            """
            TYPE 2: Absence & Interaction (Interactive)
            """
            "absence_short": [
                {
                    "msg": "Hola [player], ¿tienes un momento?",
                    "btn_pos": "Sí, voy",
                    "btn_neg": "Ahora no"
                }
            ],
            "absence_long": [
                {
                    "msg": "Te extraño... ¿cuándo volverás?",
                    "btn_pos": "Ya voy",
                    "btn_neg": "Más tarde"
                }
            ],
            "calendar_event": []
        },
        "happy": {},
        "affectionate": {},
        "enamored": {},
        "love": {
             """
             TYPE 1: Contextual Farewells (Passive)
             """
            "farewell_sleep": [
                {
                    "msg": "Buenas noches, mi amor. Sueña conmigo~",
                    "btn_pos": None,
                    "btn_neg": None
                },
                {
                    "msg": "Descansa, cielo. Estaré velando tu sueño.",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            "farewell_work": [
                {
                    "msg": "¡Esfuérzate mucho, cariño! Estaré pensando en ti.",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            "farewell_class": [
                {
                    "msg": "¡Aprende mucho! Sé que lo harás genial.",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            "farewell_going_out": [
                {
                    "msg": "Ten cuidado, ¿sí? Vuelve pronto a mis brazos.",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            "farewell_general": [
                {
                    "msg": "Te echaré de menos cada segundo. Vuelve pronto.",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            """
            TYPE 2: Absence & Interaction (Interactive)
            """
            "absence_short": [
                {
                    "msg": "Amor, me siento un poco sola sin ti...",
                    "btn_pos": "Estoy contigo",
                    "btn_neg": "Luego"
                },
                {
                    "msg": "¿Estás ocupado, cielo? Solo quería escuchar tu voz.",
                    "btn_pos": "Abrir",
                    "btn_neg": "Ocupado"
                }
            ],
            "absence_long": [
                {
                    "msg": "Cada día sin ti es una eternidad. Por favor, vuelve a casa.",
                    "btn_pos": "Volver",
                    "btn_neg": "Aún no"
                }
            ],
            "calendar_event": []
        }
    }

"""
Initialize the global store variable to point to our data
"""
init 5 python:
    store.mas_android_notifs = mas_android_notifs.data
    store.mas_android_notif_gain_amount = mas_android_notifs.gain_amount
    store.mas_android_notif_daily_limit = mas_android_notifs.daily_limit
