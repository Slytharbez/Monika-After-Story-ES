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
            
            source_path = os.path.join(renpy.config.gamedir, "mod_assets/games/chess", binary_name)
            private_dir = os.environ.get('ANDROID_PRIVATE', '')
            dest_dir = os.path.join(private_dir, "files")
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            dest_path = os.path.join(dest_dir, "stockfish_android")

            if os.path.exists(source_path):
                shutil.copyfile(source_path, dest_path)
                os.chmod(dest_path, 0o755)
                print("[ANDROID_CHESS] Stockfish instalado en: " + dest_path)
            else:
                print("[ANDROID_CHESS] ERROR: No se encontró el binario en " + source_path)
        except Exception as e:
            print("[ANDROID_CHESS] Excepción instalando Stockfish: " + str(e))

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
                print("[ANDROID_OVERRIDES] Chess Save Path redirected")
            
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
            except Exception as e:
                print("[ANDROID_OVERRIDES] Logging Redirect Error: " + str(e))
        
            print("[ANDROID_OVERRIDES] Permisos no detectados. Usando rutas internas para evitar crash.")

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

    def mas_android_generateMonika(dockstat, logpath):
        """
        [ANDROID] generateMonika
        
        Una versión parcheada de generateMonika que usa renpy.file()
        para leer el archivo 'mbase' desde el APK en lugar de open().
        """
        import codecs
        import store.mas_docking_station as mas_dockstat_module
        from cStringIO import StringIO as fastIO
        
        cr_log = store.mas_logging.init_log(logpath, append=False)
        cr_log.info("[ANDROID] Creating Monika in: {0}".format(dockstat.station))
        
        if "temp" in dockstat.station.lower():
            cr_log.error("temp directory found, aborting.")
            return False
            
        moni_buffer = fastIO()
        moni_buffer = codecs.getwriter("utf8")(moni_buffer)
        
        NUM_DELIM = "|num|"
        
        if not mas_dockstat_module._buildMetaDataPer(moni_buffer, cr_log):
            mas_dockstat_module._buildMetaDataList(moni_buffer)
             
        moni_chr = None
        try:
            """
            [ANDROID FIX]
            Usamos renpy.file() para leer desde el asset (APK o RPA).
            """
            moni_chr = renpy.file("mod_assets/monika/mbase")
            moni_buffer.write(moni_chr.read())
            
        except Exception as e:
            cr_log.error("[ANDROID] mbase copy failed | {0}".format(repr(e)))
            
            """
            DEBUG: List files to see if mbase exists
            """
            try:
                all_files = renpy.list_files()
                mbase_candidates = [f for f in all_files if "mbase" in f]
                cr_log.info("[ANDROID DEBUG] Candidates for mbase: " + str(mbase_candidates))
            except:
                pass
            
            moni_buffer.close()
            return False
            
        finally:
            if moni_chr is not None:
                moni_chr.close()
                
        # El resto de la función es idéntica a la original, 
        # pero necesitamos llamar a los métodos internos de MASDockingStation
        # usando la instancia 'dockstat' o la clase 'store.MASDockingStation'.
        
        moni_path = dockstat._trackPackage("monika")
        moni_fbuffer = None
        moni_tbuffer = None
        moni_sum = None
        blocksize = 4 * (1024**2) # Hardcoded from zz_dockingstation default
        
        try:
            # Usando la clase store.MASDockingStation para métodos estáticos
            moni_buffer_iter = store.MASDockingStation._blockiter(moni_buffer, blocksize)
            lines = 0
            last_line_size = 0
            for _line in moni_buffer_iter:
                lines += 1
                last_line_size = len(_line)
                
            line_str_size = len(str(lines) + NUM_DELIM)
            if (last_line_size + line_str_size) > blocksize:
                lines += 1
                
            moni_buffer_iter = store.MASDockingStation._blockiter(moni_buffer, blocksize)
            moni_tbuffer = fastIO()
            moni_tbuffer = codecs.getwriter("utf8")(moni_tbuffer)
            moni_tbuffer.write(str(lines) + NUM_DELIM)
            for _line in moni_buffer_iter:
                moni_tbuffer.write(_line)
            moni_buffer.close()
            
            # Escritura en disco (La ruta ya es externa gracias a nuestros overrides)
            moni_fbuffer = codecs.open(moni_path, "wb", "utf-8")
            
            checklist = dockstat.hashlib.sha256()
            def safe_encoder(data):
                return dockstat.base64.b64encode(dockstat.safeRandom(data))
            encoder = dockstat.base64.b64encode
            
            moni_tbuffer.seek(0)
            _line = moni_tbuffer.read(blocksize)
            total_buffer_size = 0
            while len(_line) == blocksize:
                total_buffer_size += blocksize
                data = encoder(_line)
                checklist.update(data)
                moni_fbuffer.write(data)
                _line = moni_tbuffer.read(blocksize)
            moni_tbuffer.close()
            
            last_buffer_size = len(_line)
            total_buffer_size += last_buffer_size
            
            moni_size_left = store.persistent._mas_dockstat_moni_size - total_buffer_size
            
            if moni_size_left > 0:
                if (moni_size_left + last_buffer_size) <= blocksize:
                    extra_padding = moni_size_left
                    moni_size_left = 0
                else:
                    extra_padding = blocksize - last_buffer_size
                    moni_size_left -= extra_padding
                    
                data = encoder(_line + dockstat.safeRandom(extra_padding))
                checklist.update(data)
                moni_fbuffer.write(data)
                
                moni_size_limit = moni_size_left - blocksize
                curr_size = 0
                while curr_size < moni_size_limit:
                    data = safe_encoder(blocksize)
                    checklist.update(data)
                    moni_fbuffer.write(data)
                    curr_size += blocksize
                    
                leftovers = moni_size_left - curr_size
                if leftovers > 0:
                    data = safe_encoder(leftovers)
                    checklist.update(data)
                    moni_fbuffer.write(data)
            else:
                data = encoder(_line)
                checklist.update(data)
                moni_fbuffer.write(data)
                
            moni_sum = checklist.hexdigest()
            
        except Exception as e:
            cr_log.error("monibuffer write failed | {0}".format(repr(e)))
            try:
                if moni_fbuffer is not None: moni_fbuffer.close()
                moni_fbuffer = None
                os.remove(moni_path)
            except: pass
            return False
            
        finally:
            if moni_fbuffer is not None: moni_fbuffer.close()
            if moni_tbuffer is not None: moni_tbuffer.close()
            moni_buffer.close()
             
        # Validación final
        moni_pkg = dockstat.getPackage("monika")
        if moni_pkg is None:
            cr_log.error("monika not found.")
            store.mas_utils.trydel(moni_path)
            return False
            
        moni_slip = dockstat.createPackageSlip(moni_pkg, blocksize)
        if moni_slip is None:
            cr_log.error("monika could not be validated.")
            store.mas_utils.trydel(moni_path)
            return False
            
        if moni_slip != moni_sum:
            cr_log.critical("monisums didn't match, did we have write failure?")
            store.mas_utils.trydel(moni_path)
            return -1
            
        cr_log.info("chk: {0}".format(moni_sum))
        return moni_sum

    if renpy.android:
        """
        [ANDROID] INJECTION
        Reemplazamos la función original en el store 'mas_dockstat'.
        Esto es crítico porque 'monikagen_promise' usa esta referencia específica
        al inicializarse en init 205.
        """
        import store.mas_dockstat as mas_dockstat
        mas_dockstat.generateMonika = mas_android_generateMonika
        print("[ANDROID_OVERRIDES] 'store.mas_dockstat.generateMonika' monkey-patched.")


# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc