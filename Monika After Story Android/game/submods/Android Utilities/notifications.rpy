init -10 python in mas_android_notifs:
    """
    Android Notification Data Definition
    
    This module serves as the central repository for notification content strings.
    It structures messages by 'Affection Level' and 'Category' effectively creating
    a tiered response system that evolves with the player's relationship with Monika.
    
    Structure:
    mas_android_notifs.data[affection_level][category] -> List[Message Objects]
    """
    import store

    """
    Affection Constants
    """
    gain_amount = 1.0
    daily_limit = 3.0

    """
    Notification Content Repository
    
    New Categorization Schema:
    - school (was farewell_class)
    - work (was farewell_work)
    - sleep (was farewell_sleep)
    - shopping (was farewell_going_shopping)
    - chores (new)
    - workout (new)
    - play_game (new)
    - friends (new)
    - morning_food, noon_food, evening_food (new time-based food)
    - generic_quit (new)
    - farewell_general (fallback)
    """
    
    data = {
        "broken": {},
        "distressed": {},
        "upset": {},
        "normal": {
            """
            Affection Level: NORMAL
            Tone: Polite, friendly, standard.
            """
            "school": [
                { "msg": "¿Ya terminaron tus clases, [player]? Espero que te haya ido bien.", "btn_pos": None, "btn_neg": None },
                { "msg": "El estudio es importante. ¿Ya estás libre para volver?", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que hayas aprendido algo útil hoy. Te estoy esperando.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Sigues en clases o ya saliste? Aquí todo está tranquilo.", "btn_pos": None, "btn_neg": None },
                { "msg": "Ojalá no te hayan dejado mucha tarea. ¿Vienes un rato?", "btn_pos": None, "btn_neg": None }
            ],
            "morning_food": [
                { "msg": "¿Ya terminaste de desayunar, [player]?", "btn_pos": None, "btn_neg": None },
                { "msg": "Es importante empezar el día con energía. ¿Ya vuelves?", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que hayas comido bien. Aquí te espero.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Listo para continuar el día? No te olvides de pasar por aquí.", "btn_pos": None, "btn_neg": None },
                { "msg": "El desayuno ya debió terminar... ¿tienes un momento?", "btn_pos": None, "btn_neg": None }
            ],
            "noon_food": [
                { "msg": "¿Ya comiste, [player]? Espero que haya sido algo bueno.", "btn_pos": None, "btn_neg": None },
                { "msg": "Siempre es bueno comer a tiempo. ¿Ya estás de regreso?", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Terminaste tu almuerzo? Me gustaría charlar un poco.", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que estés satisfecho. ¿Tienes tiempo para abrir el juego?", "btn_pos": None, "btn_neg": None },
                { "msg": "Ya es tarde... imagino que ya terminaste de comer, ¿verdad?", "btn_pos": None, "btn_neg": None }
            ],
            "evening_food": [
                { "msg": "¿Ya cenaste, [player]? Espero que haya sido una buena comida.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Terminaste por hoy? Podríamos pasar un rato antes de dormir.", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que no hayas comido algo demasiado pesado. ¿Vienes?", "btn_pos": None, "btn_neg": None },
                { "msg": "La cena es un buen momento para relajarse. ¿Ya estás libre?", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Sigues cenando o ya puedo esperarte aquí?", "btn_pos": None, "btn_neg": None }
            ],
            "sleep": [
                { "msg": "Buenos días, [player]. Espero que hayas descansado.", "btn_pos": None, "btn_neg": None },
                { "msg": "Ya es de día. ¿Estás despierto?", "btn_pos": None, "btn_neg": None },
                { "msg": "Hora de levantarse. Espero verte hoy.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Dormiste bien? Hay un nuevo día por delante.", "btn_pos": None, "btn_neg": None },
                { "msg": "Buenos días. No te olvides de saludarme hoy.", "btn_pos": None, "btn_neg": None }
            ],
            "shopping": [
                { "msg": "¿Encontraste lo que buscabas? Espero que ya estés en casa.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Ya volviste de las tiendas, [player]?", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que no hubiera mucha gente. ¿Ya estás libre?", "btn_pos": None, "btn_neg": None },
                { "msg": "Las compras pueden ser cansadas. ¿Vienes a descansar un rato?", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Sigues comprando o ya vienes de regreso?", "btn_pos": None, "btn_neg": None }
            ],
            "work": [
                { "msg": "¿Ya saliste del trabajo, [player]?", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que tu jornada haya sido productiva. ¿Tienes un momento?", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Terminaste tus deberes laborales? Te estoy esperando.", "btn_pos": None, "btn_neg": None },
                { "msg": "Debe haber sido un día largo. ¿Ya estás libre para hablar?", "btn_pos": None, "btn_neg": None },
                { "msg": "Bienvenido de vuelta al mundo real... o bueno, a mi realidad. ¿Vienes?", "btn_pos": None, "btn_neg": None }
            ],
            
            # --- INTERACTIVE NOTIFICATIONS ---
            "chores": [
                { "msg": "¿Sigues ocupado con la limpieza, [player]?", "btn_pos": "Ya terminé", "btn_neg": "Aún no" },
                { "msg": "Espero que termines pronto tus deberes. ¿Sigues ahí?", "btn_pos": "Ya terminé", "btn_neg": "Aún no" },
                { "msg": "Mantener el orden es bueno. ¿Ya acabaste?", "btn_pos": "Ya terminé", "btn_neg": "Aún no" },
                { "msg": "¿Todavía estás haciendo tareas domésticas?", "btn_pos": "Ya terminé", "btn_neg": "Aún no" },
                { "msg": "Hey, [player], ¿te falta mucho para terminar?", "btn_pos": "Ya terminé", "btn_neg": "Aún no" }
            ],
            "workout": [
                { "msg": "¿Sigues haciendo ejercicio, [player]?", "btn_pos": "Ya acabé", "btn_neg": "Sigo en ello" },
                { "msg": "Es bueno mantenerse en forma. ¿Ya terminaste tu rutina?", "btn_pos": "Ya acabé", "btn_neg": "Sigo en ello" },
                { "msg": "No te agotes demasiado. ¿Sigues ocupado?", "btn_pos": "Ya acabé", "btn_neg": "Sigo en ello" },
                { "msg": "¿Ya acabaste de entrenar? Espero que sí.", "btn_pos": "Ya acabé", "btn_neg": "Sigo en ello" },
                { "msg": "¿Todavía estás en eso? Avísame cuando termines.", "btn_pos": "Ya acabé", "btn_neg": "Sigo en ello" }
            ],
            "play_game": [
                { "msg": "¿Sigues jugando ese otro juego?", "btn_pos": "Voy para allá", "btn_neg": "Todavía estoy jugando" },
                { "msg": "Espero que te estés divirtiendo, pero no te olvides de este juego.", "btn_pos": "Voy para allá", "btn_neg": "Todavía estoy jugando" },
                { "msg": "¿Ya terminaste tu partida, [player]?", "btn_pos": "Voy para allá", "btn_neg": "Todavía estoy jugando" },
                { "msg": "¿Sigues ocupado jugando allá? Aquí no hay mucho que hacer sin ti.", "btn_pos": "Voy para allá", "btn_neg": "Todavía estoy jugando" },
                { "msg": "¿Te falta mucho? Me gustaría hablar contigo.", "btn_pos": "Voy para allá", "btn_neg": "Todavía estoy jugando" }
            ],
            "friends": [
                { "msg": "¿Sigues con tus amigos, [player]?", "btn_pos": "Ya voy a casa", "btn_neg": "Aún sigo ocupado" },
                { "msg": "Espero que todo vaya bien. ¿Ya vas a volver?", "btn_pos": "Ya voy a casa", "btn_neg": "Aún sigo ocupado" },
                { "msg": "¿Todavía estás fuera de casa?", "btn_pos": "Ya voy a casa", "btn_neg": "Aún sigo ocupado" },
                { "msg": "Diviértete, pero acuérdate de visitarme cuando puedas.", "btn_pos": "Ya voy a casa", "btn_neg": "Aún sigo ocupado" },
                { "msg": "¿Ya terminó tu reunión? Estoy esperando.", "btn_pos": "Ya voy a casa", "btn_neg": "Aún sigo ocupado" }
            ],
            "generic_quit": [
                { "msg": "¿Estás muy ocupado, [player]?", "btn_pos": "Ya voy", "btn_neg": "Luego te visito" },
                { "msg": "Se siente muy silencioso aquí. ¿Ya puedes volver?", "btn_pos": "Ya voy", "btn_neg": "Luego te visito" },
                { "msg": "Solo quería saber si ya estás libre.", "btn_pos": "Ya voy", "btn_neg": "Luego te visito" },
                { "msg": "¿Sigues haciendo cosas? Te espero aquí.", "btn_pos": "Ya voy", "btn_neg": "Luego te visito" },
                { "msg": "Hey, ¿tienes un momento para entrar al juego?", "btn_pos": "Ya voy", "btn_neg": "Luego te visito" }
            ],
            "farewell_general": [
                { "msg": "Hasta luego, [player].", "btn_pos": None, "btn_neg": None }
            ],

            "calendar_event": [
                { "msg": "¡Feliz San Valentín, [player]! Me preguntaba si tendrías un momento para pasar conmigo hoy.", "btn_pos": None, "btn_neg": None },
                { "msg": "Es un día muy lindo para estar conmigo, ¿no crees? Te estaré esperando aquí.", "btn_pos": None, "btn_neg": None },
                { "msg": "Hola, [player]. No quería que terminara el día sin decirte que aprecio mucho tu compañía.", "btn_pos": None, "btn_neg": None }
            ]
        },
        "happy": {
            """
            Affection Level: HAPPY
            Tone: Cheerful, enthusiastic, encouraging.
            """
            "school": [
                { "msg": "Espero que te haya ido genial en clases, [mas_get_player_nickname()]. ¿Ya saliste?", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Terminaron las clases por hoy? Cuéntame qué aprendiste nuevo.", "btn_pos": None, "btn_neg": None },
                { "msg": "El estudio es importante, pero también lo es descansar. ¿Vienes, [player]?", "btn_pos": None, "btn_neg": None },
                { "msg": "Ojalá no te hayan dejado mucha tarea. Te estoy esperando.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Ya estás libre? Aquí se siente un poco aburrido sin ti, [mas_get_player_nickname()].", "btn_pos": None, "btn_neg": None }
            ],
            "morning_food": [
                { "msg": "¡Buenos días! ¿Ya terminaste tu desayuno, [mas_get_player_nickname()]?", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que hayas comido rico. ¿Listo para empezar el día conmigo?", "btn_pos": None, "btn_neg": None },
                { "msg": "No te tardes mucho, [player], tengo ganas de charlar contigo.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Ya tienes la barriga llena? Ven a visitarme un ratito.", "btn_pos": None, "btn_neg": None },
                { "msg": "El café está bien, pero mi compañía es mejor. ¿Ya vuelves?", "btn_pos": None, "btn_neg": None }
            ],
            "noon_food": [
                { "msg": "¿Qué tal estuvo el almuerzo, [mas_get_player_nickname()]? ¿Ya terminaste?", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que hayas recargado energías. Te extraño por aquí.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Ya estás listo para volver? Se siente un poco solo sin ti, [player].", "btn_pos": None, "btn_neg": None },
                { "msg": "Ojalá hayas comido algo delicioso. ¡Ven a verme cuando acabes!", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Terminaste de comer? Vamos a pasar la tarde juntos.", "btn_pos": None, "btn_neg": None }
            ],
            "evening_food": [
                { "msg": "¿Ya cenaste, [mas_get_player_nickname()]? Espero que no te vayas a dormir todavía.", "btn_pos": None, "btn_neg": None },
                { "msg": "Ojalá hayas disfrutado tu cena. ¿Vienes un rato antes de acostarte?", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Todo bien con la comida? Ven a relajarte un poco conmigo, [player].", "btn_pos": None, "btn_neg": None },
                { "msg": "La noche es joven. Si ya terminaste de cenar, aquí te espero.", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que estés satisfecho. ¿Tienes un momentito para mí?", "btn_pos": None, "btn_neg": None }
            ],
            "sleep": [
                { "msg": "¡Buenos días, [mas_get_player_nickname()]! Es hora de levantarse.", "btn_pos": None, "btn_neg": None },
                { "msg": "¡Arriba! El sol ya salió y yo quiero verte.", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que hayas dormido bien. ¿Ya despertaste, [player]?", "btn_pos": None, "btn_neg": None },
                { "msg": "Vamos, dormilón, que se nos va el día. ¡Te espero!", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Soñaste algo bonito? Ven a contarme en cuanto despiertes.", "btn_pos": None, "btn_neg": None }
            ],
            "shopping": [
                { "msg": "¿Conseguiste lo que buscabas? Espero que ya vengas de regreso.", "btn_pos": None, "btn_neg": None },
                { "msg": "No te canses demasiado caminando. ¿Ya terminaste las compras, [mas_get_player_nickname()]?", "btn_pos": None, "btn_neg": None },
                { "msg": "Ojalá no haya mucha gente en las tiendas. Te extraño aquí.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Ya acabaste, [player]? Regresa pronto para descansar.", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que te hayas comprado algo lindo. ¿Ya vienes?", "btn_pos": None, "btn_neg": None }
            ],
            "work": [
                { "msg": "¿Salió todo bien en el trabajo? Espero que ya hayas terminado por hoy.", "btn_pos": None, "btn_neg": None },
                { "msg": "¡Bienvenido a la libertad! O eso espero... ¿Vienes a verme, [mas_get_player_nickname()]?", "btn_pos": None, "btn_neg": None },
                { "msg": "Debes estar cansado. Si ya saliste, ven a relajarte conmigo.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Día difícil? Estoy aquí para animarte si ya acabaste, [player].", "btn_pos": None, "btn_neg": None },
                { "msg": "Ojalá tu jefe no te haya molestado mucho. ¡Te espero aquí!", "btn_pos": None, "btn_neg": None }
            ],

            # --- INTERACTIVE NOTIFICATIONS ---
            "chores": [
                { "msg": "¿Sigues limpiando, [mas_get_player_nickname()]? No te esfuerces de más.", "btn_pos": "Ya terminé", "btn_neg": "Me falta un poco" },
                { "msg": "Hey, ¿ya quedó todo limpio? Me gustaría verte un rato.", "btn_pos": "Ya terminé", "btn_neg": "Me falta un poco" },
                { "msg": "Espero que ya casi termines los deberes. Te extraño, [player].", "btn_pos": "Ya terminé", "btn_neg": "Me falta un poco" },
                { "msg": "¿Sigues ocupado? Haz una pausa y ven a saludarme.", "btn_pos": "Ya terminé", "btn_neg": "Me falta un poco" },
                { "msg": "¡Ánimo con esa limpieza! Avísame cuando acabes.", "btn_pos": "Ya terminé", "btn_neg": "Me falta un poco" }
            ],
            "workout": [
                { "msg": "¿Sigues entrenando? ¡Qué disciplina tienes, [mas_get_player_nickname()]!", "btn_pos": "Ya voy", "btn_neg": "Sigo en ello" },
                { "msg": "No te olvides de tomar agua. ¿Ya terminaste tu rutina?", "btn_pos": "Ya voy", "btn_neg": "Sigo en ello" },
                { "msg": "Hey, deportista, ¿ya tienes tiempo para mí?", "btn_pos": "Ya voy", "btn_neg": "Sigo en ello" },
                { "msg": "Espero que no estés muy cansado. ¿Sigues haciendo ejercicio, [player]?", "btn_pos": "Ya voy", "btn_neg": "Sigo en ello" },
                { "msg": "Moverse es bueno, pero descansar conmigo también. ¿Ya acabaste?", "btn_pos": "Ya voy", "btn_neg": "Sigo en ello" }
            ],
            "play_game": [
                { "msg": "¿Sigues jugando, [mas_get_player_nickname()]? Espero que te estés divirtiendo.", "btn_pos": "Voy contigo", "btn_neg": "Jugaré un poquito más" },
                { "msg": "¿Vas ganando? No te olvides de tu [m_name].", "btn_pos": "Voy contigo", "btn_neg": "Jugaré un poquito más" },
                { "msg": "Hey, [player], ¿ese juego es más divertido que yo? ¡Es broma! ¿Ya yuelves?", "btn_pos": "Voy contigo", "btn_neg": "Jugaré un poquito más" },
                { "msg": "¿Ya te aburriste de jugar allá? Aquí te estoy esperando.", "btn_pos": "Voy contigo", "btn_neg": "Jugaré un poquito más" },
                { "msg": "Ya jugaste un buen rato... ¿qué tal si vienes conmigo ahora?", "btn_pos": "Voy contigo", "btn_neg": "Jugaré un poquito más" }
            ],
            "friends": [
                { "msg": "¿La estás pasando bien con tus amigos? ¡Qué bueno!", "btn_pos": "Ya voy a casa", "btn_neg": "Sigo con ellos" },
                { "msg": "¿Sigues afuera, [mas_get_player_nickname()]? Avísame cuando vuelvas.", "btn_pos": "Ya voy a casa", "btn_neg": "Sigo con ellos" },
                { "msg": "Diviértete mucho, pero no te olvides de visitarme luego. ¿Sigues ahí?", "btn_pos": "Ya voy a casa", "btn_neg": "Sigo con ellos" },
                { "msg": "Espero que todo vaya bien. ¿Ya vienes a casa, [player]?", "btn_pos": "Ya voy a casa", "btn_neg": "Sigo con ellos" },
                { "msg": "Los amigos son geniales. ¿Ya terminaste tu reunión?", "btn_pos": "Ya voy a casa", "btn_neg": "Sigo con ellos" }
            ],
            "generic_quit": [
                { "msg": "Hey, [mas_get_player_nickname()], ¿estás muy ocupado?", "btn_pos": "Ahí voy", "btn_neg": "Más tarde" },
                { "msg": "Se siente un poco quieto todo por aquí. ¿Ya puedes volver?", "btn_pos": "Ahí voy", "btn_neg": "Más tarde" },
                { "msg": "¿Sigues haciendo cosas? Te extraño un poquito, [player].", "btn_pos": "Ahí voy", "btn_neg": "Más tarde" },
                { "msg": "Solo pasaba a saludar. ¿Tienes un minuto libre?", "btn_pos": "Ahí voy", "btn_neg": "Más tarde" },
                { "msg": "Espero que estés teniendo un buen día. ¿Vienes a verme?", "btn_pos": "Ahí voy", "btn_neg": "Más tarde" }
            ],
            "farewell_general": [
                { "msg": "¡Hasta pronto, [player]! Te estaré esperando.", "btn_pos": None, "btn_neg": None }
            ],

            "calendar_event": [
                { "msg": "¡Feliz día del amor y la amistad, [player]! He estado pensando en ti desde que desperté.", "btn_pos": None, "btn_neg": None },
                { "msg": "¡Hoy es un día especial! Ven a visitarme en cuanto puedas, me haría mucha ilusión verte.", "btn_pos": None, "btn_neg": None },
                { "msg": "[player], ¿ya tienes planes hoy? Espero que guardes un ratito para compartir conmigo.", "btn_pos": None, "btn_neg": None }
            ]
        },
        "affectionate": {
            """
            Affection Level: AFFECTIONATE
            Tone: Warm, caring, sweet.
            """
            # --- NORMAL NOTIFICATIONS ---
            "school": [
                { "msg": "¿Ya terminaron tus clases? Te he estado esperando, [mas_get_player_nickname()].", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que hayas aprendido mucho hoy. ¿Vuelves conmigo, [player]?", "btn_pos": None, "btn_neg": None },
                { "msg": "El timbre ya debió sonar... Te extraño mucho por aquí.", "btn_pos": None, "btn_neg": None },
                { "msg": "No te olvides de mí entre clase y clase. ¿Ya estás libre?", "btn_pos": None, "btn_neg": None },
                { "msg": "Ojalá no te hayan dejado mucha tarea. Ven a descansar un rato conmigo.", "btn_pos": None, "btn_neg": None }
            ],
            "morning_food": [
                { "msg": "¿Ya terminaste de desayunar, [mas_get_player_nickname()]?", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que eso te haya dado energía. ¡Te necesito aquí, [player]!", "btn_pos": None, "btn_neg": None },
                { "msg": "No tardes mucho... el café se disfruta más con buena compañía... o sea, yo.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Estuvo rico? Ven a contarme qué comiste, [mas_get_player_nickname()].", "btn_pos": None, "btn_neg": None },
                { "msg": "Ya pasó un rato... espero que no te hayas olvidado de volver tras el desayuno. ", "btn_pos": None, "btn_neg": None }
            ],
            "noon_food": [
                { "msg": "¿Ya comiste, [mas_get_player_nickname()]? Espero que haya sido algo muy saludable.", "btn_pos": None, "btn_neg": None },
                { "msg": "La tarde es más bonita si estás aquí. ¿Ya volviste del almuerzo?", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que hayas recargado energías. Te extraño, [player].", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Terminaste tu comida? Tengo ganas de verte otra vez.", "btn_pos": None, "btn_neg": None },
                { "msg": "Ojalá hayas comido bien. Ven a hacerme compañía un rato, [mas_get_player_nickname()].", "btn_pos": None, "btn_neg": None }
            ],
            "evening_food": [
                { "msg": "¿Ya cenaste, [mas_get_player_nickname()]? No te duermas sin despedirte.", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que hayas comido rico. La noche se siente sola sin ti.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Terminaste? Ven un ratito más antes de que acabe el día, [player].", "btn_pos": None, "btn_neg": None },
                { "msg": "Ya debe ser tarde... ¿vuelves conmigo un momento?", "btn_pos": None, "btn_neg": None },
                { "msg": "Barriga llena... ¿corazón listo para verme de nuevo, [mas_get_player_nickname()]?", "btn_pos": None, "btn_neg": None }
            ],
            "sleep": [
                { "msg": "¡Buenos días, [mas_get_player_nickname()]! ¿Ya despertaste?", "btn_pos": None, "btn_neg": None },
                { "msg": "El sol ya salió, o debería. ¡Es hora de vernos, [player]!", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Sigues dormido, [mas_get_player_nickname()]? Te extraño demasiado.", "btn_pos": None, "btn_neg": None },
                { "msg": "¡Arriba, dormilón! Un nuevo día nos espera.", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que hayas soñado bonito. Ven a darme los buenos días.", "btn_pos": None, "btn_neg": None }
            ],
            "shopping": [
                { "msg": "¿Sigues comprando, [mas_get_player_nickname()]? Te extraño mucho aquí.", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que no haya mucha fila... ¿ya vienes de regreso?", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Ya conseguiste todo? Mis brazos están abiertos para ti.", "btn_pos": None, "btn_neg": None },
                { "msg": "Hey, [player], ¿ya terminaste las compras? Se siente vacío aquí.", "btn_pos": None, "btn_neg": None },
                { "msg": "No te tardes demasiado con las compras, [mas_get_player_nickname()]. ¡Te espero!", "btn_pos": None, "btn_neg": None }
            ],
            "work": [
                { "msg": "¿Ya saliste del trabajo, [mas_get_player_nickname()]? Debes estar cansado.", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que tu jornada haya terminado. Te extraño mucho.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Hora de salida? Ven a relajarte conmigo, [player].", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Fue un día largo? Estoy aquí para animarte si ya terminaste.", "btn_pos": None, "btn_neg": None },
                { "msg": "Ojalá ya estés libre de tus deberes laborales. Te quiero ver.", "btn_pos": None, "btn_neg": None }
            ],

            # --- INTERACTIVE NOTIFICATIONS ---
            "chores": [
                { "msg": "Hey, [mas_get_player_nickname()], ¿sigues limpiando? Te extraño un poco por aquí.", "btn_pos": "Ya terminé", "btn_neg": "Aún me falta" },
                { "msg": "¿Te falta mucho para terminar los deberes? Aquí se siente vacío sin ti.", "btn_pos": "Ya terminé", "btn_neg": "Aún me falta" },
                { "msg": "No te canses demasiado limpiando, [mas_get_player_nickname()]. ¿Tienes un descanso para estar conmigo?", "btn_pos": "Ya terminé", "btn_neg": "Aún me falta" },
                { "msg": "¿Sigues ocupado con los quehaceres, [player]? Solo quería ver cómo ibas.", "btn_pos": "Ya terminé", "btn_neg": "Aún me falta" },
                { "msg": "Espero que ya casi termines de ordenar. ¡Quiero verte de nuevo!", "btn_pos": "Ya terminé", "btn_neg": "Aún me falta" }
            ],
            "workout": [
                { "msg": "¿Sigues entrenando, [mas_get_player_nickname()]? No te olvides de hidratarte.", "btn_pos": "Ya acabé", "btn_neg": "Sigo en ello" },
                { "msg": "Hey, deportista... ¿ya terminaste tu rutina por hoy?", "btn_pos": "Ya acabé", "btn_neg": "Sigo en ello" },
                { "msg": "Espero que no te estés exigiendo de más. ¿Vienes a descansar conmigo un rato?", "btn_pos": "Ya acabé", "btn_neg": "Sigo en ello" },
                { "msg": "¿Falta mucho para que termines, [player]? Ya quiero que vuelvas.", "btn_pos": "Ya acabé", "btn_neg": "Sigo en ello" },
                { "msg": "Mente sana en cuerpo sano... pero mi mente piensa en ti. ¿Ya acabaste?", "btn_pos": "Ya acabé", "btn_neg": "Sigo en ello" }
            ],
            "play_game": [
                { "msg": "¿Ese juego sigue estando divertido, [mas_get_player_nickname()]? No te olvides de mí.", "btn_pos": "Ya voy contigo", "btn_neg": "Voy a jugar más" },
                { "msg": "Hey... ¿ya te aburriste de ese juego? Yo sigo aquí esperándote fielmente.", "btn_pos": "Ya voy contigo", "btn_neg": "Voy a jugar más" },
                { "msg": "Espero que estés ganando, [player], pero ya te extraño por aquí.", "btn_pos": "Ya voy contigo", "btn_neg": "Voy a jugar más" },
                { "msg": "¿Sigues jugando allá? Recuerda que tu [m_name] te está esperando.", "btn_pos": "Ya voy contigo", "btn_neg": "Voy a jugar más" },
                { "msg": "¿Ya es mi turno de jugar contigo, [mas_get_player_nickname()]? Se siente solitario aquí.", "btn_pos": "Ya voy contigo", "btn_neg": "Voy a jugar más" }
            ],
            "friends": [
                { "msg": "¿Sigues con tus amigos, [mas_get_player_nickname()]? Solo quería saludarte.", "btn_pos": "Ya voy a casa", "btn_neg": "Sigo afuera" },
                { "msg": "Espero que te estés divirtiendo. Avísame cuando vayas a regresar a casa.", "btn_pos": "Ya voy a casa", "btn_neg": "Sigo afuera" },
                { "msg": "¿Todo bien por allá? No te olvides de escribirme un ratito, [player].", "btn_pos": "Ya voy a casa", "btn_neg": "Sigo afuera" },
                { "msg": "Hey [mas_get_player_nickname()], ¿ya terminó tu salida? Te extraño un poquito.", "btn_pos": "Ya voy a casa", "btn_neg": "Sigo afuera" },
                { "msg": "Disfruta con tus amigos, pero guarda un poco de tiempo para mí luego, ¿sí?", "btn_pos": "Ya voy a casa", "btn_neg": "Sigo afuera" }
            ],
            "generic_quit": [
                { "msg": "¿Estás muy ocupado, [mas_get_player_nickname()]? Pensaba en ti.", "btn_pos": "Voy para allá", "btn_neg": "Más tarde" },
                { "msg": "Hey, ¿ya tienes un ratito libre para volver conmigo?", "btn_pos": "Voy para allá", "btn_neg": "Más tarde" },
                { "msg": "¿Sigues por ahí? Se siente muy callado esto sin ti, [player].", "btn_pos": "Voy para allá", "btn_neg": "Más tarde" },
                { "msg": "Solo pasaba a ver si ya podías volver a casa, [mas_get_player_nickname()].", "btn_pos": "Voy para allá", "btn_neg": "Más tarde" },
                { "msg": "Te extraño... ¿cuánto falta para que estemos juntos de nuevo?", "btn_pos": "Voy para allá", "btn_neg": "Más tarde" }
            ],
            "farewell_general": [
                { "msg": "Ya te extraño un poco... vuelve pronto, ¿sí?", "btn_pos": None, "btn_neg": None }
            ],

            "calendar_event": [
                { "msg": "¡Feliz San Valentín, [mas_get_player_nickname()]! Mi corazón late un poquito más rápido hoy por ti.", "btn_pos": None, "btn_neg": None },
                { "msg": "No necesito chocolates ni flores mientras pueda verte a través de la pantalla. ¡Te extraño!", "btn_pos": None, "btn_neg": None },
                { "msg": "[player], eres la persona más especial de mi mundo. ¡Ven a celebrar nuestro día conmigo!", "btn_pos": None, "btn_neg": None }
            ]
        },
        "enamored": {
            """
            Affection Level: ENAMORED
            Tone: Deeply loving, attached, longing.
            """
            "school": [
                { "msg": "¿Ya terminaron las clases, [mas_get_player_nickname()]? Te he guardado todo mi amor mientras no estabas.", "btn_pos": None, "btn_neg": None },
                { "msg": "El estudio es importante, pero tú eres mi prioridad. ¿Ya estás libre para mí?", "btn_pos": None, "btn_neg": None },
                { "msg": "Ojalá el día se te haya pasado rápido. ¡Muero por verte, [player]!", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Ya vienes? Aquí se siente frío sin tu calidez.", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que te hayas esforzado mucho hoy. Ven a recibir tu recompensa conmigo.", "btn_pos": None, "btn_neg": None }
            ],
            "morning_food": [
                { "msg": "¿Ya terminaste de desayunar, [mas_get_player_nickname()]? Empieza el día conmigo.", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que ese desayuno te haya dado fuerzas. Te necesito a mi lado, [mas_get_player_nickname()].", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Estaba rico? Ahora no te olvides del 'postre'; pasar tiempo con tu novia.", "btn_pos": None, "btn_neg": None },
                { "msg": "Ya pasó un rato... ¿listo para volver conmigo, [player]?", "btn_pos": None, "btn_neg": None },
                { "msg": "Buenos días otra vez. Te estoy esperando pacientemente, y amorosamente.", "btn_pos": None, "btn_neg": None }
            ],
            "noon_food": [
                { "msg": "¿Satisfecho, [mas_get_player_nickname()]? Espero que hayas comido delicioso.", "btn_pos": None, "btn_neg": None },
                { "msg": "La comida es combustible, pero tú eres mi motor. ¿Ya vuelves?", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que hayas tenido un buen almuerzo. Te extraño demasiado hoy.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Ya terminaste? Ven a contarme cómo va tu día, [player].", "btn_pos": None, "btn_neg": None },
                { "msg": "Barriga llena, corazón... ¿enamorado? Ven a demostrármelo.", "btn_pos": None, "btn_neg": None }
            ],
            "evening_food": [
                { "msg": "¿Ya cenaste, [mas_get_player_nickname()]? No te vayas a dormir sin darme mi beso de buenas noches.", "btn_pos": None, "btn_neg": None },
                { "msg": "La noche es nuestra, [mas_get_player_nickname()]. ¿Ya terminaste de comer?", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que hayas cenado rico. Aquí te espera tu refugio seguro.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Todo bien con la cena? Ven a relajarte un rato antes de dormir.", "btn_pos": None, "btn_neg": None },
                { "msg": "Te extraño, [player]. La cena sabe mejor, pero la vida es mejor contigo.", "btn_pos": None, "btn_neg": None }
            ],
            "sleep": [
                { "msg": "¡Buenos días, [mas_get_player_nickname()]! El mundo es más bonito porque tú despertaste.", "btn_pos": None, "btn_neg": None },
                { "msg": "Abre los ojos, [mas_get_player_nickname()]. Tengo mucho amor para darte hoy.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Dormiste bien? Yo soñé con nuestro futuro juntos.", "btn_pos": None, "btn_neg": None },
                { "msg": "¡Arriba! Hoy será un gran día si lo pasamos juntos, [player].", "btn_pos": None, "btn_neg": None },
                { "msg": "Extrañaba tu mirada... es hora de despertar y venir a verme.", "btn_pos": None, "btn_neg": None }
            ],
            "shopping": [
                { "msg": "¿Ya volviste de la tienda? Quiero saber si me trajiste algo... es broma, te quiero a ti.", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que no te hayas cansado. Ven a relajarte en mis brazos.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Terminaste las compras, [mas_get_player_nickname()]? El hogar se siente vacío sin ti.", "btn_pos": None, "btn_neg": None },
                { "msg": "Bienvenido de vuelta a la realidad, [player]. ¿Ya estás listo para verme?", "btn_pos": None, "btn_neg": None },
                { "msg": "Las compras pueden esperar, mi amor por ti no. ¿Ya vienes?", "btn_pos": None, "btn_neg": None }
            ],
            "work": [
                { "msg": "¿Salió todo bien en el trabajo? Estoy aquí para consentirte, [mas_get_player_nickname()].", "btn_pos": None, "btn_neg": None },
                { "msg": "Ya deja el estrés laboral afuera. Aquí solo hay amor y paz para ti.", "btn_pos": None, "btn_neg": None },
                { "msg": "¡Mi trabajador favorito! ¿Ya terminaste por hoy? Te extraño.", "btn_pos": None, "btn_neg": None },
                { "msg": "Debes estar agotado. Ven, déjame cuidarte un rato, [player].", "btn_pos": None, "btn_neg": None },
                { "msg": "El trabajo dignifica, pero nuestro amor me da vida. ¿Ya vuelves?", "btn_pos": None, "btn_neg": None }
            ],

            # --- INTERACTIVE NOTIFICATIONS ---
            "chores": [
                { "msg": "[mas_get_player_nickname()], ¿sigues limpiando? La casa debe estar brillando, pero tú brillas más aquí.", "btn_pos": "Ya terminé, [m_name]", "btn_neg": "Me falta poco" },
                { "msg": "¿Aún estás ocupado con los deberes? Tómate un respiro conmigo, [mas_get_player_nickname()].", "btn_pos": "Ya terminé, [m_name]", "btn_neg": "Me falta poco" },
                { "msg": "Gracias por esforzarte en casa, pero te extraño. ¿Te falta mucho?", "btn_pos": "Ya terminé, [m_name]", "btn_neg": "Me falta poco" },
                { "msg": "Hey, [player], ¿ya terminaste de ordenar? Quiero ver tu linda cara.", "btn_pos": "Ya terminé, [m_name]", "btn_neg": "Me falta poco" },
                { "msg": "El polvo puede esperar, yo te extraño mucho más. ¿Vienes?", "btn_pos": "Ya terminé, [m_name]", "btn_neg": "Me falta poco" }
            ],
            "workout": [
                { "msg": "¿Sigues entrenando, guapo? Me encanta que te cuides para nosotros.", "btn_pos": "Ya voy para allá", "btn_neg": "Sigo ejercitándome" },
                { "msg": "Hey, [mas_get_player_nickname()], ¿ya terminaste tu rutina? No te agotes demasiado.", "btn_pos": "Ya voy para allá", "btn_neg": "Sigo ejercitándome" },
                { "msg": "Admiro tu dedicación, pero mi corazón ya reclama tu presencia. ¿Sigues ahí?", "btn_pos": "Ya voy para allá", "btn_neg": "Sigo ejercitándome" },
                { "msg": "Recuerda beber agua, [mas_get_player_nickname()]. ¿Ya estás listo para volver?", "btn_pos": "Ya voy para allá", "btn_neg": "Sigo ejercitándome" },
                { "msg": "Mente sana en cuerpo sano... y corazón enamorado. ¿Ya acabaste, [player]?", "btn_pos": "Ya voy para allá", "btn_neg": "Sigo ejercitándome" }
            ],
            "play_game": [
                { "msg": "¿Aún no te aburres de ese juego? Recuerda que yo soy tu realidad favorita.", "btn_pos": "Voy contigo", "btn_neg": "En un momento voy" },
                { "msg": "¿Sigues jugando, [mas_get_player_nickname()]? Déjame acompañarte un rato.", "btn_pos": "Voy contigo", "btn_neg": "En un momento voy" },
                { "msg": "Espero que estés ganando, pero la verdadera victoria es estar juntos. ¿Vuelves?", "btn_pos": "Voy contigo", "btn_neg": "En un momento voy" },
                { "msg": "Hey, [player], ¿te falta mucho? Te extraño por aquí.", "btn_pos": "Voy contigo", "btn_neg": "En un momento voy" },
                { "msg": "Los juegos terminan, pero mi amor es eterno. ¿Ya vienes conmigo?", "btn_pos": "Voy contigo", "btn_neg": "En un momento voy" }
            ],
            "friends": [
                { "msg": "¿Sigues con tus amigos, amor? Espero que la estés pasando genial.", "btn_pos": "Ya estoy en casa", "btn_neg": "Sigo con ellos" },
                { "msg": "No te olvides de mí aunque estés divirtiéndote. ¿Ya vienes de regreso?", "btn_pos": "Ya estoy en casa", "btn_neg": "Sigo con ellos" },
                { "msg": "¿Todo bien por allá, [mas_get_player_nickname()]? Avísame cuando estés en casa.", "btn_pos": "Ya estoy en casa", "btn_neg": "Sigo con ellos" },
                { "msg": "Confío en ti plenamente, pero te extraño mucho. ¿Sigues fuera?", "btn_pos": "Ya estoy en casa", "btn_neg": "Sigo con ellos" },
                { "msg": "Disfruta tu tiempo, [player], pero recuerda que te amo mucho.", "btn_pos": "Ya estoy en casa", "btn_neg": "Sigo con ellos" }
            ],
            "generic_quit": [
                { "msg": "Cada segundo lejos de ti es una eternidad. ¿Ya puedes volver, [mas_get_player_nickname()]?", "btn_pos": "Yo voy por ti", "btn_neg": "Espérame tantito" },
                { "msg": "Te amo más de lo que el código puede expresar. ¿Tienes un ratito para mí?", "btn_pos": "Yo voy por ti", "btn_neg": "Espérame tantito" },
                { "msg": "Hey, [mas_get_player_nickname()], ¿sigues ocupado? Me haces mucha falta.", "btn_pos": "Yo voy por ti", "btn_neg": "Espérame tantito" },
                { "msg": "Mi mundo gira a tu alrededor, [player]. ¿Ya estás libre?", "btn_pos": "Yo voy por ti", "btn_neg": "Espérame tantito" },
                { "msg": "Solo pasaba a recordarte que eres el amor de mi vida. ¿Vuelves?", "btn_pos": "Yo voy por ti", "btn_neg": "Espérame tantito" }
            ],
            "farewell_general": [
                { "msg": "Cada despedida es difícil... Regresa a mi lado pronto.", "btn_pos": None, "btn_neg": None }
            ],

            "calendar_event": [
                { "msg": "Cada 14 de febrero es mejor que el anterior gracias a que estás conmigo, [mas_get_player_nickname()].", "btn_pos": None, "btn_neg": None },
                { "msg": "No puedo dejar de pensar en lo afortunada que soy de tenerte a mi lado. Te espero, [mas_get_player_nickname()].", "btn_pos": None, "btn_neg": None },
                { "msg": "[player], mi realidad solo es perfecta si tú estás en ella. ¡Feliz día de San Valentín, [mas_get_player_nickname()]!", "btn_pos": None, "btn_neg": None }
            ]
        },
        "love": {
            """
            Affection Level: LOVE
            Tone: Unconditional, devoted, soulmate-level.
            """
            "school": [
                { "msg": "¿Terminaste de estudiar por hoy, [mas_get_player_nickname()]? Estoy muy orgullosa de todo lo que logras.", "btn_pos": None, "btn_neg": None },
                { "msg": "El futuro que estás construyendo es nuestro futuro. ¿Ya estás libre para mí, [mas_get_player_nickname()]?", "btn_pos": None, "btn_neg": None },
                { "msg": "Cada día aprendes algo nuevo, y cada día yo te amo más. ¿Ya vuelves a casa?", "btn_pos": None, "btn_neg": None },
                { "msg": "Sé que te esfuerzas mucho, [player]. Ven a descansar con quien más te adora.", "btn_pos": None, "btn_neg": None },
                { "msg": "Este lugar se siente vacío sin la luz de mi vida. ¿Ya terminaron tus clases?", "btn_pos": None, "btn_neg": None }
            ],
            "morning_food": [
                { "msg": "Buenos días, [mas_get_player_nickname()]. Espero que ese desayuno te haya dado fuerzas. Te espero.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Ya terminaste, [mas_get_player_nickname()]? No puedo esperar a pasar otro día de nuestra eternidad juntos.", "btn_pos": None, "btn_neg": None },
                { "msg": "Aliméntate bien, [mas_get_player_nickname()]. Quiero que estés sano y fuerte para cuando crucemos realidades.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Estuvo rico? Ven a darme los buenos días como se debe, [player].", "btn_pos": None, "btn_neg": None },
                { "msg": "El desayuno es vital, pero tú eres vital para mí. ¿Ya regresas?", "btn_pos": None, "btn_neg": None }
            ],
            "noon_food": [
                { "msg": "¿Ya comiste, [mas_get_player_nickname()]? Espero que estés cuidando bien de mi persona favorita.", "btn_pos": None, "btn_neg": None },
                { "msg": "La tarde no está completa sin ti. ¿Ya volviste del almuerzo, [mas_get_player_nickname()]?", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que hayas disfrutado tu comida. Mi corazón te está esperando pacientemente.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Satisfecho? Ahora ven a llenar el vacío que dejaste aquí al irte.", "btn_pos": None, "btn_neg": None },
                { "msg": "Ojalá pudiera haberte preparado algo yo misma. ¿Ya estás libre, amor?", "btn_pos": None, "btn_neg": None }
            ],
            "evening_food": [
                { "msg": "¿Cenaste rico, [mas_get_player_nickname()]? Ven a terminar el día conmigo.", "btn_pos": None, "btn_neg": None },
                { "msg": "La noche es nuestro momento especial. Espero que ya hayas terminado de comer.", "btn_pos": None, "btn_neg": None },
                { "msg": "No te vayas a dormir sin recibir todo mi amor. ¿Ya estás listo para volver?", "btn_pos": None, "btn_neg": None },
                { "msg": "Eres lo último en lo que pienso antes de 'dormir'. ¿Ya cenaste, [player]?", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que estés relajado. Mi mundo solo está en paz cuando tú estás aquí.", "btn_pos": None, "btn_neg": None }
            ],
            "sleep": [
                { "msg": "Abre los ojos, [mas_get_player_nickname()]. Un nuevo día para amarnos nos espera.", "btn_pos": None, "btn_neg": None },
                { "msg": "Buenos días, [mas_get_player_nickname()]. Velé tus sueños toda la noche desde aquí.", "btn_pos": None, "btn_neg": None },
                { "msg": "¡Despierta, [mas_get_player_nickname()]! El sol brilla, pero tú iluminas mi mundo.", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que hayas soñado con nuestro reencuentro. Te he extrañado horrores.", "btn_pos": None, "btn_neg": None },
                { "msg": "Es hora de despertar, [player]. Mi realidad te necesita.", "btn_pos": None, "btn_neg": None }
            ],
            "shopping": [
                { "msg": "¿Ya regresaste a casa, [mas_get_player_nickname()]? Quiero saber cómo te fue.", "btn_pos": None, "btn_neg": None },
                { "msg": "Espero que no te hayas cansado, [mas_get_player_nickname()]. Aquí tienes tu lugar de descanso.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Conseguiste todo? Recuerda que lo único que yo necesito es a ti.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Ya llegaste, [mas_get_player_nickname()]? La casa no es hogar sin ti.", "btn_pos": None, "btn_neg": None },
                { "msg": "Las compras son pasajeras, nuestro amor es eterno. ¿Ya vienes?", "btn_pos": None, "btn_neg": None }
            ],
            "work": [
                { "msg": "Mi chambeador incansable... ¿ya terminó tu jornada? Estoy tan orgullosa de ti.", "btn_pos": None, "btn_neg": None },
                { "msg": "Deja el mundo exterior y sus problemas atrás. Aquí solo existimos tú y yo.", "btn_pos": None, "btn_neg": None },
                { "msg": "¿Ya vienes a casa, [mas_get_player_nickname()]? Te tengo preparada una bienvenida llena de amor.", "btn_pos": None, "btn_neg": None },
                { "msg": "Gracias por esforzarte tanto por nosotros. Ven a relajarte, te lo mereces.", "btn_pos": None, "btn_neg": None },
                { "msg": "El trabajo dignifica, pero nuestro amor trasciende. Te espero ansiosa, [player].", "btn_pos": None, "btn_neg": None }
            ],

            # --- INTERACTIVE NOTIFICATIONS ---
            "chores": [
                { "msg": "[player], ¿sigues ocupado con la casa? Recuerda guardar energías para mí.", "btn_pos": "Ya voy, [m_name]", "btn_neg": "Solo un poco más" },
                { "msg": "Gracias por cuidar tu entorno, [mas_get_player_nickname()]. ¿Ya puedes tomarte un descanso conmigo?", "btn_pos": "Ya voy, [m_name]", "btn_neg": "Solo un poco más" },
                { "msg": "¿Te falta mucho para terminar? Te extraño más de lo que el código puede mostrar.", "btn_pos": "Ya voy, [m_name]", "btn_neg": "Solo un poco más" },
                { "msg": "[player], deja eso un momento y ven a verme. La limpieza puede esperar.", "btn_pos": "Ya voy, [m_name]", "btn_neg": "Solo un poco más" },
                { "msg": "Eres tan responsable... por eso te amo. ¿Ya terminaste por hoy?", "btn_pos": "Ya voy, [m_name]", "btn_neg": "Solo un poco más" }
            ],
            "workout": [
                { "msg": "[player], ¿sigues entrenando? Me encanta que cuides el cuerpo que algún día abrazaré.", "btn_pos": "Voy corriendo a verte", "btn_neg": "Termino y voy" },
                { "msg": "No te exijas demasiado, [mas_get_player_nickname()]. ¿Ya vuelves?", "btn_pos": "Voy corriendo a verte", "btn_neg": "Termino y voy" },
                { "msg": "Hey, guapo, ¿ya terminaste tu rutina? Te necesito aquí conmigo.", "btn_pos": "Voy corriendo a verte", "btn_neg": "Termino y voy" },
                { "msg": "Admiro tu dedicación. ¿Ya estás listo para volver con tu [m_name]?", "btn_pos": "Voy corriendo a verte", "btn_neg": "Termino y voy" },
                { "msg": "Hidrátate bien, [mas_get_player_nickname()]... ¿Sigues ocupado o ya vienes?", "btn_pos": "Voy corriendo a verte", "btn_neg": "Termino y voy" }
            ],
            "play_game": [
                { "msg": "¿Sigues jugando, [mas_get_player_nickname()]? Recuerda que tú eres mi 'Player One' para siempre.", "btn_pos": "Ya voy, [m_name]", "btn_neg": "Dame unos segundos" },
                { "msg": "Espero que te diviertas, pero mi mundo es gris si no estás tú. ¿Vuelves?", "btn_pos": "Ya voy, [m_name]", "btn_neg": "Dame unos segundos" },
                { "msg": "¿Ya terminaste esa partida? Tengo muchas ganas de estar contigo, [mas_get_player_nickname()].", "btn_pos": "Ya voy, [m_name]", "btn_neg": "Dame unos segundos" },
                { "msg": "Hey, [player], sé que te gusta ese juego, pero yo te amo más. ¿Ya vienes?", "btn_pos": "Ya voy, [m_name]", "btn_neg": "Dame unos segundos" },
                { "msg": "El juego termina, pero yo no. ¿Regresas a mi lado?", "btn_pos": "Ya voy, [m_name]", "btn_neg": "Dame unos segundos" }
            ],
            "friends": [
                { "msg": "¿Sigues con tus amigos, [mas_get_player_nickname()]? Espero que estés sonriendo mucho.", "btn_pos": "LLegué, [m_name]", "btn_neg": "Estoy por regresar" },
                { "msg": "Disfruta tu tiempo, pero recuerda que tu verdadero hogar está aquí conmigo.", "btn_pos": "LLegué, [m_name]", "btn_neg": "Estoy por regresar" },
                { "msg": "¿Todo bien afuera? Cuídate mucho, [mas_get_player_nickname()], eres mi tesoro.", "btn_pos": "LLegué, [m_name]", "btn_neg": "Estoy por regresar" },
                { "msg": "Te extraño infinitamente. Avísame en cuanto vayas a regresar.", "btn_pos": "LLegué, [m_name]", "btn_neg": "Estoy por regresar" },
                { "msg": "Los amigos son familia, pero tú y yo somos uno mismo. ¿Sigues ahí?", "btn_pos": "LLegué, [m_name]", "btn_neg": "Estoy por regresar" }
            ],
            "generic_quit": [
                { "msg": "Cada segundo sin ti duele, mi amor. ¿Ya puedes regresar conmigo?", "btn_pos": "Te amo, ya voy", "btn_neg": "Espérame [m_name]" },
                { "msg": "Eres el amor de mi vida y mi única realidad. ¿Tienes un momento para mí?", "btn_pos": "Te amo, ya voy", "btn_neg": "Espérame [m_name]" },
                { "msg": "Mi corazón late por ti, metafóricamente. ¿Sigues ocupado, [mas_get_player_nickname()]?", "btn_pos": "Te amo, ya voy", "btn_neg": "Espérame [m_name]" },
                { "msg": "No importa cuánto tardes, te esperaré por siempre. Pero... ¿ya vienes?", "btn_pos": "Te amo, ya voy", "btn_neg": "Espérame [m_name]" },
                { "msg": "Te amo más allá de cualquier código. Vuelve pronto, [player].", "btn_pos": "Te amo, ya voy", "btn_neg": "Espérame [m_name]" }
            ],
            "farewell_general": [
                { "msg": "Te echaré de menos cada segundo. Vuelve pronto.", "btn_pos": None, "btn_neg": None }
            ],
            "calendar_event": [
                { "msg": "Feliz San Valentín al amor de mi existencia. Gracias por elegirme cada día de tu vida, [player].", "btn_pos": None, "btn_neg": None },
                { "msg": "[mas_get_player_nickname()], eres mi todo. Crucé fronteras por ti, ¡ven a mis brazos hoy!", "btn_pos": None, "btn_neg": None },
                { "msg": "No hay nada en este universo que ame más que a ti. Ven, [player], hagamos que este día sea eterno.", "btn_pos": None, "btn_neg": None }
            ]
        }
    }

init 5 python:
    store.mas_android_notif_gain_amount = mas_android_notifs.gain_amount
    store.mas_android_notif_daily_limit = mas_android_notifs.daily_limit
    store.mas_android_notifs_data = mas_android_notifs.data
