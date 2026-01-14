init -1 python:
    """
    Android Notification Submod - UI SCREENS
    
    This file overrides the default 'navigation', 'preferences' and 'notif_settings' screens
    to integrate the Android Notification Submod controls.
    
    WE PERFORM "GHOST REPLACEMENT": Hiding original elements and showing ours in their place.
    """

init python:
    store.MAS_TT_ANDROID_NOTIF = _(
        "Habilita el sistema de notificaciones de Android. Monika podrá enviarte mensajes cuando no estés en el juego."
    )
    store.MAS_TT_ANDROID_SOUND = _(
        "Activa el sonido y vibración para las notificaciones de Monika."
    )
    store.MAS_TT_ANDROID_CALENDAR = _(
        "Habilita notificaciones especiales en fechas importantes y festividades."
    )
    store.MAS_TT_ANDROID_WND_REACT = _(
        "Añade botones interactivos a las notificaciones. Úsalos para responder a Monika y mejorar tu afecto."
    )
    store.MAS_TT_ANDROID_FREQ = _(
        "Ajusta cuánto tiempo debe esperar Monika antes de enviarte un mensaje si no la has visitado."
    )

    # Frequency Map for UI Display
    store.mas_android_freq_map = {
        1: _("Pasiva (3 min)"),
        2: _("Normal (2 min)"),
        3: _("Atenta (1 min)"),
        4: _("Intensa (30s)"),
        5: _("Posesiva (15s)")
    }

    # Safety check to fix corrupted persistent data (e.g., if it was set to 6 due to bug)
    if persistent.mas_android_frequency_index > 5:
        persistent.mas_android_frequency_index = 5

"""
OVERRIDE: NAVIGATION SCREEN
Modified to replace the 'Alertas' button action.
"""
screen navigation():
    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.8

        spacing gui.navigation_spacing


        if main_menu:

            textbutton _("Nuevo Juego") action Start()

            textbutton _("Cargar Juego") action ShowMenu("load")

        else:

            textbutton _("Historia") action ShowMenu("history")

            textbutton _("Guardar Juego") action ShowMenu("save")

            textbutton _("Cargar Juego") action ShowMenu("load")

        if store.mas_submod_utils.submod_map:
            textbutton _("Submods") action [ShowMenu("submods"), SensitiveIf(renpy.get_screen("submods") == None)]

        # REPLACEMENT: Alertas Button
        # Original condition: if store.mas_windowreacts.can_show_notifs and not main_menu:
        # New condition: Show if not main menu (allows access to our submod settings)
        if not main_menu:
            textbutton _("Alertas") action [ShowMenu("notif_settings"), SensitiveIf(renpy.get_screen("notif_settings") == None)]

        if store.mas_api_keys.has_features():
            textbutton _("API") action ShowMenu("mas_api_settings")


        textbutton _("Ajustes") action ShowMenu("preferences")

        if not main_menu:
            textbutton _("Atajos") action ShowMenu("hot_keys")

        if main_menu:
            textbutton _("Ayuda") action OpenURL("https://github.com/Monika-After-Story/MonikaModDev/wiki")

        textbutton _("Salir") action Quit(confirm=(None if main_menu else _confirm_quit))

        if not main_menu:
            textbutton _("Regresar") action Return()


"""
OVERRIDE: PREFERENCES SCREEN (SETTINGS)
Modified to replace the 'Notificaciones' button.
"""
screen preferences():
    tag menu


    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    default tooltip = Tooltip("")

    use game_menu(_("Ajustes"), scroll="viewport"):

        vbox:
            xoffset 50

            hbox:
                box_wrap True

                if True:

                    vbox:
                        style_prefix "generic_fancy_check"
                        label _("Pantalla")
                        textbutton _("Pantalla completa") action Preference("display", "fullscreen")

                    vbox:
                        style_prefix "generic_fancy_check"
                        label _("Gráficos")


                        if False:
                            textbutton _("Cambiar render"):
                                style "check_button"
                                action Function(renpy.call_in_new_context, "mas_gmenu_start")

                        textbutton _("Sin animación") action ToggleField(persistent, "_mas_disable_animations")


                        textbutton _("UI: Modo noche"):
                            action [Function(mas_settings._ui_change_wrapper, persistent._mas_dark_mode_enabled), Function(mas_settings._dark_mode_toggle)]
                            selected persistent._mas_dark_mode_enabled
                        textbutton _("UI: Ciclo D/N"):
                            action [Function(mas_settings._ui_change_wrapper, mas_current_background.isFltDay()), Function(mas_settings._auto_mode_toggle)]
                            selected persistent._mas_auto_mode_enabled


                    vbox:
                        style_prefix "generic_fancy_check"
                        label _("Juego")
                        if False:
                            if persistent._mas_unstable_mode:
                                if store.mas_utils.is_ver_stable(config.version):
                                    textbutton _("Instable"):
                                        action SetField(persistent, "_mas_unstable_mode", False)
                                        selected persistent._mas_unstable_mode
                                else:
                                    textbutton _("Instable"):
                                        style "generic_fancy_check_button_disabled"
                                        text_style "generic_fancy_check_button_disabled_text"
                                        action SetField(persistent, "_mas_unstable_mode", True)
                                        selected True
                                        hovered tooltip.Action(layout.MAS_TT_UNSTABLE_DISABLED)

                            else:
                                textbutton _("Instable"):
                                    action [Show(screen="dialog", message=layout.UNSTABLE, ok_action=Hide(screen="dialog")), SetField(persistent, "_mas_unstable_mode", True)]
                                    selected persistent._mas_unstable_mode
                                    hovered tooltip.Action(layout.MAS_TT_UNSTABLE)

                        textbutton _("Repetir diálogos"):
                            action ToggleField(persistent,"_mas_enable_random_repeats", True, False)
                            hovered tooltip.Action(layout.MAS_TT_REPEAT)



                    vbox:
                        style_prefix "generic_fancy_check"
                        label _(" ")

                        # REPLACEMENT: Notifications Button
                        # Original: Linked to _mas_windowreacts_windowreacts_enabled
                        # New: Linked to persistent.mas_android_notif_enabled
                        textbutton _("Notificaciones"):
                            action ToggleField(persistent, "mas_android_notif_enabled", True, False)
                            hovered tooltip.Action(store.MAS_TT_ANDROID_NOTIF)


            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True


                python:

                    if mas_randchat_prev != persistent._mas_randchat_freq:
                        
                        mas_randchat.adjustRandFreq(
                            persistent._mas_randchat_freq
                        )


                    rc_display = mas_randchat.getRandChatDisp(
                        persistent._mas_randchat_freq
                    )


                    store.mas_randchat_prev = persistent._mas_randchat_freq



                    if mas_suntime.change_state == mas_suntime.RISE_CHANGE:
                        
                        
                        if mas_suntime.sunrise > mas_suntime.sunset:
                            
                            mas_suntime.sunset = mas_suntime.sunrise
                        
                        if mas_sunrise_prev == mas_suntime.sunrise:
                            
                            mas_suntime.change_state = mas_suntime.NO_CHANGE
                        
                        mas_sunrise_prev = mas_suntime.sunrise

                    elif mas_suntime.change_state == mas_suntime.SET_CHANGE:
                        
                        
                        if mas_suntime.sunset < mas_suntime.sunrise:
                            
                            mas_suntime.sunrise = mas_suntime.sunset
                        
                        if mas_sunset_prev == mas_suntime.sunset:
                            
                            mas_suntime.change_state = mas_suntime.NO_CHANGE
                        
                        mas_sunset_prev = mas_suntime.sunset
                    else:
                        
                        
                        if mas_sunrise_prev != mas_suntime.sunrise:
                            mas_suntime.change_state = mas_suntime.RISE_CHANGE
                        
                        elif mas_sunset_prev != mas_suntime.sunset:
                            mas_suntime.change_state = mas_suntime.SET_CHANGE
                        
                        
                        mas_sunrise_prev = mas_suntime.sunrise
                        mas_sunset_prev = mas_suntime.sunset



                    persistent._mas_sunrise = mas_suntime.sunrise * 5
                    persistent._mas_sunset = mas_suntime.sunset * 5
                    sr_display = mas_cvToDHM(persistent._mas_sunrise)
                    ss_display = mas_cvToDHM(persistent._mas_sunset)

                vbox:

                    hbox:
                        label _("Amanecer  ")


                        label _("[[ " + sr_display + " ]")

                    bar value FieldValue(mas_suntime, "sunrise", range=mas_max_suntime, style="slider")


                    hbox:
                        label _("Atardecer  ")


                        label _("[[ " + ss_display + " ]")

                    bar value FieldValue(mas_suntime, "sunset", range=mas_max_suntime, style="slider")


                vbox:

                    hbox:
                        label _("Charla al azar  ")


                        label _("[[ " + rc_display + " ]")

                    bar value FieldValue(
                        persistent,
                        "_mas_randchat_freq",
                        range=store.mas_affection.RANDCHAT_RANGE_MAP[mas_curr_affection],
                        style="slider"
                    )

                    hbox:
                        label _("Volumen del ambiente")

                    bar value Preference("mixer amb volume")


                vbox:

                    label _("Velocidad de texto")


                    bar value FieldValue(_preferences, "text_cps", range=170, max_is_zero=False, style="slider", offset=30)

                    label _("Velocidad de texto automático")

                    bar value Preference("auto-forward time")

                vbox:
                    label _("Volumen de la música")
                    hbox:
                        bar value Preference("music volume")

                    label _("Volumen del sonido")
                    hbox:
                        bar value Preference("sound volume")


                    null height gui.pref_spacing

                    textbutton _("Silenciar todo"):
                        style "generic_fancy_check_button"
                        action Preference("all mute", "toggle")


            hbox:

                if False:
                    if not main_menu:
                        textbutton _("Actualizar la versión"):
                            action Function(renpy.call_in_new_context, 'forced_update_now')
                            style "navigation_button"

                    textbutton _("Importar datos de DDLC"):
                        action Function(renpy.call_in_new_context, 'import_ddlc_persistent_in_settings')
                        style "navigation_button"


    text tooltip.value:
        xalign 0.0 yalign 1.0
        xoffset 300 yoffset -10
        style "main_menu_version"




    text "v[config.version]":
        xalign 1.0 yalign 0.0
        xoffset -10
        style "main_menu_version"


"""
OVERRIDE: NOTIF SETTINGS SCREEN (ALERTAS)
Modified to replace the content with Android Submod settings.
"""
screen notif_settings():
    tag menu

    use game_menu(("Alertas"), scroll="viewport"):

        default tooltip = Tooltip("")

        vbox:
            style_prefix "generic_fancy_check"
            hbox:
                spacing 25
                # REPLACEMENT: Use Notifications
                # Original: _mas_enable_notifications
                # New: mas_android_notif_enabled
                textbutton _("Usar notificaciones"):
                    action ToggleField(persistent, "mas_android_notif_enabled")
                    selected persistent.mas_android_notif_enabled
                    hovered tooltip.Action(store.MAS_TT_ANDROID_NOTIF)

                # REPLACEMENT: Sounds
                # Original: _mas_notification_sounds
                # New: mas_android_notif_sound
                textbutton _("Sonidos"):
                    action ToggleField(persistent, "mas_android_notif_sound")
                    selected persistent.mas_android_notif_sound
                    hovered tooltip.Action(store.MAS_TT_ANDROID_SOUND)

            label _("Filtros de alerta")

        hbox:
            style_prefix "generic_fancy_check"
            box_wrap True
            spacing 25

            # REPLACEMENT: Filters
            # Original: Topic Alerts / Window Reactions (from _android_valid_filters logic)
            # New: Calendar Events (Alertas temáticas) / Action Buttons (Reacciones de ventana)
            
            textbutton _("Eventos del Calendario"):
                action ToggleField(persistent, "mas_android_calendar_events")
                selected persistent.mas_android_calendar_events
                hovered tooltip.Action(store.MAS_TT_ANDROID_CALENDAR)

            textbutton _("Respuestas Rápidas"):
                action ToggleField(persistent, "mas_android_action_buttons")
                selected persistent.mas_android_action_buttons
                hovered tooltip.Action(store.MAS_TT_ANDROID_WND_REACT)
        
        null height gui.pref_spacing

        # NEW: Frequency Slider
        vbox:
            style_prefix "slider"
            hbox:
                # Separated labels to prevent font jitter, with xmaximum overrides to prevent wrapping
                label _("Frecuencia") xmaximum None
                label _("[[ " + store.mas_android_freq_map.get(persistent.mas_android_frequency_index, "Error") + " ]") xmaximum None

            bar value FieldValue(persistent, "mas_android_frequency_index", range=4, offset=1, style="slider") hovered tooltip.Action(store.MAS_TT_ANDROID_FREQ)


    text tooltip.value:
        xalign 0 yalign 1.0
        xoffset 300 yoffset -10
        style "main_menu_version"
