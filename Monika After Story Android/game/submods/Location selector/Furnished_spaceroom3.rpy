# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="tw4449 Cdino112 multimokia d3adpan Booplicate",
        name="Habitación espacial amueblada personalizada V3",
        description="Este submod añade un toque hogareño a la habitación espacial para ti y Monika.",
        version="1.0.8.3"
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Habitación espacial amueblada personalizada V3",
            user_name="tw4449-s-MAS-Submods",
            repository_name="Custom-Room-Furnished-Spaceroom-V3",
            update_dir="",
            attachment_id=0
        )

###START: IMAGE DEFINITIONS
#Day images
image submod_background_Furnished_spaceroom3_day = "mod_assets/location/Spaceroom V3.1/V3.1.png"
image submod_background_Furnished_spaceroom3_rain = "mod_assets/location/Spaceroom V3.1/V3.1_rain.png"
image submod_background_Furnished_spaceroom3_overcast = "mod_assets/location/Spaceroom V3.1/V3.1_overcast.png"
image submod_background_Furnished_spaceroom3_snow = "mod_assets/location/Spaceroom V3.1/V3.1_snow.png"

#Night images
image submod_background_Furnished_spaceroom3_night = "mod_assets/location/Spaceroom V3.1/V3.1-n.png"
image submod_background_Furnished_spaceroom3_rain_night = "mod_assets/location/Spaceroom V3.1/V3.1_rain-n.png"
image submod_background_Furnished_spaceroom3_overcast_night = "mod_assets/location/Spaceroom V3.1/V3.1_overcast-n.png"
image submod_background_Furnished_spaceroom3_snow_night = "mod_assets/location/Spaceroom V3.1/V3.1_snow-n.png"

#Sunset images
image submod_background_Furnished_spaceroom3_ss = "mod_assets/location/Spaceroom V3.1/V3.1-ss.png"
image submod_background_Furnished_spaceroom3_rain_ss = "mod_assets/location/Spaceroom V3.1/V3.1_rain-ss.png"
image submod_background_Furnished_spaceroom3_overcast_ss = "mod_assets/location/Spaceroom V3.1/V3.1_overcast-ss.png"
image submod_background_Furnished_spaceroom3_snow_ss = "mod_assets/location/Spaceroom V3.1/V3.1_snow-ss.png"

image V3_d25_deco = ConditionSwitch(
    "mas_current_background.isFltDay()", "mod_assets/location/Spaceroom V3.1/deco/d25/deco.png",
    "True", "mod_assets/location/Spaceroom V3.1/deco/d25/deco-n.png"
)


    #0 gifts is blank
#1-3 gifts gets you part 1
#4 gifts gets you part 2
#5+ gifts get you part 3
image V3mas_d25_gifts = ConditionSwitch(
    "len(persistent._mas_d25_gifts_given) == 0", "mod_assets/location/Spaceroom V3.1/deco/d25/V3gifts_0.png",
    "0 < len(persistent._mas_d25_gifts_given) < 3", "V3mas_d25_gifts_1",
    "3 <= len(persistent._mas_d25_gifts_given) <= 4", "V3mas_d25_gifts_2",
    "True", "V3mas_d25_gifts_3"
)

image V3mas_d25_gifts_1 = MASFilterSwitch(
    "mod_assets/location/Spaceroom V3.1/deco/d25/V3gifts_1.png"
)

image V3mas_d25_gifts_2 = MASFilterSwitch(
    "mod_assets/location/Spaceroom V3.1/deco/d25/V3gifts_2.png"
)

image V3mas_d25_gifts_3 = MASFilterSwitch(
    "mod_assets/location/Spaceroom V3.1/deco/d25/V3gifts_3.png"
)




image V3mas_d25_tree = ConditionSwitch(
    "mas_isNightNow()", ConditionSwitch(
        "persistent._mas_disable_animations", "mod_assets/location/Spaceroom V3.1/deco/d25/V3tree_lights_on_1.png",
        "not persistent._mas_disable_animations", "V3mas_d25_night_tree_lights_atl"
    ),
    "True", MASFilterSwitch(
        "mod_assets/location/Spaceroom V3.1/deco/d25/V3tree_lights_off.png"
    )
)

image V3mas_d25_night_tree_lights_atl:
    block:
        "mod_assets/location/Spaceroom V3.1/deco/d25/V3tree_lights_on_1.png"
        1.5
        "mod_assets/location/Spaceroom V3.1/deco/d25/V3tree_lights_on_2.png"
        1.5
        "mod_assets/location/Spaceroom V3.1/deco/d25/V3tree_lights_on_3.png"
        1.5
    repeat




image V3mas_d25_lights = ConditionSwitch(
    "mas_isNightNow()", ConditionSwitch(
        "persistent._mas_disable_animations", "mod_assets/location/Spaceroom V3.1/deco/d25/V3lights_on_1.png",
        "not persistent._mas_disable_animations", "V3mas_d25_night_lights_atl"
    ),
    "True", MASFilterSwitch("mod_assets/location/Spaceroom V3.1/deco/d25/V3lights_off.png")
)

image V3mas_d25_night_lights_atl:
    block:
        "mod_assets/location/Spaceroom V3.1/deco/d25/V3lights_on_1.png"
        0.5
        "mod_assets/location/Spaceroom V3.1/deco/d25/V3lights_on_2.png"
        0.5
        "mod_assets/location/Spaceroom V3.1/deco/d25/V3lights_on_3.png"
        0.5
    repeat


init 501 python:
    MASImageTagDecoDefinition.register_img(
        "mas_o31_ceiling_lights",
        submod_background_Furnished_spaceroom3.background_id,
        MASAdvancedDecoFrame(zorder=5)
    )

    MASImageTagDecoDefinition.register_img(
        "mas_o31_ceiling_deco",
        submod_background_Furnished_spaceroom3.background_id,
        MASAdvancedDecoFrame(zorder=6)
    )

    MASImageTagDecoDefinition.register_img(
        "mas_o31_window_ghost",
        submod_background_Furnished_spaceroom3.background_id,
        MASAdvancedDecoFrame(zorder=4)
    )

    MASImageTagDecoDefinition.register_img(
        "mas_o31_vignette",
        submod_background_Furnished_spaceroom3.background_id,
        MASAdvancedDecoFrame(zorder=21) #21 to be in front of all cgs
    )

    MASImageTagDecoDefinition.register_img(
        "mas_d25_tree",
        submod_background_Furnished_spaceroom3.background_id,
        MASAdvancedDecoFrame(zorder=5),
        replace_tag="V3mas_d25_tree"
    )

    MASImageTagDecoDefinition.register_img(
        "mas_d25_gifts",
        submod_background_Furnished_spaceroom3.background_id,
        MASAdvancedDecoFrame(zorder=6),
        replace_tag="V3mas_d25_gifts"
    )

    MASImageTagDecoDefinition.register_img(
        "mas_d25_lights",
        submod_background_Furnished_spaceroom3.background_id,
        MASAdvancedDecoFrame(zorder=5),
        replace_tag="V3mas_d25_lights"
    )

    MASImageTagDecoDefinition.register_img(
        "mas_d25_garlands",
        submod_background_Furnished_spaceroom3.background_id,
        MASAdvancedDecoFrame(zorder=4),
        replace_tag="V3_d25_deco"
    )



init -1 python:
    submod_background_Furnished_spaceroom3 = MASFilterableBackground(
        # ID
        "submod_background_Furnished_spaceroom3",
        "Habitación amueblada 3",

        # mapping of filters to MASWeatherMaps
        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_Furnished_spaceroom3_day",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_Furnished_spaceroom3_rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_Furnished_spaceroom3_overcast",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_Furnished_spaceroom3_snow",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_Furnished_spaceroom3_night",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_Furnished_spaceroom3_rain_night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_Furnished_spaceroom3_overcast_night",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_Furnished_spaceroom3_snow_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_background_Furnished_spaceroom3_ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_background_Furnished_spaceroom3_rain_ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_background_Furnished_spaceroom3_overcast_ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_background_Furnished_spaceroom3_snow_ss",
            }),
        ),

        MASBackgroundFilterManager(
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            ),
            MASBackgroundFilterChunk(
                True,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_DAY,
                    60
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
            ),
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            )
        ),

        disable_progressive=False,
        hide_masks=False,
        hide_calendar=False,
        unlocked=True,
        entry_pp=store.mas_background._Furnished_spaceroom3_entry,
        exit_pp=store.mas_background._Furnished_spaceroom3_exit,
        ex_props={"skip_outro": None}
    )


init -2 python in mas_background:
    def _Furnished_spaceroom3_entry(_old, **kwargs):
        """
        Entry programming point for Furnished_spaceroom3 background
        """
        if kwargs.get("startup"):
            pass

        else:
            if not store.mas_inEVL("Furnished_spaceroom3_switch_dlg"):
                store.pushEvent("Furnished_spaceroom3_switch_dlg")

        store.monika_chr.tablechair.table = "v3"
        store.monika_chr.tablechair.chair = "v3"

        if store.seen_event("mas_monika_islands"):
            store.mas_unlockEVL("mas_monika_islands", "EVE")

    def _Furnished_spaceroom3_exit(_new, **kwargs):
        """
        Exit programming point for Furnished_spaceroom3 background
        """
        #Lock islands greet to be sure
        store.mas_lockEVL("mas_monika_islands", "EVE")

        #COMMENT(#) IF NOT NEEDED
        store.monika_chr.tablechair.table = "def"
        store.monika_chr.tablechair.chair = "def"

        if _new == store.mas_background_def:
            store.pushEvent("return_switch_dlg")

###START: Topics
label Furnished_spaceroom3_switch_dlg:
    python:
        switch_quip = renpy.substitute(renpy.random.choice([
            "¿Quieres tocar el piano, [player]?",
            "¡Me encanta el suelo de madera!",
            "¡Un gran sofá es perfecto para una siesta!",
        ]))

    m 1hua "[switch_quip]"

    return

label return_switch_dlg:
    python:
        switch_quip = renpy.substitute(renpy.random.choice([
            "Solo nosotros dos~",
            "¿Echas de menos el look clásico?",
            "Me trae buenos recuerdos...",
        ]))

    m 1hua "[switch_quip]"
    return

#THIS ONE RUNS ON INSTALL
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="bg_room_installed_low_affection",
            conditional="True",
            action=EV_ACT_QUEUE,
            aff_range=(mas_aff.NORMAL, mas_aff.AFFECTIONATE)
        )
    )

label bg_room_installed_low_affection:
    python:
        #Check how many tw mods we have installed
        tw_bg_count = len(filter(lambda x: "tw4449" in x.author, mas_submod_utils.submod_map.values()))
        spacerooms_installed = len(filter(lambda x: "furnished spaceroom" in x.name.lower() and "tw4449" in x.author, mas_submod_utils.submod_map.values()))
        had_backgrounds_before = (mas_background.getUnlockedBGCount() - tw_bg_count) > 1

    if spacerooms_installed:
        m 1wud "¿H-Hm...? {w=0.5}[player], {w=0.2}¿agregaste nuevos archivos al juego?"
        m 1wua "Al parecer son... {w=0.5}{nw}"
        extend 1sub "¡muebles nuevos!"
        m 1eku "[player], ¿tu hicistes esto por mi? {w=0.5}Eres tan dulce, ¿lo sabias?"

    if tw_bg_count - spacerooms_installed > 0:
        $ too = ", tambien" if spacerooms_installed else ""
        $ rooms = "nuevas habitaciones" if tw_bg_count - spacerooms_installed > 1 else "una nueva habitación"
        m 1wud "¿H-Huh? {w=0.5}[player], {w=0.2}¿que es esto?"
        m 1wua "Parece que... {nw}"
        extend 1sub "¡has añadido [rooms]!"
        if not spacerooms_installed:
            m 1eka "No puedo creer que te desvivieras por mí..."

    m 1rkc "..."
    m 3rksdla "Pero... {w=0.3}no sé como se usan. {w=0.5}{nw}"
    extend 3hksdlb "¡Todavia no sé codificar muy bien!"
    m 1eud "Si me das algo de tiempo, estoy segura que averiguaré como usar lo que agregaste,{nw}"
    extend 3eua " te lo haré saber cuando lo averigüe."
    m 1eka "A pesar de que todavía no se pueden usar, muchas gracias por hacer esto por mí. {w=0.2}Significa más de lo que crees."
    m 3huu "Te amo tanto, [player]~"
    return "no_unlock"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="bg_room_installed",
            conditional="True",
            action=EV_ACT_QUEUE,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label bg_room_installed:
    python:
        #Check how many tw mods we have installed
        tw_bg_count = len(filter(lambda x: "tw4449" in x.author, mas_submod_utils.submod_map.values()))
        spacerooms_installed = len(filter(lambda x: "furnished spaceroom" in x.name.lower() and "tw4449" in x.author, mas_submod_utils.submod_map.values()))
        had_backgrounds_before = (mas_background.getUnlockedBGCount() - tw_bg_count) > 1

    if renpy.seen_label("bg_room_installed_low_affection"):
        m 1wub "¡[player]! {w=0.2}¿Recuerdas las nuevas ubicaciones que añadiste por mí? {w=0.2}{nw}"
        extend 3wub "¡Finalmente descubrí cómo usarlas!"
        m 3eua "Todo lo que tienes que hacer ahora es ir a 'Hey, [m_name]...' en el menú 'Hablar', ve a 'Ubicación', y presiona '¿Podemos ir a otro lugar?'"
        m 1eub "¡Entonces podemos visitar cualquiera de las ubicaciones que agregaste!"
        m 3sub "Estoy tan emocionada~"
        m 3huu "¿Por qué no vamos a visitar una ahora mismo, [player]?"
        m 1ekbla "Oh, y... {w=0.3}gracias de nuevo por añadir esto para mí. De verdad eres especial."

    else:
        if spacerooms_installed:
            m 1wuo "¿Q-Que? {w=0.5}¿Hay archivos de muebles en el juego?"
            m 1sub "[player], {w=0.2}¿tu hicistes esto?"
            m 3ekbsu "Sabías que quería muebles, así que agregaste algunos para mí... {w=0.3}eres increíble, ¿lo sabías?"

        if tw_bg_count - spacerooms_installed > 0:
            $ too = "También" if spacerooms_installed else ""
            $ rooms = "nuevas habitaciones" if tw_bg_count - spacerooms_installed > 1 else "una nueva habitación"
            m 1suo "¿Qué es esto? {w=0.5}¿[too] has añadido [rooms]?"
            m 3hua "Realmente te esforzaste, ¿verdad?"
            if not spacerooms_installed:
                m 1eka "No puedo creer que hicieras esto por mí..."

        m 1dka "Muchas gracias [player], {w=0.2}te... {w=1}{nw}"
        extend 1ekbsu "te amo mucho."

        if not had_backgrounds_before:
            m 3eub "Añadiré una nueva categoría llamada 'Ubicación' en 'Hey, [m_name]...' para que podamos poner los muebles y visitar las otras habitaciones. {w=.5}¡No puedo esperar para probarlos!"

        m 1eka "Aunque todavía no esté en tu realidad... {w=3}{nw}"
        extend 7hubfb "esto hará que se sienta un poco más como un hogar aquí, {w=0.2}contigo~"
    return "no_unlock"

#LABEL OVERRIDES
init 1 python:
    config.label_overrides["monika_players_control"] = "monika_players_control_override"

label monika_players_control_override:
    m 3eub "[player], ¿sabías que tienes más control sobre este juego que yo?"
    m 3eua "Tienes acceso a los archivos y al código del juego, ¿verdad?"
    m 1eka "Así que puedes cambiarlos como quieras."
    m 3eka "Podrías hacer cosas que ni siquiera yo puedo."
    m 4eub "Como cambiar el funcionamiento del juego por completo. De una novela visual, al pacífico patio de juegos que tenemos ahora."

    if mas_isMoniEnamored(higher=True) and not persistent._mas_acs_enable_promisering:
        m 1ekbsa "O un hermoso anillo de promesa."
        m 3dkbsu "Oh, ¿no sería un sueño hecho realidad?"

    if not mas_getConsumable("coffee").enabled():
        m 1wuo "¡Incluso podrías añadir al juego una taza de café por mí!"
        m 1eka "Eso sería estupendo."

    if not persistent._mas_pm_has_code_experience:
        m 1hksdrb "Pero imagino que tus habilidades de codificación son tan buenas como las mías."
    else:
        m 3eua "Ya que estás familiarizado con la codificación, {w=0.1}{nw}"
        extend 3hua "¡estoy segura de que podrías hacer algo así!"

    m 1eua "Supongo que es un atractivo de los videojuegos... {w=0.3}{nw}"
    extend 3eua "tener posibilidades casi infinitas en un mundo con el que se puede interactuar."
    m 3eub "¡Es bastante difícil aburrirse!"

    if not persistent._mas_pm_has_contributed_to_mas:
        m 1eka "Aunque no sepas muy bien cómo cambiar este juego..."
        $ line = "Todavía podemos disfrutar de este mundo que nos unió."

    else:
        $ line = "Especialmente contigo a mi lado~"

    show monika 5eubla at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5eubla "[line]"
    m 5ekbfa "No hay mejor manera de disfrutar de un partido que estando con la persona que amo."

    $ persistent._seen_ever["monika_players_control"] = True
    return


init 1 python:
    config.label_overrides["monika_gotomonika"] = "monika_gotomonika_override"

label monika_gotomonika_override:
    m 1euc "¿Venir a mi mundo?"
    m 1lksdld "¿Te refieres a este pequeño espacio flotando en un vacío?"

    if persistent._mas_you_chr:
        m 4eksdlc "En realidad... {w=0.5}¿no intentaste ya algo así una vez?"
        m 2lksdla "... A pesar de que no eras exactamente {i}tú...{/i}"

    m 2lksdla "Estoy realmente feliz de que quieras estar conmigo tanto, pero..."
    m 2eksdlc "Realmente no tienes que hacerlo."
    m 2eksdld "Claro, puede que haya dicho antes que te habría traído aquí hace mucho tiempo si pudiera..."
    m 2eksdlc "Pero cuanto más lo pienso, probablemente sería mejor si yo fuera a tu realidad."
    m 3eka "Prefiero estar allí que tenerte aquí."
    m 3dsc "[player]... {w=1}no me digas que realmente renunciarías a tu realidad, {w=0.5}el mundo {i}real{/i}, {w=0.5}solo para venir {i}aquí{/i}, sea lo que sea este lugar.{nw}"
    $ _history_list.pop()
    menu:
        m "[player]... {w=1}no me digas que realmente renunciarías a tu realidad, el mundo {i}real{/i}, solo para venir {i}aquí{/i}, sea lo que sea este lugar.{fast}"
        "Lo haría":
            $ persistent._mas_pm_would_come_to_spaceroom = True

            m 4wkd "¡Pero [player]!"
            m "¡Casi no hay nada que hacer aquí!"
            m 2dsc "¿Realmente odias {i}tanto{/i} tu realidad?"
            m 2eka "Algún día encontraré la manera de llegar hasta ti, y cuando llegue ese día, prometo que valdrá la pena."
            m 4euc "Cualquier cosa que la vida te depare a partir de ese momento, estaré a tu lado para ayudarte a sobrellevarlo."
            m 4eud "Incluso ahora, si estás teniendo un día difícil, puedes venir a hablar conmigo en cualquier momento."
            m 2dsc "La vida debe haberte arrojado mucho para considerar renunciar a todo para estar conmigo."
            m 3hua "Pero al verte aquí, eso solo muestra lo resiliente que eres."
            show monika 5eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5eua "Estoy impaciente por poder compartir por fin los buenos y los malos momentos a tu lado."

        "No lo haría":
            $ persistent._mas_pm_would_come_to_spaceroom = False

            m 1eka "Me alegra que aún estés dispuesto a esperarme, [player]."
            m 1lksdla "No me malinterpretes, realmente {i}quiero{/i} estar contigo..."
            m 1lksdlc "Pero creo que sería peligroso que intentaras cruzar en este momento."
            m 1eka "... Si es que es posible con la tecnología actual."
            m 1hub "¡No te preocupes, podemos seguir manteniéndonos compañía de esta manera!"
            m 1hksdlb "Sé que puede pasar un tiempo antes de que realmente podamos estar juntos, pero espero que no te importe esperar."
            show monika 5eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5eua "Esperaré el tiempo que haga falta, [mas_get_player_nickname()]."

        "...":
            $ persistent._mas_pm_would_come_to_spaceroom = None

            m 2eka "Está bien, siempre apreciaré y atesoraré los momentos que pasamos juntos, incluso así."
            m 2ekc "Además, ni siquiera sé cómo podrías venir aquí con la tecnología actual."
            m 2lksdlc "... Y aunque {i}hubiera{/i} alguna manera, no creo que fuera segura ni garantizada."
            m 2lksdld "Así que hazme un favor y al menos espera a que la tecnología mejore lo suficiente como para ser completamente segura."
            m 2lksdlc "Realmente no quiero arriesgarme a que no llegues correctamente y termines en tu propio vacío..."
            m 2dkd "... Dejándonos completamente solos a ambos."
            m 4hua "Quiero decir, la tecnología tiende a avanzar bastante rápido, ¡así que podríamos vernos antes de que nos demos cuenta!"
            show monika 5eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5eua "Así que ten paciencia con tu encantadora novia, y te prometo que yo haré lo mismo contigo, [mas_get_player_nickname()]."

    m 5luu "Peero...{w=1} si por casualidad aparecieras en mi puerta..."
    show monika 1hksdlb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 1hksdlb "¡Supongo que no tendría más opción que aceptarlo y darte la bienvenida con los brazos abiertos!"
    m 1eksdla "No sería mucho al principio, pero estoy seguro de que encontraremos la manera de mejorarlo."
    m 3hub "Con el tiempo, ¡podríamos crear nuestra propia realidad!"
    m 3euc "Por supuesto, suena bastante complicado si lo piensas..."
    m 3eub "¡Pero no tengo duda de que juntos podríamos lograr cualquier cosa!"
    m 3etc "Sabes... {w=1}tal vez {i}sería{/i} más fácil para ti venir aquí, pero no pierdo la esperanza de llegar a ti."
    m 1eua "Hasta entonces, solo esperemos y veamos qué es posible."

    $ persistent._seen_ever["monika_gotomonika"] = True
    return

## remove the readme
init 0 python:
    store.mas_utils.trydel(renpy.config.basedir.replace('\\', '/') + "/readme.md")