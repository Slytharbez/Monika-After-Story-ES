



init -100 python:

    if not renpy.android:
        for archive in ['audio','images','scripts','fonts']:
            if not archive in config.archives:
                
                renpy.error("No se han encontrado los archivos DDLC en la carpeta /game. Compruebe la instalación y vuelva a intentarlo.")





init python:
    menu_trans_time = 1

    splash_message_default = _("Este mod es un trabajo no oficial de un fan, no está afiliado al Equipo Salvato.")
    splash_messages = [
    _("Por favor, apoya a Doki Doki Literature Club! y a Team Salvato."),
    _("Eres mi sol, mi único sol."),
    _("Te extrañé."),
    _("Juega conmigo."),
    _("Es solo un juego, principalmente."),
    _("¿Este juego no es apto para niños ni para los que se alteran fácilmente?"),
    _("sdfasdklfgsdfgsgoinrfoenlvbd"),
    _("null"),
    _("He enviado a los niños al infierno."),
    _("PM murió por esto."),
    _("Fue solo parcialmente tu culpa."),
    _("Este juego no es apto para niños ni para aquellos que se desmembren fácilmente.")

    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)


image menu_logo:
    "mod_assets/menu_new.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move



image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=20, particleTime=2.0, particleXSpeed=6, particleYSpeed=4).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"


label splashscreen:
    
    if renpy.android:
        python:
            """
            Permission Verification

            We check if the utility functions imported from zz_android_setup.rpy exist.
            """
            if "mas_android_has_permission" in globals():
                
                """
                STATE: NO PERMISSIONS
                
                We enter the request and wait flow.
                """
                if not mas_android_has_permission():
                    
                    """
                    1. Request Permissions
                    
                    Launches the JNI request for notifications and storage.
                    This generates the desired superimposed visual behavior.
                    """
                    if "mas_android_check_and_request_permissions" in globals():
                        mas_android_check_and_request_permissions()
                    
                    """
                    2. Wait Loop
                    
                    Pauses the game while the user interacts with
                    system dialogs or the settings screen.
                    """
                    while not mas_android_has_permission():
                        renpy.pause(0.1)
                        
                    """
                    3. Create Folders
                    
                    Once permissions are obtained, we force the immediate creation
                    of the directory structure in external storage.
                    """
                    if "mas_android_setup_public_storage" in globals():
                        mas_android_setup_public_storage()
                    
                    """
                    4. Conditional Reset
                    
                    Controlled closure of the application, depending on the Android version, to force a Ren'Py 
                    reboot and detect the new external storage on the next run.
                    """
                    renpy.quit()
                
                else:
                    """
                    STATE: PERMISSIONS OBTAINED
                    
                    Routine secondary permission verification (Notifications)
                    silently.
                    """
                    if "mas_android_check_and_request_permissions" in globals():
                        mas_android_check_and_request_permissions()

    python:
        if renpy.android:
            try:
                if "mas_android_setup_public_storage" in globals():
                    mas_android_setup_public_storage()
                if "mas_android_rescue_saves" in globals():
                    mas_android_rescue_saves()
                pass
                
                """
                Docking Station Override
                
                Ensures that the "station" path points correctly to
                external storage before starting the game logic.
                """
                if hasattr(store, "mas_docking_station"):
                    store.mas_docking_station.station = "/storage/emulated/0/Monika After Story/characters/"
            except:
                pass

    python:
        _mas_AffStartup()

        persistent.sessions['current_session_start']=datetime.datetime.now()
        persistent.sessions['total_sessions'] = persistent.sessions['total_sessions']+ 1
        store.mas_calendar.loadCalendarDatabase()


        store.mas_sprites.adjust_zoom()


        Event.validateConditionals()

    if store.mas_per_check.should_show_chibika_persistent():

        call mas_backups_you_have_bad_persistent

    scene white


    if persistent.first_run:
        $ quick_menu = False
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        "[config.name] es un mod del Doki Doki Literature Club! que no está afiliado a Team Salvato."
        "Está diseñado para ser jugado solo después de haber completado el juego oficial, ya que contiene spoilers del juego oficial."
        "Para jugar a este mod se necesitan los archivos del juego Doki Doki Literature Club!, pueden descargarse gratuitamente en: http://ddlc.moe."
        menu:
            "Al jugar [config.name] declaras que has completado Doki Doki Literature Club! y aceptas cualquier spoiler que contenga."
            "Estoy de acuerdo":
                pass
        scene tos2
        with Dissolve(1.5)
        pause 1.0

        scene white
        with Dissolve(1.5)


        if not persistent._mas_imported_saves:
            call import_ddlc_persistent from _call_import_ddlc_persistent

        $ persistent.first_run = False



    python:
        basedir = config.basedir.replace("\\", "/")

        if renpy.android:
            try:
                """
                AGRESSIVE FOLDER CREATION - RUNTIME
                
                Directory security fill. Ensures the structure exists even if the user
                manually grants permissions.
                """
                mas_root = "/storage/emulated/0/Monika After Story/"
                dirs_to_force = [
                    mas_root,
                    mas_root + "characters/",
                    mas_root + "chess_games/",
                    mas_root + "log/",
                    mas_root + "game/saves/",
                    mas_root + "custom_bgm/",
                    mas_root + "game/mod_assets/monika/",
                    mas_root + "game/mod_assets/monika/a/",
                    mas_root + "game/mod_assets/monika/c/",
                    mas_root + "game/mod_assets/monika/f/",
                    mas_root + "game/mod_assets/monika/h/",
                    mas_root + "game/mod_assets/monika/j/",
                    mas_root + "game/mod_assets/monika/t/",
                    mas_root + "game/mod_assets/location/",
                    mas_root + "game/mod_assets/thumbs/",
                    mas_root + "game/submods/"
                ]

                import os
                saves_created = False
                
                for d in dirs_to_force:
                    if not os.path.exists(d):
                        try:
                            """
                            Python 2.7 compatibility
                            
                            os.makedirs does not have the 'exist_ok' argument in this version,
                            so we catch the exception if the directory already exists.
                            """
                            os.makedirs(d)
                            """
                            Detection of First Run with Permissions
                            
                            If we create 'game/saves', we mark the flag to
                            restart and use this new location.
                            """
                            if d.endswith("game/saves/"):
                                saves_created = True
                        except:
                            pass
                
                """
                Version file generation (masrun)
                """
                with open(mas_root + "masrun", "w") as versfile:
                    versfile.write(config.name + "|" + config.version + "\n")
                
                """
                Persistent creation
                
                Manual low-level writing of the 'persistent' file.
                
                REASON:
                    Ren'Py caches the save path at startup. If we change
                    config.savedir at runtime, the automatic saving
                    could fail or use the wrong path.
                    
                ACTION:
                    Serializing (pickle) and compressing (zlib) manually the
                    persistent data and writing it directly to disk.
                """
                try:
                    import pickle
                    import zlib
                    ext_saves = mas_root + "game/saves/"
                    ext_persistent_file = ext_saves + "persistent"
                    
                    """
                    Verification to avoid deleting backups
                    """
                    if not os.path.exists(ext_persistent_file):
                        with open(ext_persistent_file, "wb") as f:
                            """
                            CRITICAL: Ren'Py expects a compressed pickle with zlib.
                            If we write raw pickle, it crashes on load (Error -3).
                            Protocol 2 is the standard compatible.
                            """
                            raw_data = pickle.dumps(persistent, protocol=2)
                            compressed_data = zlib.compress(raw_data)
                            f.write(compressed_data)
                            
                        print("Persistent Comprimido 'materializado' en: " + ext_persistent_file)
                    else:
                        print("El persistent ya existe en la ruta externa. No hay cambios para aplicar.")

                except Exception as ep:
                    print("Error en escritura manual de persistent: " + str(ep))
                    
            except Exception as e:
                print("Error creando carpetas runtime: " + str(e))
                pass
        else:
            with open(basedir + "/game/masrun", "w") as versfile:
                versfile.write(config.name + "|" + config.version + "\n")






    if persistent.autoload and not _restart:
        jump autoload

    $ mas_enable_quit()


    $ config.allow_skipping = False


    show white
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.t1
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)

    if renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = False

    python:
        if persistent._mas_auto_mode_enabled:
            mas_darkMode(mas_current_background.isFltDay())
        else:
            mas_darkMode(not persistent._mas_dark_mode_enabled)
    return

label warningscreen:
    hide intro
    show warning
    pause 3.0

label after_load:
    $ config.allow_skipping = False
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    if anticheat != persistent.anticheat:
        stop music
        scene black
        "No se ha podido cargar el archivo de guardado."
        "¿Estás intentando hacer trampa?"

        $ renpy.utter_restart()
    return


label autoload:
    python:

        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history

        _game_menu_screen = "preferences"
        renpy.block_rollback()


        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None


    $ config.keymap["debug_voicing"] = list()
    $ config.keymap["choose_renderer"] = list()


    $ renpy.pop_call()


    if persistent._mas_chess_mangle_all:
        jump mas_chess_go_ham_and_delete_everything

    python:







        store.mas_dockstat.setMoniSize(persistent.sessions["total_playtime"])

        mas_runDelayedActions(MAS_FC_START)

        renpy.start_predict("monika idle")



    jump ch30_autoload

label before_main_menu:
    $ config.main_menu_music = audio.t1
    return

label quit:
    python:
        store.mas_calendar.saveCalendarDatabase(CustomEncoder)
        persistent.sessions['last_session_end']=datetime.datetime.now()
        
        """
        [ANDROID FIX]
        Si cerramos el juego demasiado pronto (ej. Sacrificial Restart), 
        current_session_start puede ser None. Verificamos antes de calcular.
        """
        new_time = persistent.sessions["total_playtime"]
        
        if persistent.sessions.get("current_session_start"):
            today_time = (
                persistent.sessions["last_session_end"]
                - persistent.sessions["current_session_start"]
            )
            new_time = today_time + persistent.sessions["total_playtime"]
            persistent.sessions["total_playtime"] = new_time


        if datetime.timedelta(0) < new_time <= mas_maxPlaytime():
            persistent.sessions['total_playtime'] = new_time


        store.mas_dockstat.setMoniSize(persistent.sessions["total_playtime"])


        store.mas_selspr.save_selectables()


        monika_chr.save()


        store.mas_weather.saveMWData()


        store.mas_background.saveMBGData()


        store.mas_o31_event.removeImages()


        mas_runDelayedActions(MAS_FC_END)
        store.mas_delact.saveDelayedActionMap()

        _mas_AffSave()


        if not persistent._mas_dockstat_going_to_leave:
            store.mas_utils.trydel(mas_docking_station._trackPackage("monika"))


        store.mas_sprites._clear_caches()


        store.mas_xp.grant()


        store.mas_logging.logging.shutdown()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
