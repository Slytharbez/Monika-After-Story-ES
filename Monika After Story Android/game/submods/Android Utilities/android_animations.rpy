init -990 python in mas_submod_utils:
    submod = Submod(
        author="Antigravity",
        name="Android Animations",
        description="Añade animaciones suaves a los menús y botones (fade-in, fade-out).",
        version="2.6.0"
    )

# Prioridad alta para sobrescribir definiciones
init offset = 100

# Variable para controlar si la columna izquierda debe animarse (True) o no (False)
default mas_anim_twopane_left = True

# TRANSFORMACIÓN GENERAL
transform android_screen_fade:
    on show:
        alpha 0.0
        easein 0.5 alpha 1.0
    on hide:
        easeout 0.5 alpha 0.0

# TRANSFORMACIÓN ESTÁTICA (Pero con salida suave)
transform android_noop:
    alpha 1.0
    on hide:
        easeout 0.5 alpha 0.0

# TRANSFORMACIÓN LENTA (Para Prompts)
transform android_fade_in_slow:
    alpha 0.0
    easein 0.8 alpha 1.0

# LABEL PERSONALIZADO PARA CERRAR EXTRAS CON ANIMACIÓN
label mas_extra_menu_close_android:
    $ store.mas_extramenu.menu_visible = False
    
    hide screen mas_extramenu_area with Dissolve(0.5)

    if store.mas_sprites.zoom_level != prev_zoom:
        call mas_extra_menu_zoom_callback

    if store.mas_globals.in_idle_mode:
        $ mas_coreToIdleShield()
    else:
        $ mas_DropShield_core()

    show monika idle
    jump ch30_loop


# REDEFINICIÓN DE PANTALLAS (SCREENS)

# 0. Menú de Elección Principal (Hablar root menu)
screen talk_choice(items):
    style_prefix "talk_choice"

    # Resetear flag al entrar
    on "show" action Function(setattr, store, "mas_anim_twopane_left", True)

    # Manejar salida con Escape/Click Derecho para asegurar reset
    key "game_menu" action [
        Function(setattr, store, "mas_anim_twopane_left", True),
        Return(False)
    ]

    vbox at android_screen_fade:
        for i in items:
            textbutton i.caption action i.action

# 1. Menús de Selección (Categorías, Submenús)
screen twopane_scrollable_menu(prev_items, main_items, left_area, left_align, right_area, right_align, cat_length):
    #on "hide" action Function(store.main_adj.change, 0)

    default flt_evs = None
    default is_search_active = False

    style_prefix "twopane_scrollable_menu"

    # Manejar salida con Escape/Click Derecho para asegurar reset del flag de animación
    key "game_menu" action [
        Function(setattr, store, "mas_anim_twopane_left", True),
        Return(False)
    ]

    fixed: 
        if flt_evs is not None:
            # Resultados de búsqueda (Lento)
            fixed at android_fade_in_slow:
                pos (left_area[0], left_area[1])
                xsize right_area[0] - left_area[0] + right_area[2]
                ysize left_area[3]

                vbox:
                    pos (0, 0)
                    anchor (0, 0)

                    viewport:
                        id "search_viewport"
                        yfill False
                        mousewheel True
                        arrowkeys True

                        has vbox
                        for ev in flt_evs:
                            textbutton ev.prompt:
                                if renpy.has_label(ev.eventlabel) and not seen_event(ev.eventlabel):
                                    style "scrollable_menu_new_button"
                                else:
                                    style "scrollable_menu_button"
                                xsize right_area[0] - left_area[0] + right_area[2]
                                action [
                                    Function(setattr, store, "mas_anim_twopane_left", True),
                                    Function(mas_ui.twopane_menu_delegate_callback, ev.eventlabel), 
                                    Return(ev.eventlabel)
                                ]

                    null height 20

                    textbutton _("No importa"):
                        style "scrollable_menu_button"
                        xsize right_area[0] - left_area[0] + right_area[2]
                        action [
                            Function(setattr, store, "mas_anim_twopane_left", True),
                            Return(False)
                        ]

                bar:
                    style "classroom_vscrollbar"
                    value YScrollValue("search_viewport")
                    unscrollable "hide"

                    xalign left_align / 2 + 0.005


        else:

            # Columna izquierda (Categorías) - Animación Condicional
            # Usamos expresión Python en el 'at' para elegir transformación, evitando errores de sintaxis ATL
            fixed at (android_screen_fade if store.mas_anim_twopane_left else android_noop):
                anchor (0, 0)
                pos (left_area[0], left_area[1])
                xsize left_area[2]

                if cat_length != 1:
                    ysize left_area[3]
                else:
                    ysize left_area[3] + evhand.LEFT_EXTRA_SPACE

                vbox:
                    ypos 0
                    yanchor 0

                    viewport:
                        id "prev_viewport"
                        yadjustment store.mas_category_adj
                        yfill False
                        mousewheel True
                        arrowkeys True

                        has vbox
                        for i_caption, i_label in prev_items:
                            textbutton i_caption:
                                if renpy.has_label(i_label) and not seen_event(i_label):
                                    style "twopane_scrollable_menu_new_button"

                                elif not renpy.has_label(i_label):
                                    style "twopane_scrollable_menu_special_button"

                                # ACCIÓN CLAVE: Function() no marca el botón como "selected"
                                action [
                                    Function(setattr, store, "mas_anim_twopane_left", False), 
                                    Function(store.mas_topic_adj.change, 0), 
                                    Return(i_label)
                                ]

                    if cat_length != 1:
                        null height 20

                        if cat_length == 0:
                            textbutton _("No importa") action [
                                Function(setattr, store, "mas_anim_twopane_left", True),
                                Return(False)
                            ]

                        elif cat_length > 1:
                            textbutton _("Regresar") action [
                                Function(setattr, store, "mas_anim_twopane_left", True),
                                Return(-1)
                            ]

                bar:
                    style "classroom_vscrollbar"
                    value YScrollValue("prev_viewport")
                    unscrollable "hide"
                    xalign left_align


            if main_items:
                # Columna derecha (Prompts) - Animación Lenta (0.8s) y siempre activa
                fixed at android_fade_in_slow:
                    area right_area

                    vbox:
                        ypos 0
                        yanchor 0

                        viewport:
                            id "main_viewport"
                            yadjustment store.mas_topic_adj
                            yfill False
                            mousewheel True
                            arrowkeys True

                            has vbox
                            for i_caption, i_label in main_items:
                                textbutton i_caption:
                                    if renpy.has_label(i_label) and not seen_event(i_label):
                                        style "twopane_scrollable_menu_new_button"

                                    elif not renpy.has_label(i_label):
                                        style "twopane_scrollable_menu_special_button"

                                    action [
                                        Function(setattr, store, "mas_anim_twopane_left", True),
                                        Return(i_label)
                                    ]
                                    
                        null height 20

                        textbutton _("No importa") action [
                            Function(setattr, store, "mas_anim_twopane_left", True),
                            Return(False)
                        ]

                    bar:
                        style "classroom_vscrollbar"
                        value YScrollValue("main_viewport")
                        unscrollable "hide"
                        xalign right_align


        # Barra de búsqueda - Animación Condicional
        if not persistent._mas_hidesearch:
            frame at (android_screen_fade if store.mas_anim_twopane_left else android_noop):
                xpos left_area[0]
                ypos left_area[1] - 55
                xsize right_area[0] - left_area[0] + right_area[2]
                ysize 40
                background Solid(store.mas_ui.TEXT_FIELD_BG)

                if is_search_active:
                    viewport:
                        draggable False
                        arrowkeys False
                        mousewheel "horizontal"
                        xsize right_area[0] - left_area[0] + right_area[2] - 10
                        ysize 38
                        xadjustment ui.adjustment(ranged=store.mas_ui.twopane_menu_adj_ranged_callback)
            
                        input:
                            id "search_input"
                            style_prefix "input"
                            length 50
                            default_focus True
                            xalign 0.0
                            layout "nobreak"
                            first_indent (0 if flt_evs is None else 10)
            
                            changed store.mas_ui.twopane_menu_search_callback
                            
                else:
                    button:
                        xfill True
                        yfill True
                        background None
                        padding (0, 0)
                        action SetScreenVariable("is_search_active", True)

                        text "Buscar una conversación...":
                            text_align 0.0
                            layout "nobreak"
                            color "#EEEEEEB2"
                            first_indent 10
                            line_leading 1
                            outlines []

                if flt_evs is None and is_search_active:
                    text "Buscar una conversación...":
                        text_align 0.0
                        layout "nobreak"
                        color "#EEEEEEB2"
                        first_indent 10
                        line_leading 1
                        outlines []


screen scrollable_menu(items, display_area, scroll_align, nvm_text, remove=None):
    style_prefix "scrollable_menu"

    fixed at android_screen_fade:
        area display_area

        vbox:
            ypos 0
            yanchor 0

            viewport:
                id "scrollable_menu_viewport"
                yadjustment store.mas_scrollable_menu_adj
                yfill False
                mousewheel True

                has vbox
                for i_caption, i_label in items:
                    $ button_text = i_caption
                    if not button_text:
                        $ ev = store.mas_all_ev_db.get(i_label, None)
                        if ev and ev.prompt:
                            $ button_text = ev.prompt
                        else:
                            $ button_text = i_label
                    
                    textbutton "[button_text]":
                        text_style "scrollable_menu_button_text"
                        if renpy.has_label(i_label) and not seen_event(i_label):
                            style "scrollable_menu_new_button"

                        elif not renpy.has_label(i_label):
                            style "scrollable_menu_special_button"

                        action Return(i_label)

            null height 20

            if remove:

                textbutton _(remove[0]) action Return(remove[1])

            textbutton _(nvm_text) action Return(False)

        bar:
            style "classroom_vscrollbar"
            value YScrollValue("scrollable_menu_viewport")
            unscrollable "hide"
            xalign scroll_align

screen mas_gen_scrollable_menu(items, display_area, scroll_align, *args):
    style_prefix "scrollable_menu"

    fixed at android_screen_fade:
        area display_area

        vbox:
            ypos 0
            yanchor 0

            viewport:
                id "mas_gen_viewport"
                yfill False
                mousewheel True

                has vbox
                for item_prompt, item_value, is_italic, is_bold in items:
                    $ button_text = item_prompt
                    if not button_text:
                        $ ev = store.mas_all_ev_db.get(item_value, None)
                        if ev and ev.prompt:
                            $ button_text = ev.prompt
                        else:
                            $ button_text = item_value

                    textbutton "[button_text]":
                        text_style "scrollable_menu_button_text"
                        if is_italic and is_bold:
                            style "scrollable_menu_crazy_button"

                        elif is_italic:
                            style "scrollable_menu_new_button"

                        elif is_bold:
                            style "scrollable_menu_special_button"

                        xsize display_area[2]
                        action Return(item_value)

            for final_items in args:
                if final_items[4] > 0:
                    null height final_items[4]

                textbutton _(final_items[0]):
                    if final_items[2] and final_items[3]:
                        style "scrollable_menu_crazy_button"

                    elif final_items[2]:
                        style "scrollable_menu_new_button"

                    elif final_items[3]:
                        style "scrollable_menu_special_button"

                    xsize display_area[2]
                    action Return(final_items[1])

        bar:
            style "classroom_vscrollbar"
            value YScrollValue("mas_gen_viewport")
            unscrollable "hide"
            xalign scroll_align

screen mas_check_scrollable_menu(items, display_area, scroll_align, selected_button_prompt="Hecho", default_button_prompt="No importa", return_all=False):
    default buttons_data = {
        _tuple[1]: {
            "return_value": _tuple[3] if _tuple[2] else _tuple[4],
            "true_value": _tuple[3],
            "false_value": _tuple[4]
        }
        for _tuple in items
    }

    style_prefix "check_scrollable_menu"

    fixed at android_screen_fade:
        area display_area

        vbox:
            ypos 0
            yanchor 0

            viewport:
                id "check_scrollable_viewport"
                yfill False
                mousewheel True

                has vbox
                for button_prompt, button_key, start_selected, true_value, false_value in items:
                    textbutton button_prompt:
                        selected buttons_data[button_key]["return_value"] == buttons_data[button_key]["true_value"]
                        xsize display_area[2]
                        action ToggleDict(
                                buttons_data[button_key],
                                "return_value",
                                true_value,
                                false_value
                            )

            null height 20

            textbutton store.mas_ui.check_scr_menu_choose_prompt(buttons_data, selected_button_prompt, default_button_prompt):
                style "scrollable_menu_button"
                xsize display_area[2]
                action Function(
                    store.mas_ui.check_scr_menu_return_values,
                    buttons_data,
                    return_all
                )

        bar:
            style "classroom_vscrollbar"
            value YScrollValue("check_scrollable_viewport")
            unscrollable "hide"
            xalign scroll_align

screen music_menu(music_page, page_num=0, more_pages=False):
    modal True
    $ import store.songs as songs

    if songs.current_track is None:
        $ return_value = songs.NO_SONG
    else:
        $ return_value = songs.current_track

    # Acciones con transicion forzada (0.5s)
    key "noshift_M" action [Function(renpy.transition, Dissolve(0.5)), Return(return_value)]
    key "noshift_m" action [Function(renpy.transition, Dissolve(0.5)), Return(return_value)]

    zorder 200

    style_prefix "music_menu"

    fixed at android_screen_fade:

        frame:
            style "music_menu_outer_frame"

            hbox:
                frame:
                    style "music_menu_navigation_frame"
                frame:
                    style "music_menu_content_frame"
                    transclude
            vbox:
                style_prefix "music_menu"
                xpos gui.navigation_xpos
                spacing gui.navigation_spacing

                for name,song in music_page:
                    # Transicion al seleccionar cancion (0.5s)
                    textbutton _(name) action [Function(renpy.transition, Dissolve(0.5)), Return(song)]

        vbox:
            yalign 1.0
            hbox:
                if page_num > 0:
                    textbutton _("<<<< Prev"):
                        style "music_menu_prev_button"
                        action Return(page_num - 1)
                else:
                    textbutton _(""):
                        style "music_menu_prev_button"
                        xsize 126
                        sensitive False

                if more_pages:
                    textbutton _("Post >>>>"):
                        style "music_menu_return_button"
                        action Return(page_num + 1)

            textbutton _(songs.NO_SONG):
                style "music_menu_return_button"
                # Transicion al elegir Sin Musica (0.5s)
                action [Function(renpy.transition, Dissolve(0.5)), Return(songs.NO_SONG)]

            textbutton _("Regresar"):
                style "music_menu_return_button"
                # Transicion al Regresar (0.5s)
                action [Function(renpy.transition, Dissolve(0.5)), Return(return_value)]

screen mas_extramenu_area():
    zorder 52

    # Saltamos a nuestro label personalizado
    key "e" action Jump("mas_extra_menu_close_android")
    key "E" action Jump("mas_extra_menu_close_android")

    frame at android_screen_fade:
        area (0, 0, 1280, 720)
        background Solid("#0000007F")

        textbutton _("Cerrar"):
            area (60, 596, 120, 35)
            style "hkb_button"
            # Saltamos a nuestro label personalizado
            action Jump("mas_extra_menu_close_android")

        frame:
            area (195, 450, 80, 255)
            style "mas_extra_menu_frame"
            has vbox:
                spacing 2
            label "Zoom":
                text_style "mas_extra_menu_label_text"
                xalign 0.5


            textbutton _("Reset"):
                style "mas_adjustable_button"
                selected False
                xsize 72
                ysize 35
                xalign 0.3
                action SetField(store.mas_sprites, "zoom_level", store.mas_sprites.default_zoom_level)


            bar value FieldValue(store.mas_sprites, "zoom_level", store.mas_sprites.max_zoom):
                style "mas_adjust_vbar"
                xalign 0.5
            $ store.mas_sprites.adjust_zoom()


# 2. Navegación (sidebar)
screen navigation():
    style_prefix "navigation"
    
    if main_menu:
        vbox:
            xpos gui.navigation_xpos
            yalign 0.8
            spacing gui.navigation_spacing

            if main_menu:
                textbutton _("Solo Monika") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Por favor introduce tu nombre", ok_action=Function(FinishEnterName)))
            else:
                textbutton _("Historial") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]
                textbutton _("Guardar juego") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]

            textbutton _("Cargar juego") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]

            if _in_replay:
                textbutton _("Terminar repetición") action EndReplay(confirm=True)
            elif not main_menu:
                textbutton _("Menú principal") action NullAction(), Show(screen="dialog", message="No necesitas volver allí.\nTerminarás volviendo aquí, así que no te preocupes.", ok_action=Hide("dialog"))

            textbutton _("Ajustes") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]

            if store.mas_submod_utils.submod_map:
                textbutton _("Submods") action [ShowMenu("submods"), SensitiveIf(renpy.get_screen("submods") == None)]

            if store.mas_windowreacts.can_show_notifs and not main_menu:
                textbutton _("Alertas") action [ShowMenu("notif_settings"), SensitiveIf(renpy.get_screen("notif_settings") == None)]

            if store.mas_api_keys.has_features():
                textbutton _("API Keys") action [ShowMenu("mas_apikeys"), SensitiveIf(renpy.get_screen("mas_apikeys") == None)]

            if renpy.variant("pc") and not renpy.mobile:
                textbutton _("Atajos") action [ShowMenu("hot_keys"), SensitiveIf(renpy.get_screen("hot_keys") == None)]

            if renpy.variant("pc") or renpy.mobile:
                textbutton _("Ayuda") action OpenURL("https://github.com/Monika-After-Story/MonikaModDev/wiki")
                textbutton _("Salir") action Quit(confirm=(None if main_menu else _confirm_quit))

            if not main_menu:
                textbutton _("Regresar") action Return()

    else:
        vbox at android_screen_fade:
            xpos gui.navigation_xpos
            yalign 0.8
            spacing gui.navigation_spacing

            if main_menu:
                textbutton _("Solo Monika") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Por favor introduce tu nombre", ok_action=Function(FinishEnterName)))
            else:
                textbutton _("Historial") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]
                textbutton _("Guardar juego") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]

            textbutton _("Cargar juego") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]

            if _in_replay:
                textbutton _("Terminar repetición") action EndReplay(confirm=True)
            elif not main_menu:
                textbutton _("Menú principal") action NullAction(), Show(screen="dialog", message="No necesitas volver allí.\nTerminarás volviendo aquí, así que no te preocupes.", ok_action=Hide("dialog"))

            textbutton _("Ajustes") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]

            if store.mas_submod_utils.submod_map:
                textbutton _("Submods") action [ShowMenu("submods"), SensitiveIf(renpy.get_screen("submods") == None)]

            if store.mas_windowreacts.can_show_notifs and not main_menu:
                textbutton _("Alertas") action [ShowMenu("notif_settings"), SensitiveIf(renpy.get_screen("notif_settings") == None)]

            if store.mas_api_keys.has_features():
                textbutton _("API Keys") action [ShowMenu("mas_apikeys"), SensitiveIf(renpy.get_screen("mas_apikeys") == None)]

            if renpy.variant("pc") and not renpy.mobile:
                textbutton _("Atajos") action [ShowMenu("hot_keys"), SensitiveIf(renpy.get_screen("hot_keys") == None)]

            if renpy.variant("pc") or renpy.mobile:
                textbutton _("Ayuda") action OpenURL("https://github.com/Monika-After-Story/MonikaModDev/wiki")
                textbutton _("Salir") action Quit(confirm=(None if main_menu else _confirm_quit))

            if not main_menu:
                textbutton _("Regresar") action Return()

# 3. Game Menu
screen game_menu(title, scroll=None):

    key "noshift_T" action NullAction()
    key "noshift_t" action NullAction()
    key "noshift_M" action NullAction()
    key "noshift_m" action NullAction()
    key "noshift_P" action NullAction()
    key "noshift_p" action NullAction()
    key "noshift_E" action NullAction()
    key "noshift_e" action NullAction()


    if main_menu:
        add gui.main_menu_background
    else:
        key "mouseup_3" action Return()
        add gui.game_menu_background

    style_prefix "game_menu"

    frame at android_screen_fade:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    yinitial 1.0

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial 1.0

                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    label title style "game_menu_label"

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

# 4. Dialogos / Confirmaciones
screen confirm(message, yes_action, no_action):

    modal True

    zorder 200

    style_prefix "confirm"
    add mas_getTimeFile("gui/overlay/confirm.png")

    frame at android_screen_fade:
        has vbox:
            xalign .5
            yalign .5
            spacing 30

        if in_sayori_kill and message == layout.QUIT:
            add "confirm_glitch" xalign 0.5

        else:
            label _(message):
                style "confirm_prompt"
                xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            if mas_in_finalfarewell_mode:
                textbutton _("-") action yes_action
                textbutton _("-") action yes_action
            else:
                textbutton _("Sí") action [SetField(persistent, "_mas_game_crashed", False), Show(screen="quit_dialog", message=layout.QUIT_YES, ok_action=yes_action)]
                textbutton _("No") action no_action, Show(screen="dialog", message=layout.QUIT_NO, ok_action=Hide("dialog"))

screen dialog(message, ok_action):

    modal True

    zorder 200

    style_prefix "confirm"
    add mas_getTimeFile("gui/overlay/confirm.png")

    frame at android_screen_fade:
        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action
