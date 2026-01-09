python early:
    import os
    
    """
    [ANDROID] FORCE SAVE PATH - EARLY INIT
    Executes before ANY init block to override Ren'Py's default save location detection.
    This ensures config.savedir is set to our custom "Backpack" path immediately.
    """
    is_android = renpy.android or "ANDROID_ARGUMENT" in os.environ or "ANDROID_PRIVATE" in os.environ
    
    if is_android:
        """
        [CRITICAL FIX] DISABLE AUTO-PATH
        We set this to None so Ren'Py stops trying to be 'smart' with the project name
        and forces it to respect our custom config.savedir below.
        This fixes the 'Overwrite/Ignore' bug.
        """
        config.save_directory = None
        
        """
        [CRITICAL FIX] FORCE SAVE PATH
        We explicitly set config.savedir to our custom path.
        This ensures Ren'Py uses our Backpack path instead of the default internal path.
        """
        config.savedir = "/storage/emulated/0/Monika After Story/game/saves"
        
        """
        [CRITICAL FIX] CREATE SAVES DIRECTORY
        We explicitly create the saves directory right now (aggressive creation).
        This ensures Ren'Py has a valid directory to write to, even if it's empty.
        """
        try:
            if not os.path.exists(config.savedir):
                os.makedirs(config.savedir)
        except:
            pass

init -999 python:
    import os
    import shutil
    import platform

    """
    CONSTANTES DE RUTAS
    """
    ANDROID_BACKPACK_PATH = "/storage/emulated/0/Monika After Story/"
    
    """
    Subdirectorios críticos
    """
    ANDROID_CHARACTERS_PATH = os.path.join(ANDROID_BACKPACK_PATH, "characters/")
    ANDROID_CHESS_PATH = os.path.join(ANDROID_BACKPACK_PATH, "chess_games/")
    ANDROID_LOG_PATH = os.path.join(ANDROID_BACKPACK_PATH, "log/")
    ANDROID_SAVES_PATH = os.path.join(ANDROID_BACKPACK_PATH, "game/saves/")
    ANDROID_CUSTOM_BGM_PATH = os.path.join(ANDROID_BACKPACK_PATH, "custom_bgm/")
    
    """
    Función de creación agresiva
    """
    def mas_android_setup_backpack():
        if not renpy.android:
            return

        dirs_to_create = [
            ANDROID_BACKPACK_PATH,
            ANDROID_CHARACTERS_PATH,
            ANDROID_CHESS_PATH,
            ANDROID_LOG_PATH,
            ANDROID_SAVES_PATH,
            ANDROID_CUSTOM_BGM_PATH,
            os.path.join(ANDROID_BACKPACK_PATH, "game/mod_assets/location/"),
            os.path.join(ANDROID_BACKPACK_PATH, "game/mod_assets/thumbs/"),
            os.path.join(ANDROID_BACKPACK_PATH, "game/mod_assets/monika/"),
            os.path.join(ANDROID_BACKPACK_PATH, "game/mod_assets/monika/a/"),
            os.path.join(ANDROID_BACKPACK_PATH, "game/mod_assets/monika/c/"),
            os.path.join(ANDROID_BACKPACK_PATH, "game/mod_assets/monika/f/"),
            os.path.join(ANDROID_BACKPACK_PATH, "game/mod_assets/monika/h/"),
            os.path.join(ANDROID_BACKPACK_PATH, "game/mod_assets/monika/j/"),
            os.path.join(ANDROID_BACKPACK_PATH, "game/mod_assets/monika/t/"),
            os.path.join(ANDROID_BACKPACK_PATH, "game/submods/")
        ]

        print("[ANDROID_SETUP] Iniciando creación agresiva de directorios...")
        for d in dirs_to_create:
            if not os.path.exists(d):
                try:
                    os.makedirs(d)
                    print("[ANDROID_SETUP] Creado: " + d)
                except Exception as e:
                    print("[ANDROID_SETUP] Error creando " + d + ": " + str(e))
            else:
                pass
    
    mas_android_setup_backpack()

init python:
    """
    OPTIMIZACIÓN JNI
    Usamos try-except para evitar el crash si una clase no existe en tu versión de Ren'Py.
    """
    if renpy.android:
        from jnius import autoclass
        
        """
        Clases Estándar
        """
        _Environment = autoclass('android.os.Environment')
        _Intent = autoclass('android.content.Intent')
        _Settings = autoclass('android.provider.Settings')
        _Uri = autoclass('android.net.Uri')
        _VERSION = autoclass('android.os.Build$VERSION')
        _PackageManager = autoclass('android.content.pm.PackageManager')

        """
        Clases de Actividad (Carga Segura)
        """
        _PythonSDLActivity = None
        try:
            _PythonSDLActivity = autoclass('org.renpy.android.PythonSDLActivity')
        except:
            pass
            
        _PythonActivity = None
        try:
            _PythonActivity = autoclass('org.renpy.android.PythonActivity')
        except:
            pass
    
    def mas_get_current_activity():
        if not renpy.android: return None
        
        act = None
        """
        Intentamos obtener la actividad de las clases que logramos cargar
        """
        if _PythonSDLActivity:
            try: act = _PythonSDLActivity.mActivity
            except: pass
            
        if act is None and _PythonActivity:
            try: act = _PythonActivity.mActivity
            except: pass
            
        return act

    """
    PERMISOS UNIVERSALES
    """
    def mas_android_check_and_request_permissions():
        if not renpy.android: return
            
        CurrentActivity = mas_get_current_activity()
        if CurrentActivity is None: return

        sdk_int = _VERSION.SDK_INT
        
        """
        1. Almacenamiento (Directo)
        """
        if sdk_int >= 30:
            if not _Environment.isExternalStorageManager():
                try:
                    intent = _Intent(_Settings.ACTION_MANAGE_APP_ALL_FILES_ACCESS_PERMISSION)
                    package_uri = _Uri.parse("package:" + CurrentActivity.getPackageName())
                    intent.setData(package_uri)
                    CurrentActivity.startActivity(intent)
                except: pass
        else:
            CurrentActivity.requestPermissions([
                "android.permission.WRITE_EXTERNAL_STORAGE",
                "android.permission.READ_EXTERNAL_STORAGE"
            ], 102)

        """
        2. Notificaciones (Simultáneo para efecto glitch)
        """
        if sdk_int >= 33:
            CurrentActivity.requestPermissions(["android.permission.POST_NOTIFICATIONS"], 101)


    """
    AJEDREZ UNIVERSAL
    """
    def mas_android_install_stockfish():
        if not renpy.android:
            return

        try:
            arch = platform.machine()
            binary_name = "stockfish-android-armv7"
            if "aarch64" in arch or "armv8" in arch:
                binary_name = "stockfish-android-arm64-v8a"
            
            """
            Estrategia de Escaneo
            """
            found_path = None
            all_files = renpy.list_files()
            
            for f in all_files:
                if f.endswith(binary_name):
                    found_path = f
                    break
            
            if not found_path:
                print("[ANDROID_CHESS] ERROR CRÍTICO: No se encontró " + binary_name + " en ningún lugar de los assets.")
                return

            print("[ANDROID_CHESS] Binario encontrado en: " + found_path)

            """
            Instalación
            """
            private_dir = os.environ.get('ANDROID_PRIVATE', '')
            dest_dir = os.path.join(private_dir, "files")
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            
            dest_path = os.path.join(dest_dir, "stockfish_android")

            try:
                # Lectura directa del asset encontrado
                file_handle = renpy.file(found_path)
                with open(dest_path, "wb") as out_file:
                    out_file.write(file_handle.read())
                file_handle.close()
                
                os.chmod(dest_path, 0o755)
                print("[ANDROID_CHESS] Stockfish instalado correctamente en: " + dest_path)
            except Exception as e:
                print("[ANDROID_CHESS] Error escribiendo archivo: " + str(e))

        except Exception as e:
            print("[ANDROID_CHESS] Excepción general instalando Stockfish: " + str(e))

    mas_android_install_stockfish()

    def mas_android_has_permission():
        """
        CHECKER OPTIMIZADO

        Verifica si la aplicación tiene los permisos necesarios de almacenamiento
        según la versión de Android.

        RETURNS:
            True si tiene permisos, False si no.
        """
        if not renpy.android: return True
        try:
            CurrentActivity = mas_get_current_activity()
            if _VERSION.SDK_INT >= 30:
                return _Environment.isExternalStorageManager()
            else:
                res = CurrentActivity.checkSelfPermission("android.permission.WRITE_EXTERNAL_STORAGE")
                return res == _PackageManager.PERMISSION_GRANTED
        except:
            return False


init 50 python:
    """
    OVERRIDES AGRESIVOS (Monkey Patching)

    Modificaciones en tiempo de ejecución para redirigir subsistemas
    a las rutas de "La Mochila".
    """
    if renpy.android:
        """
        VÁLVULA DE SEGURIDAD

        Solo redirigimos SI tenemos permisos. Esto evita el crash del OLD
        si se intenta escribir antes de tiempo.
        """
        if mas_android_has_permission():
            
            if hasattr(store, 'songs'):
                pass

            if hasattr(store, 'mas_chess'):
                store.mas_chess.CHESS_SAVE_PATH = ANDROID_CHESS_PATH
                
                """
                Redirigir binario de Stockfish a almacenamiento interno ejecutable
                """
                private_dir = os.environ.get('ANDROID_PRIVATE', '')
                store.mas_chess.STOCKFISH_PATH = os.path.join(private_dir, "files", "stockfish_android")
                
                print("[ANDROID_OVERRIDES] Chess Save Path & Binary redirected")
            
            if hasattr(store, 'mas_docking_station'):
                store.mas_docking_station.station = ANDROID_CHARACTERS_PATH
                if not os.path.isdir(ANDROID_CHARACTERS_PATH):
                    try:
                        os.makedirs(ANDROID_CHARACTERS_PATH)
                    except:
                        pass
                print("[ANDROID_OVERRIDES] Docking Station redirected")

            """
            Logging Override
            """
            import logging.handlers
            root_logger = logging.getLogger()
            for h in root_logger.handlers[:]:
                root_logger.removeHandler(h)
                h.close()
            
            try:
                log_file = os.path.join(ANDROID_LOG_PATH, "mas_log.txt")
                hdlr = logging.handlers.RotatingFileHandler(
                    log_file, 
                    maxBytes=getattr(store.mas_logging, "MAX_LOG_SIZE", 5242880), 
                    backupCount=getattr(store.mas_logging, "BACKUP_COUNT", 5)
                )
                formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
                hdlr.setFormatter(formatter)
                root_logger.addHandler(hdlr)
                print("[ANDROID_OVERRIDES] Logging redirected")

                # --- EXTRA MODULE LOGS REDIRECTION ---
                # List of specific MAS loggers to redirect to the external log folder
                extra_loggers = ["aff_log", "pnm", "submod_log", "spj", "mfgen"]
                
                for log_name in extra_loggers:
                    try:
                        # Get the specific logger
                        tgt_log = logging.getLogger(log_name)
                        
                        # Remove existing handlers to avoid duplication/internal writing
                        for h in tgt_log.handlers[:]:
                            tgt_log.removeHandler(h)
                            h.close()
                        
                        # create new handler pointing to backpack
                        # We use .txt for mobile readability
                        l_file = os.path.join(ANDROID_LOG_PATH, log_name + ".txt")
                        
                        l_hdlr = logging.handlers.RotatingFileHandler(
                            l_file,
                            maxBytes=getattr(store.mas_logging, "MAX_LOG_SIZE", 5242880),
                            backupCount=getattr(store.mas_logging, "BACKUP_COUNT", 5)
                        )
                        
                        # Use same formatter
                        l_hdlr.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
                        
                        tgt_log.addHandler(l_hdlr)
                        print("[ANDROID_OVERRIDES] Redirected extra logger: " + log_name)
                        
                    except Exception as e:
                        print("[ANDROID_OVERRIDES] Failed to redirect " + log_name + ": " + str(e))

            except Exception as e:
                print("[ANDROID_OVERRIDES] Logging Redirect Error: " + str(e))
        
            print("[ANDROID_OVERRIDES] Permisos no detectados. Usando rutas internas para evitar crash.")

    def mas_android_rescue_logs():
        """
        LOG RESCUE
        Checks for crash logs (traceback.txt) or system logs (log.txt) in the internal
        private directory and copies them to the external backpack for user visibility.
        """
        if not renpy.android:
            return

        try:
            private_dir = os.environ.get('ANDROID_PRIVATE', '')
            # Ren'Py usually dumps traceback.txt in the base files dir or game dir
            internal_files_dir = os.path.join(private_dir, "files")
            
            logs_to_rescue = ["traceback.txt", "log.txt"]
            
            for log_file in logs_to_rescue:
                src_path = os.path.join(internal_files_dir, log_file)
                
                # Destination: Root of Backpack for traceback, or Log folder? 
                # User requested: "traceback.txt (informe de fallos) y log.txt (registro de Ren'Py) aparezcan en la raíz de la carpeta externa"
                dst_path = os.path.join(ANDROID_BACKPACK_PATH, log_file)
                
                if os.path.exists(src_path):
                    try:
                        shutil.copy2(src_path, dst_path)
                        print("[ANDROID_RESCUE] Rescued log: " + log_file)
                        
                        # Optional: Verify copy size?
                    except Exception as e:
                        print("[ANDROID_RESCUE] Failed to copy " + log_file + ": " + str(e))
                        
        except Exception as e:
            print("[ANDROID_RESCUE] Error processing log rescue: " + str(e))

    # Call log rescue immediately after definition
    mas_android_rescue_logs()

    def mas_android_rescue_saves():
        """
        SAVE RESCUE
        
        Intenta recuperar partidas guardadas en la ruta interna privada
        y las mueve a la ruta externa pública.
        """
        if not renpy.android:
            return
        if config.savedir != ANDROID_SAVES_PATH:
            return
        try:
            private_dir = os.environ.get('ANDROID_PRIVATE', '')
            internal_saves = os.path.join(private_dir, "files/saves")
            if os.path.exists(internal_saves):
                files_found = os.listdir(internal_saves)
                if not files_found:
                    return
                for f in files_found:
                    src = os.path.join(internal_saves, f)
                    dst = os.path.join(ANDROID_SAVES_PATH, f)
                    if os.path.isfile(src):
                        if not os.path.exists(dst):
                            try:
                                shutil.copy2(src, dst)
                            except:
                                pass
        except Exception as e:
            pass

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc