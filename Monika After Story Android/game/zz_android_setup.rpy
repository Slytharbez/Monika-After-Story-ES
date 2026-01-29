python early:
    import os
    import sys
    import re


    
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
        [CRITICAL FIX] LOGGING DIRECTORY MOVED TO EARLY INIT
        We now handle this in init -999 to assert control before Ren'Py starts logging.
        """
        pass
            
        """
        [ANDROID] SUBMOD EXTERNAL SEARCH PATH
        Inject external submod paths into config.searchpath.
        This allows Ren'Py to automatically scan and load .rpy files from these locations.
        """
        try:
            mas_root = "/storage/emulated/0/Monika After Story"
            
            candidates = [
                mas_root + "/game/submods",
                mas_root + "/game/Submods",
                mas_root + "/submods",
                mas_root + "/Submods"
            ]
            
            ext_submods_dir = None
            
            # print("[ANDROID_Submods_Early] Comprobando candidatos...")
            
            for cand in candidates:
                if os.path.exists(cand):
                    ext_submods_dir = cand
                    # print("[ANDROID_Submods_Early] Encontrado: " + cand)
                    break
            
            if ext_submods_dir:
                if ext_submods_dir not in config.searchpath:
                    config.searchpath.append(ext_submods_dir)
                    # print("[ANDROID_Submods_Early] Directorio de submods agregado a config.searchpath")

            # [CRITICAL FIX] Add external 'game' folder to searchpath
            # This allows submods to access assets via 'submods/MySubmod/image.png'
            ext_game_dir = mas_root + "/game"
            if os.path.exists(ext_game_dir):
                if ext_game_dir not in config.searchpath:
                    config.searchpath.append(ext_game_dir)
                    # print("[ANDROID_Submods_Early] Directorio de juego agregado a config.searchpath: " + ext_game_dir)
            
            # [CRITICAL FIX] Add external 'python-packages' to sys.path
            # This allows location submods (which use python-packages) to work
            import sys
            ext_packages_dir = mas_root + "/game/python-packages"
            if os.path.exists(ext_packages_dir):
                if ext_packages_dir not in sys.path:
                    sys.path.append(ext_packages_dir)
                    # print("[ANDROID_Submods_Early] Paquetes de python agregados a sys.path: " + ext_packages_dir)

        except Exception as e:
            print("Error en submods de Android: " + str(e))


init -999 python:
    import os
    import shutil
    import platform

    """
    CONSTANTES DE RUTAS
    """
    ANDROID_PUBLIC_PATH = "/storage/emulated/0/Monika After Story/"
    
    # [ANDROID] Override basedir so submods find their assets in external storage
    if renpy.android:
        renpy.config.basedir = ANDROID_PUBLIC_PATH
        
        # [ANDROID] Internal Log Location (English Master)
        # We set this VERY early ensuring Ren'Py writes the master log here.
        # This allows us to read it later for the Spanish sync.
        try:
            _private_files = os.environ.get("ANDROID_PRIVATE", "")
            if _private_files:
                # Standardize on 'files' subdir if available, or root private
                # [FIX] Avoid creating 'files/files' if ANDROID_PRIVATE already ends in 'files'
                if _private_files.rstrip("/").endswith("files"):
                    _log_dir = _private_files
                else:
                    _log_dir = os.path.join(_private_files, "files")
                if not os.path.exists(_log_dir):
                    os.makedirs(_log_dir)
                
                config.log_directory = _log_dir
                config.log_enable = True
        except:
            pass

    
    """
    Subdirectorios críticos
    """
    ANDROID_CHARACTERS_PATH = os.path.join(ANDROID_PUBLIC_PATH, "characters/")
    ANDROID_CHESS_PATH = os.path.join(ANDROID_PUBLIC_PATH, "chess_games/")
    ANDROID_LOG_PATH = os.path.join(ANDROID_PUBLIC_PATH, "log/")
    ANDROID_SAVES_PATH = os.path.join(ANDROID_PUBLIC_PATH, "game/saves/")
    ANDROID_CUSTOM_BGM_PATH = os.path.join(ANDROID_PUBLIC_PATH, "custom_bgm/")
    
    """
    Función de creación agresiva
    """
    def mas_android_setup_public_storage():
        if not renpy.android:
            return

        dirs_to_create = [
            ANDROID_PUBLIC_PATH,
            ANDROID_CHARACTERS_PATH,
            ANDROID_CHESS_PATH,
            ANDROID_LOG_PATH,
            ANDROID_SAVES_PATH,
            ANDROID_CUSTOM_BGM_PATH,
            os.path.join(ANDROID_PUBLIC_PATH, "game/python-packages/"),
            os.path.join(ANDROID_PUBLIC_PATH, "game/submods/"),
            os.path.join(ANDROID_PUBLIC_PATH, "game/mod_assets/location/"),
            os.path.join(ANDROID_PUBLIC_PATH, "game/mod_assets/thumbs/"),
            os.path.join(ANDROID_PUBLIC_PATH, "game/mod_assets/monika/"),
            os.path.join(ANDROID_PUBLIC_PATH, "game/mod_assets/monika/a/"),
            os.path.join(ANDROID_PUBLIC_PATH, "game/mod_assets/monika/c/"),
            os.path.join(ANDROID_PUBLIC_PATH, "game/mod_assets/monika/f/"),
            os.path.join(ANDROID_PUBLIC_PATH, "game/mod_assets/monika/h/"),
            os.path.join(ANDROID_PUBLIC_PATH, "game/mod_assets/monika/j/"),
            os.path.join(ANDROID_PUBLIC_PATH, "game/mod_assets/monika/t/")
        ]

        # print("Iniciando creación agresiva de directorios...")
        for d in dirs_to_create:
            if not os.path.exists(d):
                try:
                    os.makedirs(d)
                    # print("Creado: " + d)
                except Exception as e:
                    print("Error creando " + d + ": " + str(e))
            else:
                pass
    
    mas_android_setup_public_storage()




init 50 python:
    """
    [ANDROID] MANUAL SUBMOD LOADER & PATCHES
    We load submods LATE (init 50) to ensure all core MAS components (like mas_seasons at init 10)
    are fully initialized before submods try to use them.
    """
    if renpy.android:
        import os
        
        # Redefine candidates to ensure we find the right path again
        mas_loader_root = "/storage/emulated/0/Monika After Story"
        loader_candidates = [
            mas_loader_root + "/game/submods",
            mas_loader_root + "/game/Submods",
            mas_loader_root + "/submods",
            mas_loader_root + "/Submods"
        ]
        
        ext_loader_dir = None
        for cand in loader_candidates:
            if os.path.exists(cand):
                ext_loader_dir = cand
                break
        
        if ext_loader_dir:
            # print("[ANDROID_LOADER] Escaneando archivos .rpy en: " + ext_loader_dir)
            
            # Get list of files Ren'Py already knows about to avoid double-loading
            known_files = set(renpy.list_files())
            
            for root, dirs, files in os.walk(ext_loader_dir):
                for f in files:
                    if f.endswith(".rpy"):
                        full_path = os.path.join(root, f)
                        
                        # Calculate relative path to check against known_files
                        # Ren'Py usually stores paths relative to the searchpath root with forward slashes
                        rel_path = os.path.relpath(full_path, ext_loader_dir).replace("\\", "/")
                        
                        if rel_path in known_files:
                            print("Omitiendo archivo conocido: " + rel_path)
                            continue
                            
                        try:
                            # Open as binary to avoid encoding issues on read, then decode
                            with open(full_path, "rb") as f_obj:
                                content_bytes = f_obj.read()
                                
                            # [ANDROID] ENCODING SAFETY
                            # Try common encodings to prevent crash if user file is not UTF-8
                            content_unicode = None
                            for enc in ["utf-8", "latin-1", "cp1252"]:
                                try:
                                    content_unicode = content_bytes.decode(enc)
                                    break
                                except:
                                    continue
                                    
                            if content_unicode:
                                # Manually load the script content
                                renpy.load_string(content_unicode, filename=full_path)
                                # print("[ANDROID_LOADER] Cargado: " + f)
                            else:
                                print("[ANDROID_LOADER] ERROR: No se pudo decodificar " + f)
                                
                        except Exception as e:
                            print("ERROR cargando " + f + ": " + str(e))
                            import traceback
                            traceback.print_exc()
                            
            # [ANDROID] APPLY PATCHES AFTER LOADING
            try:
                if store.mas_compliments:
                    store.mas_compliments.mas_get_player_nickname = mas_get_player_nickname
                    # print("[ANDROID_PATCH] Inyectado mas_get_player_nickname en mas_compliments")
            except:
                pass
                
        else:
            print("No se encontró el directorio de submods, esto no debería suceder si la inicialización temprana funcionó.")




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
            print("Error de Ajedrez obteniendo nativeLibraryDir: " + str(e))
            return None

    def mas_android_has_permission():
        """
        CHECKER OPTIMIZADO - DEBUG EXTREMO
        
        Verifica permisos con logs detallados para diagnosticar fallos.
        """
        if not renpy.android: return True
        try:
            # print("[ANDROID_PERM_DEBUG] Starting permission check...")
            
            CurrentActivity = mas_get_current_activity()
            if not CurrentActivity:
                print("Error de Permisos: CurrentActivity es None")
                
            sdk = _VERSION.SDK_INT
            # print("[ANDROID_PERM_DEBUG] SDK_INT: " + str(sdk))
            
            if sdk >= 30:
                is_manager = _Environment.isExternalStorageManager()
                # print("[ANDROID_PERM_DEBUG] isExternalStorageManager(): " + str(is_manager))
                return is_manager
            else:
                res = CurrentActivity.checkSelfPermission("android.permission.WRITE_EXTERNAL_STORAGE")
                is_granted = (res == _PackageManager.PERMISSION_GRANTED)
                print("Permiso Legacy concedido: " + str(is_granted))
                return is_granted
        except Exception as e:
            print("Excepción en comprobación de permisos: " + str(e))
            import traceback
            traceback.print_exc()
            return False


init 50 python:
    """
    Subdirectorios a rutas de "La Mochila".
    """
    def mas_extract_stockfish():
        if not renpy.android: return None
        try:
            import zipfile
            import sys
            
            # 1. Detect Architecture
            # We use maxsize to determine if we are running 64-bit python
            is_64_bit = sys.maxsize > 2**32
            target_abi = "arm64-v8a" if is_64_bit else "armeabi-v7a"
            
            # 2. Paths
            CurrentActivity = mas_get_current_activity()
            if not CurrentActivity: return None
            
            context = CurrentActivity.getApplicationContext()
            apk_path = context.getApplicationInfo().publicSourceDir
            
            private_dir = os.environ.get("ANDROID_PRIVATE", "")
            # Ensure target directory exists
            # [ANDROID] Simplify path: putting it directly in private files root to avoid 'files/files' confusion
            out_file = os.path.join(private_dir, "stockfish_bin")
            
            # 3. Extract
            with zipfile.ZipFile(apk_path, "r") as z:
                # Path inside APK: lib/<abi>/libstockfish.so
                target_entry = "lib/" + target_abi + "/libstockfish.so"
                
                if target_entry not in z.namelist():
                    print("[MAS_STOCKFISH] Entry not found: " + target_entry)
                    return None
                    
                with open(out_file, "wb") as f:
                    f.write(z.read(target_entry))
            
            # 4. Permission
            os.chmod(out_file, 0o755)
            # print("[MAS_STOCKFISH] Extracted to " + out_file)
            return out_file
            
        except Exception as e:
            print("[MAS_STOCKFISH] Error: " + str(e))
            return None

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
                Redirigir binario de Stockfish a extraccion manual
                """
                sf_path = mas_extract_stockfish()
                if sf_path:
                    store.mas_chess.STOCKFISH_PATH = sf_path
                else:
                    # Fallback path if extraction fails
                    p_dir = os.environ.get('ANDROID_PRIVATE', '')
                    store.mas_chess.STOCKFISH_PATH = os.path.join(p_dir, "files", "stockfish_bin")
                
                # print("[ANDROID_OVERRIDES] Chess Save Path & Binary configured")
            
            if hasattr(store, 'mas_docking_station'):
                store.mas_docking_station.station = ANDROID_CHARACTERS_PATH
                if not os.path.isdir(ANDROID_CHARACTERS_PATH):
                    try:
                        os.makedirs(ANDROID_CHARACTERS_PATH)
                    except:
                        pass
                # print("[ANDROID_OVERRIDES] Docking Station redirected")

            """
            Logging Override
            """
            import logging.handlers
            root_logger = logging.getLogger()
            
            # [ANDROID] DO NOT remove existing handlers!
            # Removing them stops Ren'Py from printing to stdout, which kills MASTranslator.
            # We just ADD our external file handler so logs go to BOTH.
            # for h in root_logger.handlers[:]:
            #     root_logger.removeHandler(h)
            #     h.close()
            
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
                # print("[ANDROID_OVERRIDES] Logging redirected")

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
                        # print("[ANDROID_OVERRIDES] Redirected extra logger: " + log_name)
                        
                    except Exception as e:
                        print("Fallo al redirigir " + log_name + ": " + str(e))

            except Exception as e:
                print("Error en redirección de logs: " + str(e))
        
        
        else:
            print("Permisos no detectados. Usando rutas internas para evitar crash.")





    def mas_android_check_readme():
        """
        Extracción de README.html desde el APK si no existe públicamente
        o si la versión del APK es más reciente.
        """
        if not renpy.android:
            return

        debug_log = []
        debug_log.append("--- README CHECK ---")

        try:
            target_path = os.path.join(ANDROID_PUBLIC_PATH, "README.html")
            
            # 1. Access APK using zipfile
            import zipfile
            CurrentActivity = mas_get_current_activity()
            if not CurrentActivity: 
                debug_log.append("FAIL: No CurrentActivity")
                return
            
            context = CurrentActivity.getApplicationContext()
            apk_path = context.getApplicationInfo().publicSourceDir
            debug_log.append("APK Path: " + str(apk_path))
            
            with zipfile.ZipFile(apk_path, "r") as z:
                # [ANDROID] RECURSIVE SEARCH FOR README.html
                # We iterate ALL files in the APK to find anything that looks like "README.html"
                debug_log.append("Scanning APK structure aggressively (recursive)...")
                
                readme_candidates = []
                all_files = z.namelist()
                
                for f in all_files:
                    if f.lower().endswith("readme.html"):
                        readme_candidates.append(f)
                
                debug_log.append("Candidates found: " + str(readme_candidates))
                
                found_entry = None
                
                # Priority: root > assets > others
                # We sort to prefer shorter paths (root)
                readme_candidates.sort(key=len)
                
                if readme_candidates:
                    found_entry = readme_candidates[0]
                    debug_log.append("Selected candidate: " + found_entry)
                
                if found_entry:
                    # Logic: If target missing OR different size -> Extract
                    # (Size is a cheap proxy for version/content change)
                    do_extract = False
                    
                    if not os.path.exists(target_path):
                        do_extract = True
                        debug_log.append("Reason: Target missing")
                    else:
                        # Check size
                        apk_info = z.getinfo(found_entry)
                        local_size = os.path.getsize(target_path)
                        debug_log.append("APK Size: " + str(apk_info.file_size) + " vs Local: " + str(local_size))
                        
                        if apk_info.file_size != local_size:
                            do_extract = True
                            debug_log.append("Reason: Size mismatch")
                        else:
                            debug_log.append("Reason: Up to date")
                            
                    if do_extract:
                        with open(target_path, "wb") as f:
                            f.write(z.read(found_entry))
                        debug_log.append("SUCCESS: Extracted to " + target_path)
                    else:
                        debug_log.append("SKIPPED: Already up to date")

                else:
                    debug_log.append("FAIL: README.html not found in APK structure.")
                    try:
                        # Dump some assets to see structure
                        debug_log.append("Sample ZIP entries: " + str(z.namelist()[:10]))
                    except:
                        pass
        except Exception as e:
            debug_log.append("ERROR EXCEPTION: " + str(e))
            print("Error checking README: " + str(e))
        
        # Write debug log
        try:
            debug_path = os.path.join(ANDROID_PUBLIC_PATH, "log_rescue_debug.txt")
            with open(debug_path, "a") as f:
                f.write("\n" + "\n".join(debug_log))
        except:
            pass

    mas_android_check_readme()


init python:



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

init 500 python:
    """
    [ANDROID] NOTIFICATION REWARD CHECKER
    Checks if the game was launched via notification and awards affection.
    Uses config.label_callback to run safely when the game loop starts (ch30_init).
    """
    mas_android_intent_checked = False

    def mas_android_check_notif_launch(label, abnormal):
        global mas_android_intent_checked
        
        # Only check once per session and only on main start
        if mas_android_intent_checked:
            return
            
        if label == "ch30_init":
            mas_android_intent_checked = True
            
            if not renpy.android:
                return

            try:
                # Import Activity
                try: 
                    PythonActivity = autoclass('org.renpy.android.PythonSDLActivity')
                except: 
                    PythonActivity = autoclass('org.renpy.android.PythonActivity')
                    
                activity = PythonActivity.mActivity
                intent = activity.getIntent()
                
                # Check for Extra "launch_from_notif"
                # Default to False
                from_notif = intent.getBooleanExtra("launch_from_notif", False)
                
                if from_notif:
                    print("[MAS_ANDROID] Launched from Notification! Attempting affection gain...")
                    
                    # Award Affection if MAS function exists
                    if hasattr(store, "mas_gainAffection"):
                        # Gain 1.0 affection, bypass daily limit checks if possible
                        store.mas_gainAffection(1.0, bypass=True)
                        print("[MAS_ANDROID] Affection granted.")
                        
                        # CLEANUP: Cancel pending sticky notifications
                        if hasattr(store, "mas_android_cancel_all_notifs"):
                            store.mas_android_cancel_all_notifs()
                            print("[MAS_ANDROID] Notifications cleared.")
                        
                        # OPTIONAL: Play a sound or queue a greeting?
                        # For now, we trust the affection log.
                        
            except Exception as e:
                print("[MAS_ANDROID] Intent Check Error: " + str(e))

    # Register the callback
    config.label_callback = mas_android_check_notif_launch


init 50 python:
    def mas_android_cancel_all_notifications():
        """
        NUCLEAR CLEANUP:
        Cancels all WorkManager jobs and NotificationManager notifications.
        This resolves the "Zombie" notification issue on game start.
        """
        if not renpy.android: 
            return
            
        try:
            from jnius import autoclass
            
            # 1. Resolve Activity
            try:
                PythonActivity = autoclass('org.renpy.android.PythonSDLActivity')
            except:
                PythonActivity = autoclass('org.renpy.android.PythonActivity')
            
            mActivity = PythonActivity.mActivity
            
            # 2. Cancel WorkManager (The "Sticky" Worker)
            # This kills the Foreground Service loop in NotificationWorker
            WorkManager = autoclass('androidx.work.WorkManager')
            try:
                WorkManager.getInstance(mActivity).cancelAllWork()
            except Exception as e:
                print("MAS_NOTIF: WorkManager cancel failed: " + str(e))
            
            # 3. Cancel Standard Notifications (Fallback)
            try:
                Context = autoclass('android.content.Context')
                NotificationManager = mActivity.getSystemService(Context.NOTIFICATION_SERVICE)
                NotificationManager.cancelAll()
            except Exception as e:
                print("MAS_NOTIF: NotificationManager cancel failed: " + str(e))
                
            # print("MAS_NOTIF: Cleanup executed successfully.")
            
        except Exception as e:
            print("MAS_NOTIF: cleanup critical error: " + str(e))

    # Alias for existing code if present
    store.mas_android_cancel_all_notifs = mas_android_cancel_all_notifications

# Auto-Run on Startup (Cold Boot) & Load Hook
init 999 python:
    if renpy.android:
        # Run Immediate Cleanup
        mas_android_cancel_all_notifications()
        
        # Register for Save Loads
        config.after_load_callbacks.append(mas_android_cancel_all_notifications)

init 999 python:
    def mas_android_copy_logs():
        if not renpy.android:
            return

        import os
        import shutil
        import datetime
        import sys
        
        # JNI / Flush Check: Force flush of stdout/stderr to ensure log.txt is up to date
        try:
            sys.stdout.flush()
            sys.stderr.flush()
        except:
            pass

        debug_lines = []
        debug_lines.append("\n--- LOG COPY EXECUTION AT: " + str(datetime.datetime.now()) + " ---")
        debug_lines.append("Stdout: " + str(sys.stdout))

        # 1. Define Sources
        sources = []
        
        # A. ANDROID_PRIVATE
        private_dir = os.environ.get("ANDROID_PRIVATE", "")
        if private_dir:
            sources.append(private_dir)
            sources.append(os.path.join(private_dir, "files"))
        
        if hasattr(renpy.config, "log_directory") and renpy.config.log_directory:
            sources.append(renpy.config.log_directory)
        
        # C. External Files Dir (Android/data/pkg/files) - Critical for Tracebacks
        try:
            from jnius import autoclass
            # Resolve Activity
            try:
                PythonActivity = autoclass('org.renpy.android.PythonSDLActivity')
            except:
                PythonActivity = autoclass('org.renpy.android.PythonActivity')
            
            mActivity = PythonActivity.mActivity
            ext_files_file = mActivity.getExternalFilesDir(None)
            if ext_files_file:
                ext_path = ext_files_file.getAbsolutePath()
                sources.append(ext_path)
                debug_lines.append("Added JNI External Path: " + str(ext_path))
        except Exception as e:
            debug_lines.append("JNI External Path Error: " + str(e))

        # D. Current Working Directory (Just in case)
        sources.append(os.getcwd())

        debug_lines.append("Candidates: " + str(sources))

        # Helper to find ALL source files for debug
        def find_best_source(filename):
            candidates = []
            for src in sources:
                fpath = os.path.join(src, filename)
                if os.path.exists(fpath):
                    # Gather info
                    size = os.path.getsize(fpath)
                    try:
                        mtime = os.path.getmtime(fpath)
                        dt_mtime = datetime.datetime.fromtimestamp(mtime)
                    except:
                        dt_mtime = "Unknown"
                    
                    info = "Found " + fpath + " [Size: " + str(size) + " Time: " + str(dt_mtime) + "]"
                    debug_lines.append(info)
                    candidates.append(fpath)
            
            if not candidates:
                debug_lines.append("NOT FOUND: " + filename)
                return None
            
            # Return the first one
            return candidates[0]

        # Helper to copy and translate headers
        def copy_and_mask_log(source_path, dest_filename):
            if not source_path:
                return

            try:
                # 1. Read Original Content (English)
                with open(source_path, "r") as f:
                    content = f.read()
                
                # Report Last Line to debug truncation
                if content:
                    lines = content.splitlines()
                    last_line = lines[-1] if lines else "<empty>"
                    debug_lines.append("Last line of " + dest_filename + ": " + repr(last_line))
                    debug_lines.append("Total lines: " + str(len(lines)))
                
                # 2. Translate Header and Content
                # Dictionary of replacements
                replacements = {
                    "I'm sorry, but an uncaught exception occurred.": "Lo sentimos, pero ha ocurrido un error inesperado...",
                    "Unknown platform.": "Plataforma desconocida.",
                    "Manufacturer": "Fabricante",
                    "Screen diagonal is": "La diagonal de la pantalla es",
                    "Mobile search paths": "Rutas de búsqueda móvil",
                    "Early init took": "La inicialización temprana tomó",
                    "Loading error handling took": "Carga de manejo de errores tomó",
                    "Saving to": "Guardando en",
                    "Loading script took": "Carga del script tomó",
                    "Loading save slot metadata took": "Carga de metadatos de guardado tomó",
                    "Loading persistent took": "Carga del persistent tomó",
                    "Set script version to": "Versión del script establecida en",
                    "Running init code took": "Ejecución de código init tomó",
                    "Loading analysis data took": "Carga de datos de análisis tomó",
                    "Analyze and compile ATL took": "Análisis y compilación de ATL tomó",
                    "Reloading save slot metadata took": "Recarga de metadatos de guardado tomó",
                    "Index archives took": "Indexación de archivos tomó",
                    "Dump and make backups took": "Volcado y backups tomó",
                    "Cleaning cache took": "Limpieza de caché tomó",
                    "Making clean stores took": "Creación de stores limpios tomó",
                    "Initial gc took": "Recolección de basura inicial tomó",
                    "DPI scale factor": "Factor de escala DPI",
                    "Creating interface object took": "Creación de objeto de interfaz tomó",
                    "Cleaning stores took": "Limpieza de stores tomó",
                    "Init translation took": "Inicialización de traducción tomó",
                    "Build styles took": "Construcción de estilos tomó",
                    "Load screen analysis took": "Carga de análisis de pantalla tomó",
                    "Analyze screens took": "Análisis de pantallas tomó",
                    "Save screen analysis took": "Guardado de análisis de pantalla tomó",
                    "Prepare screens took": "Preparación de pantallas tomó",
                    "Save pyanalysis. took": "Guardado de pyanalysis tomó",
                    "Save bytecode. took": "Guardado de bytecode tomó",
                    "Running _start took": "Ejecución de _start tomó",
                    "Interface start took": "Inicio de interfaz tomó",
                    "Initializing gles2 renderer": "Inicializando renderizador gles2",
                    "primary display bounds": "límites pantalla principal",
                    "swap interval": "intervalo de intercambio",
                    "Fullscreen mode": "Modo pantalla completa",
                    "Display Info": "Info de Pantalla",
                    "Screen sizes": "Tamaños de pantalla",
                    "Could not open": "No se pudo abrir",
                    "Maximum texture size": "Tamaño máximo de textura",
                    "Total time until interface ready": "Tiempo total hasta interfaz lista",
                    "Hid presplash": "Ocultó presplash",
                    "While running game code:": "Mientras se ejecuta el código del juego:",
                    "-- Full Traceback ------------------------------------------------------------": "-- Seguimiento completo ------------------------------------------------------------",
                    "Full traceback:": "Seguimiento completo:"
                }
                
                # Apply replacements
                for en, es in replacements.items():
                    if en in content:
                        content = content.replace(en, es)
                
                # Debug message for translation
                debug_lines.append("Applied translations to " + dest_filename)
                
                # 3. Write to Public Destination
                dest_path = os.path.join(store.ANDROID_PUBLIC_PATH, dest_filename)
                
                # Ensure destination directory exists
                dest_dir = os.path.dirname(dest_path)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)

                with open(dest_path, "w") as f:
                    f.write(content)
                
                debug_lines.append("SUCCESS: Wrote to " + dest_path)

            except Exception as e:
                debug_lines.append("ERROR copying " + dest_filename + ": " + str(e))

        # Execute Copy for key files
        # Note: We now use find_best_source to log all duplicates
        copy_and_mask_log(find_best_source("log.txt"), "log.txt")
        copy_and_mask_log(find_best_source("traceback.txt"), "traceback.txt")
        
        # Write Debug Log (APPEND MODE)
        try:
            debug_file = os.path.join(store.ANDROID_PUBLIC_PATH, "mas_log_copy_report.txt")
            with open(debug_file, "a") as f:
                f.write("\n".join(debug_lines))
            
            # Cleanup old debug file if requested
            old_debug = os.path.join(store.ANDROID_PUBLIC_PATH, "log_rescue_debug.txt")
            if os.path.exists(old_debug):
                os.remove(old_debug)
        except:
            pass

    # Call moved to splash.rpy to ensure full log capture
    # mas_android_copy_logs()


# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc