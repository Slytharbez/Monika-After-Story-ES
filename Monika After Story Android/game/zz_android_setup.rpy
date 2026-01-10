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

        """
        [CRITICAL FIX] LOGGING DIRECTORY
        Force (renpy) system logs (log.txt) to be written to the Backpack.
        This avoids the need for a 'rescue' operation for the main log.
        """
        try:
            """
            Standard "Monika After Story" root for log.txt to match user request
            """
            _log_path = "/storage/emulated/0/Monika After Story/" 
            if not os.path.exists(_log_path):
                os.makedirs(_log_path)
            
            config.log_directory = _log_path
            
            """
            Ensure logging is enabled even if it was somehow disabled
            """
            config.log_enable = True 
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

        print("Iniciando creación agresiva de directorios...")
        for d in dirs_to_create:
            if not os.path.exists(d):
                try:
                    os.makedirs(d)
                    print("Creado: " + d)
                except Exception as e:
                    print("Error creando " + d + ": " + str(e))
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
    AJEDREZ UNIVERSAL (NATIVE LIB)
    """
    def mas_get_native_lib_dir():
        if not renpy.android:
            return None
            
        try:
            """
            Contexto de la aplicación
            Obtenemos la actividad actual para acceder al contexto y rutas nativas.
            """
            CurrentActivity = mas_get_current_activity()
            if not CurrentActivity:
                return None
                
            context = CurrentActivity.getApplicationContext()
            
            """
            Obtener ApplicationInfo
            Accedemos a nativeLibraryDir donde Android descomprime los .so
            """
            app_info = context.getApplicationInfo()
            
            """
            Ruta de librerías nativas
            """
            lib_path = app_info.nativeLibraryDir
            
            return lib_path

        except Exception as e:
            print("[ANDROID_CHESS] Error obteniendo nativeLibraryDir: " + str(e))
            return None

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

                """
                EXTRA MODULE LOGS
                Redirect specific MAS loggers to the external folder.
                """
                extra_loggers = ["aff_log", "pnm", "submod_log", "spj", "mfgen"]
                
                for log_name in extra_loggers:
                    try:
                        tgt_log = logging.getLogger(log_name)
                        
                        """
                        Disconnect existing handlers to prevent internal writing.
                        """
                        for h in tgt_log.handlers[:]:
                            tgt_log.removeHandler(h)
                            h.close()
                        
                        """
                        Attach external rotating handler.
                        Using .txt extension for mobile accessibility.
                        """
                        l_file = os.path.join(ANDROID_LOG_PATH, log_name + ".txt")
                        
                        l_hdlr = logging.handlers.RotatingFileHandler(
                            l_file,
                            maxBytes=getattr(store.mas_logging, "MAX_LOG_SIZE", 5242880),
                            backupCount=getattr(store.mas_logging, "BACKUP_COUNT", 5)
                        )
                        
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
        ANDROID LOG RESCUE SYSTEM

        Scans potential internal directories for Ren'Py system logs (traceback.txt, log.txt)
        and copies them to the user-accessible external storage (Backpack).

        This is necessary because Android restricted storage prevents users from seeing
        tracebacks when the game crashes.

        OUT:
            Writes copied logs to ANDROID_BACKPACK_PATH if found.
            Generates 'log_rescue_debug.txt' with search results.
        """
        if not renpy.android:
            return

        try:
            """
            CANDIDATE LIST GENERATION
            We build a list of potential internal paths where Ren'Py might have
            dumped the crash logs.
            """
            candidates = []
            
            """
            # 1. Private Files Dir
            """
            private_dir = os.environ.get('ANDROID_PRIVATE', '')
            if private_dir:
                candidates.append(private_dir)
                candidates.append(os.path.join(private_dir, "files"))
            
            """
            # 2. Ren'Py Base Dir
            """
            if renpy.config.basedir:
                candidates.append(renpy.config.basedir)
                
            """
            # 3. Current Working Dir
            """
            candidates.append(os.getcwd())
            
            """
            # Deduplicate candidates
            """
            candidates = list(set(candidates))
            
            logs_to_rescue = ["traceback.txt", "log.txt"]
            
            """
            # Debug info to help user identify where we are looking
            """
            debug_info = []
            debug_info.append("Searching for logs in:")
            for c in candidates:
                debug_info.append(" - " + str(c))
                
            found_any = False
            
            for log_file in logs_to_rescue:
                for src_dir in candidates:
                    src_path = os.path.join(src_dir, log_file)
                    
                    if os.path.exists(src_path):
                        """
                        Move logs to Backpack root for user access.
                        """
                        dst_path = os.path.join(ANDROID_BACKPACK_PATH, log_file)
                        try:
                            shutil.copy2(src_path, dst_path)
                            debug_info.append("SUCCESS: Found and copied " + log_file + " from " + src_dir)
                            found_any = True
                            """
                            Stop searching for this specific file once found
                            """
                            break 
                        except Exception as e:
                            debug_info.append("ERROR: Found " + log_file + " but failed to copy: " + str(e))
            
            if not found_any:
                debug_info.append("FAILURE: Could not find log.txt or traceback.txt in any candidate.")

            """
            # Write debug info to a visible file so user can report back
            """
            try:
                debug_path = os.path.join(ANDROID_BACKPACK_PATH, "log_rescue_debug.txt")
                with open(debug_path, "w") as f:
                    f.write("\n".join(debug_info))
            except:
                pass

        except Exception as e:
            print("[ANDROID_RESCUE] Error processing log rescue: " + str(e))


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