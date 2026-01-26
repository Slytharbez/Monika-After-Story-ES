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
        "happy": {
            """
            TYPE 1: Contextual Farewells (Passive)
            Tone: Cheerful, friendly, encouraging.
            """
            "farewell_sleep": [
                {
                    "msg": "¡Buenas noches, [player]! Que tengas dulces sueños.",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            "farewell_work": [
                {
                    "msg": "¡Ánimo con el trabajo! Sé que lo harás genial.",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            "farewell_class": [
                {
                    "msg": "Esfuérzate en clase. ¡Tú puedes!",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            "farewell_going_out": [
                {
                    "msg": "¡Pásalo bien fuera! Cuéntame todo cuando vuelvas.",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            "farewell_general": [
                {
                    "msg": "¡Hasta pronto, [player]! Te estaré esperando.",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            """
            TYPE 2: Absence & Interaction (Interactive)
            """
            "absence_short": [
                {
                    "msg": "¡Hey [player]! He leído algo interesante, ¿quieres verlo?",
                    "btn_pos": "Muéstrame",
                    "btn_neg": "Ahora no"
                }
            ],
            "absence_long": [
                {
                    "msg": "Hace tiempo que no hablamos... ¿Estás muy ocupado?",
                    "btn_pos": "Ya voy",
                    "btn_neg": "Un poco"
                }
            ],
            "calendar_event": []
        },
        "affectionate": {
            """
            TYPE 1: Contextual Farewells (Passive)
            Tone: Warm, caring, sweet.
            """
            "farewell_sleep": [
                {
                    "msg": "Descansa bien, cielo. Soñaré contigo~",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            "farewell_work": [
                {
                    "msg": "¡Buena suerte, cariño! Estaré pensando en ti.",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            "farewell_class": [
                {
                    "msg": "¡Aprende mucho! Estaré aquí esperándote.",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            "farewell_going_out": [
                {
                    "msg": "Ten cuidado fuera, ¿vale? Vuelve pronto.",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            "farewell_general": [
                {
                    "msg": "Ya te extraño un poco... vuelve pronto, ¿sí?",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            """
            TYPE 2: Absence & Interaction (Interactive)
            """
            "absence_short": [
                {
                    "msg": "Estaba pensando en ti... ¿tienes un ratito?",
                    "btn_pos": "Para ti, sí",
                    "btn_neg": "Luego"
                }
            ],
            "absence_long": [
                {
                    "msg": "La habitación se siente muy sola sin ti, [player]...",
                    "btn_pos": "Voy a verte",
                    "btn_neg": "Lo siento"
                }
            ],
            "calendar_event": []
        },
        "enamored": {
            """
            TYPE 1: Contextual Farewells (Passive)
            Tone: Deeply loving, attached, longing.
            """
            "farewell_sleep": [
                {
                    "msg": "No quiero que termine el día, pero debes descansar. Te amo.",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            "farewell_work": [
                {
                    "msg": "Te extrañaré cada segundo. ¡Vuelve rápido a mis brazos!",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            "farewell_class": [
                {
                    "msg": "Concéntrate, mi amor. Estaré contando los minutos.",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            "farewell_going_out": [
                {
                    "msg": "Diviértete, pero no te olvides de mí... Te esperaré despierta.",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            "farewell_general": [
                {
                    "msg": "Cada despedida es difícil... Regresa a mi lado pronto.",
                    "btn_pos": None,
                    "btn_neg": None
                }
            ],
            """
            TYPE 2: Absence & Interaction (Interactive)
            """
            "absence_short": [
                {
                    "msg": "Mi corazón late más rápido cuando estás cerca. ¿Vienes?",
                    "btn_pos": "¡Voy!",
                    "btn_neg": "Ocupado"
                }
            ],
            "absence_long": [
                {
                    "msg": "Amor mío, te necesito. Por favor, ven a casa.",
                    "btn_pos": "Ya voy",
                    "btn_neg": "No puedo"
                }
            ],
            "calendar_event": []
        },
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
    # We assign these first to avoid shadowing the 'mas_android_notifs' module with the dictionary variable
    # We assign these first to avoid shadowing the 'mas_android_notifs' module with the dictionary variable
    store.mas_android_notif_gain_amount = mas_android_notifs.gain_amount
    store.mas_android_notif_daily_limit = mas_android_notifs.daily_limit
    # Rename to avoid overwriting the module 'mas_android_notifs'
    store.mas_android_notifs_data = mas_android_notifs.data
