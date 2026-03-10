init -100 python:
    """
    PERSISTENT COMPATIBILITY - BINARY FIXUP
    Ren'Py 7.8.4 saves RevertableDict/List/Set as 'renpy.revertable.*' in pickle.
    Ren'Py 6.99.12 (PC) expects 'renpy.python.*'.
    This post-processes the persistent file: decompress -> binary replace -> recompress.
    """
    import zlib
    import os

    _COMPAT_SAVE_DIR = "/storage/emulated/0/Monika After Story/game/saves"


    def _compat_fixup_persistent():
        """
        Post-processes the persistent file to replace renpy.revertable
        references with renpy.python in the pickle stream.
        The pickle GLOBAL opcode format is: c<module>\n<name>\n
        So 'crenpy.revertable\n' -> 'crenpy.python\n' is valid.
        """
        log = []
        try:
            per_path = os.path.join(_COMPAT_SAVE_DIR, "persistent")

            if not os.path.exists(per_path):
                log.append("No persistent file found")
                return log

            with open(per_path, "rb") as f:
                raw = f.read()
            log.append("File size: " + str(len(raw)))

            dec = zlib.decompress(raw)
            log.append("Decompressed: " + str(len(dec)))

            rv_before = dec.count(b"renpy.revertable")
            rp_before = dec.count(b"renpy.python")
            log.append("BEFORE - 'renpy.revertable': " + str(rv_before))
            log.append("BEFORE - 'renpy.python': " + str(rp_before))

            if rv_before == 0:
                log.append("SKIP: No incompatible references found")
                return log

            dec = dec.replace(b"renpy.revertable\n", b"renpy.python\n")

            rv_after = dec.count(b"renpy.revertable")
            rp_after = dec.count(b"renpy.python")
            log.append("AFTER  - 'renpy.revertable': " + str(rv_after))
            log.append("AFTER  - 'renpy.python': " + str(rp_after))

            compressed = zlib.compress(dec)
            with open(per_path, "wb") as f:
                f.write(compressed)
            log.append("FIXED: Wrote " + str(len(compressed)) + " bytes")
            log.append("STATUS: COMPATIBLE with 6.99.12")

        except Exception as e:
            log.append("ERROR: " + str(type(e).__name__) + ": " + str(e))

        return log

    try:
        if hasattr(config, "python_exit_callbacks"):
            config.python_exit_callbacks.append(_compat_fixup_persistent)
    except:
        pass


python early:
    import os
    import sys
    import re

    """
    ANDROID FORCE SAVE PATH - EARLY INIT
    Executes before ANY init block to override Ren'Py's default save location detection.
    This ensures config.savedir is set to our custom "Backpack" path immediately.
    """
    is_android = renpy.android or "ANDROID_ARGUMENT" in os.environ or "ANDROID_PRIVATE" in os.environ
    
    if is_android:
        """
        Disables auto-save path detection to prevent Ren'Py from using the default
        internal storage path.
        """
        config.save_directory = None
        
        """
        Forces the save directory to the external storage path.
        """
        config.savedir = "/storage/emulated/0/Monika After Story/game/saves"
        
        """
        Aggressively creates the save directory if it doesn't exist, ensuring
        Ren'Py has a valid target before initialization continues.
        """
        try:
            if not os.path.exists(config.savedir):
                os.makedirs(config.savedir)
        except:
            pass
        
        pass

        """
        Injects external submod paths into config.searchpath.
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
            
            for cand in candidates:
                if os.path.exists(cand):
                    ext_submods_dir = cand
                    break
            
            if ext_submods_dir:
                if ext_submods_dir not in config.searchpath:
                    config.searchpath.append(ext_submods_dir)

            """
            Adds the external 'game' folder to the search path to allow submods
            to access assets via standard paths.
            """
            ext_game_dir = mas_root + "/game"
            if os.path.exists(ext_game_dir):
                if ext_game_dir not in config.searchpath:
                    config.searchpath.append(ext_game_dir)
            
            """
            Adds external 'python-packages' to sys.path to support submods
            that rely on custom python libraries.
            """
            import sys
            ext_packages_dir = mas_root + "/game/python-packages"
            if os.path.exists(ext_packages_dir):
                if ext_packages_dir not in sys.path:
                    sys.path.append(ext_packages_dir)

        except Exception as e:
            print("[ANDROID_EARLY] Error: " + str(e))


init -999 python:
    import os
    import shutil
    import platform

    """
    PATHS & CONSTANTS
    Defines the standard public paths for Android storage.
    """
    ANDROID_PUBLIC_PATH = "/storage/emulated/0/Monika After Story/"
    
    if renpy.android:
        """
        Overrides the base directory to point to the external public path.
        """
        renpy.config.basedir = ANDROID_PUBLIC_PATH
        
        """
        Sets the internal log directory based on the private files path.
        This ensures Ren'Py writes the master log to a valid location.
        """
        try:
            _private_files = os.environ.get("ANDROID_PRIVATE", "")
            if _private_files:
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
    PUBLIC STORAGE SETUP
    Defines constants for critical subdirectories.
    """
    ANDROID_CHARACTERS_PATH = os.path.join(ANDROID_PUBLIC_PATH, "characters/")
    ANDROID_CHESS_PATH = os.path.join(ANDROID_PUBLIC_PATH, "chess_games/")
    ANDROID_LOG_PATH = os.path.join(ANDROID_PUBLIC_PATH, "log/")
    ANDROID_SAVES_PATH = os.path.join(ANDROID_PUBLIC_PATH, "game/saves/")
    ANDROID_CUSTOM_BGM_PATH = os.path.join(ANDROID_PUBLIC_PATH, "custom_bgm/")
    
    def mas_android_setup_public_storage():
        """
        Creates the necessary folder structure in public storage to ensure
        all game features have write access.
        """
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
            os.path.join(ANDROID_PUBLIC_PATH, "game/mod_assets/monika/t/"),
            os.path.join(ANDROID_PUBLIC_PATH, "textures/"),
            os.path.join(ANDROID_PUBLIC_PATH, "textures/monika/"),
            os.path.join(ANDROID_PUBLIC_PATH, "textures/monika/eyes/"),
            os.path.join(ANDROID_PUBLIC_PATH, "textures/monika/mouth/"),
            os.path.join(ANDROID_PUBLIC_PATH, "textures/games/"),
            os.path.join(ANDROID_PUBLIC_PATH, "textures/games/pong/"),
            os.path.join(ANDROID_PUBLIC_PATH, "textures/games/nou/"),
            os.path.join(ANDROID_PUBLIC_PATH, "textures/games/chess/")            
        ]

        for d in dirs_to_create:
            if not os.path.exists(d):
                try:
                    os.makedirs(d)
                except Exception as e:
                    print("Error creating " + d + ": " + str(e))
            else:
                pass
    
    mas_android_setup_public_storage()


init python:
    """
    JNI HELPERS & PERMISSIONS
    Imports necessary Android classes via JNI/Pyjnius.
    """
    if renpy.android:
        from jnius import autoclass
        
        """
        ANDROID STANDARD CLASSES
        """
        _Environment = autoclass('android.os.Environment')
        _Intent = autoclass('android.content.Intent')
        _Settings = autoclass('android.provider.Settings')
        _Uri = autoclass('android.net.Uri')
        _VERSION = autoclass('android.os.Build$VERSION')
        _PackageManager = autoclass('android.content.pm.PackageManager')

        """
        ACTIVITY CLASSES
        Safely loads the Ren'Py activity class.
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
        """
        Returns the current running Android Activity context.

        RETURNS:
            The current activity object or None
        """
        if not renpy.android: return None
        act = None
        if _PythonSDLActivity:
            try: act = _PythonSDLActivity.mActivity
            except: pass 
        if act is None and _PythonActivity:
            try: act = _PythonActivity.mActivity
            except: pass
        return act

    def mas_android_check_and_request_permissions():
        """
        Checks and requests necessary runtime permissions based on Android SDK version.
        Handles both legacy storage permissions and modern 'Manage All Files' access.
        """
        if not renpy.android: return 
        CurrentActivity = mas_get_current_activity()
        if CurrentActivity is None: return

        sdk_int = _VERSION.SDK_INT
        
        """
        STORAGE PERMISSIONS
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
        NOTIFICATION PERMISSIONS (Android 13+)
        """
        if sdk_int >= 33:
            CurrentActivity.requestPermissions(["android.permission.POST_NOTIFICATIONS"], 101)


    def mas_get_native_lib_dir():
        """
        Returns the path to the native library directory for the current application.
        """
        if not renpy.android: return None
        try:
            CurrentActivity = mas_get_current_activity()
            if not CurrentActivity: return None
            return CurrentActivity.getApplicationContext().getApplicationInfo().nativeLibraryDir
        except Exception as e:
            return None

    def mas_android_has_permission():
        """
        Verifies if the necessary storage permissions have been granted.

        RETURNS:
            True if permissions are granted, False otherwise
        """
        if not renpy.android: return True
        try:
            CurrentActivity = mas_get_current_activity()
            if not CurrentActivity: return False
            sdk = _VERSION.SDK_INT
            if sdk >= 30:
                return _Environment.isExternalStorageManager()
            else:
                res = CurrentActivity.checkSelfPermission("android.permission.WRITE_EXTERNAL_STORAGE")
                return (res == _PackageManager.PERMISSION_GRANTED)
        except:
            return False


init 50 python:
    """
    SUBMOD LOADER
    Manually scans and loads submod .rpy scripts from the external directory.
    This bypasses Ren'Py's internal restrictions on external asset loading.
    """
    if renpy.android:
        import os
        
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
            known_files = set(renpy.list_files())
            
            for root, dirs, files in os.walk(ext_loader_dir):
                for f in files:
                    if f.endswith(".rpy"):
                        full_path = os.path.join(root, f)
                        rel_path = os.path.relpath(full_path, ext_loader_dir).replace("\\", "/")
                        
                        if rel_path in known_files:
                            continue
                            
                        try:
                            with open(full_path, "rb") as f_obj:
                                content_bytes = f_obj.read()
                            
                            content_unicode = None
                            for enc in ["utf-8", "latin-1", "cp1252"]:
                                try:
                                    content_unicode = content_bytes.decode(enc)
                                    break
                                except:
                                    continue
                                    
                            if content_unicode:
                                renpy.load_string(content_unicode, filename=full_path)
                            else:
                                print("[ANDROID_LOADER] ERROR: Could not decode " + f)
                                
                        except Exception as e:
                            print("ERROR loading " + f + ": " + str(e))
                            import traceback
                            traceback.print_exc()
                            
            """
            Here we apply monkey patches to inject necessary globals into
            loaded submods that might be missing context.
            """
            try:
                if store.mas_compliments:
                    store.mas_compliments.mas_get_player_nickname = mas_get_player_nickname
            except:
                pass

            """
            UNIVERSAL SUBMOD DATABASE AUTO-REGISTRATION [The Encoders Club]

            Problem: submods like NSFW register their custom event databases
            into mas_all_ev_db_map inside an 'init 5 python:' block, but that
            block runs BEFORE the 'init python in nsfw_fetish:' blocks that
            create the module objects. On Android, when renpy.load_string()
            processes the submod files in init priority order, the init 5
            registrar runs first and fails silently because store.nsfw_fetish
            doesn't exist yet. So NFH/NST never enter mas_all_ev_db_map.

            Solution: After ALL load_string() calls have completed (so all
            modules and their __init__ blocks are fully set up), scan every
            store sub-module for dict attributes that look like event databases
            (contain MAS Event objects) and register them into mas_all_ev_db_map
            if they are not already registered. Uses an auto-generated code
            derived from the attribute name.
            """
            try:
                import types as _types

                # IDs of dicts already registered so we skip them
                _already_registered_ids = set(
                    id(db) for db in store.mas_all_ev_db_map.values()
                )

                # Build a reverse map: id(db) -> code, for resync use later
                _id_to_code = {
                    id(db): code
                    for code, db in store.mas_all_ev_db_map.iteritems()
                }

                _ev_class = store.Event

                for _mod_name in dir(store):
                    try:
                        _mod = getattr(store, _mod_name)
                    except:
                        continue

                    if not isinstance(_mod, _types.ModuleType):
                        continue

                    for _attr in dir(_mod):
                        if not (_attr.endswith("_database") or _attr.endswith("_db")):
                            continue
                        try:
                            _db = getattr(_mod, _attr)
                        except:
                            continue

                        if not isinstance(_db, dict) or len(_db) == 0:
                            continue

                        if id(_db) in _already_registered_ids:
                            continue

                        # Confirm it's a MAS-style event database by checking
                        # that at least one value is an Event instance
                        _sample = next(_db.itervalues(), None)
                        if _sample is None or not isinstance(_sample, _ev_class):
                            continue

                        # Auto-generate a 3-letter code from the attribute name
                        # e.g. nsfw_fetish_database -> NFH (first letters of parts)
                        _parts = _attr.replace("_database", "").replace("_db", "").split("_")
                        _parts = [p for p in _parts if p]
                        _auto_code = "".join(p[0].upper() for p in _parts[:3]).ljust(3, "X")

                        # Avoid collisions with existing codes
                        _suffix = 0
                        _candidate = _auto_code
                        while _candidate in store.mas_all_ev_db_map:
                            _suffix += 1
                            _candidate = _auto_code[:2] + str(_suffix)

                        store.mas_all_ev_db_map[_candidate] = _db
                        _already_registered_ids.add(id(_db))
                        _id_to_code[id(_db)] = _candidate
                        print(
                            "[ANDROID_LOADER] Auto-registered submod db: "
                            + _mod_name + "." + _attr
                            + " as code [" + _candidate + "] with "
                            + str(len(_db)) + " events"
                        )
            except Exception as _e:
                import traceback as _tb
                print("[ANDROID_LOADER] Error in db auto-registration: " + str(_e))
                _tb.print_exc()

        """
        Rebuilds the aggregate event database to include events from
        externally loaded submods, which were added after the initial
        build at init 6.
        """
        try:
            store.mas_all_ev_db = {}
            for code, ev_db in store.mas_all_ev_db_map.iteritems():
                store.mas_all_ev_db.update(ev_db)
        except:
            pass

        """
        Resyncs module-level database references that may have been
        overwritten by renpy.load_string(). When a submod has blocks like
        'init python in mas_compliments:', Ren'Py executes them and the
        module's dict reference gets replaced with a new empty dict. But
        mas_all_ev_db_map (built at init 4) still holds the ORIGINAL
        dicts where addEvent() stored all events.
        """
        try:
            store.evhand.event_database = store.mas_all_ev_db_map["EVE"]
            store.evhand.farewell_database = store.mas_all_ev_db_map["BYE"]
            store.evhand.greeting_database = store.mas_all_ev_db_map["GRE"]
            store.mas_compliments.compliment_database = store.mas_all_ev_db_map["CMP"]
            store.mas_moods.mood_db = store.mas_all_ev_db_map["MOO"]
            store.mas_stories.story_database = store.mas_all_ev_db_map["STY"]
            store.mas_songs.song_db = store.mas_all_ev_db_map["SNG"]
            store.mas_games.game_db = store.mas_all_ev_db_map["GME"]
        except:
            pass



init python:
    """
    UNIVERSAL SUBMOD DB SYNC - POST-LOAD HOOK

    Root cause discovered: Ren'Py's save/load system restores store module
    variables (including nsfw_fetish.nsfw_fetish_database) from the save file
    AFTER all init blocks run. Any update() done in init 7 gets overwritten
    by the save restoration.

    Fix: register a callback that fires AFTER the save is loaded (after_load)
    and also AFTER a new game starts (start). At those points, sync the module
    db attributes in-place from mas_all_ev_db_map, which is NOT overwritten
    because it is rebuilt from scratch by addEvent at init 6.

    This runs at the correct moment: after save restoration, before gameplay.
    """
    if renpy.android:
        import types as _cb_types

        def _mas_android_resync_submod_dbs():
            """
            Syncs submod module db attributes in-place from mas_all_ev_db_map.
            Called after every save load and new game start on Android.
            """
            _STANDARD_CODES = {"EVE", "BYE", "GRE", "CMP", "MOO", "STY", "SNG", "GME"}
            try:
                for _cb_code, _cb_db in store.mas_all_ev_db_map.iteritems():
                    if _cb_code in _STANDARD_CODES:
                        continue
                    if not _cb_db:
                        continue

                    # Identify the owning module via common event label prefix
                    _cb_labels = list(_cb_db.keys())
                    if not _cb_labels:
                        continue

                    _cb_common = _cb_labels[0]
                    for _cb_lbl in _cb_labels[1:]:
                        while not _cb_lbl.startswith(_cb_common):
                            _cb_common = _cb_common[:-1]
                            if not _cb_common:
                                break
                        if not _cb_common:
                            break

                    _cb_common = _cb_common.rstrip("_")
                    if not _cb_common:
                        continue

                    # Find the store module by progressively shorter prefix
                    _cb_parts = _cb_common.split("_")
                    _cb_mod = None
                    _cb_mod_name = None
                    for _cb_n in range(len(_cb_parts), 0, -1):
                        _cb_try = "_".join(_cb_parts[:_cb_n])
                        try:
                            _cb_obj = getattr(store, _cb_try)
                            if isinstance(_cb_obj, _cb_types.ModuleType):
                                _cb_mod = _cb_obj
                                _cb_mod_name = _cb_try
                                break
                        except AttributeError:
                            continue

                    if _cb_mod is None:
                        continue

                    # Update the module db attribute in-place
                    for _cb_attr in [_cb_mod_name + "_database", _cb_mod_name + "_db"]:
                        try:
                            _cb_existing = getattr(_cb_mod, _cb_attr)
                        except AttributeError:
                            continue
                        if not isinstance(_cb_existing, dict):
                            continue
                        if id(_cb_existing) == id(_cb_db):
                            break  # Already the same object
                        if len(_cb_existing) == 0 or len(_cb_existing) < len(_cb_db):
                            _cb_existing.update(_cb_db)
                            print(
                                "[ANDROID_SETUP resync] "
                                + _cb_mod_name + "." + _cb_attr
                                + " <- [" + _cb_code + "] "
                                + str(len(_cb_db)) + " events"
                            )
                        break
            except Exception as _cb_e:
                print("[ANDROID_SETUP resync] Error: " + str(_cb_e))

        # Register for BOTH new game start and save loading
        try:
            if not hasattr(config, "start_callbacks"):
                config.start_callbacks = []
            config.start_callbacks.append(_mas_android_resync_submod_dbs)
        except:
            pass
        try:
            if not hasattr(config, "after_load_callbacks"):
                config.after_load_callbacks = []
            config.after_load_callbacks.append(_mas_android_resync_submod_dbs)
        except:
            pass


    """
    FEATURE OVERRIDES
    Handlers for Stockfish binary extraction and Logging redirection.
    """
    def mas_extract_stockfish():
        """
        Extracts the Stockfish binary from the APK to the app's private
        files directory so it can be executed.
        """
        if not renpy.android: return None
        try:
            import zipfile
            import sys
            
            is_64_bit = sys.maxsize > 2**32
            target_abi = "arm64-v8a" if is_64_bit else "armeabi-v7a"
            
            CurrentActivity = mas_get_current_activity()
            if not CurrentActivity: return None
            
            context = CurrentActivity.getApplicationContext()
            apk_path = context.getApplicationInfo().publicSourceDir
            private_dir = os.environ.get("ANDROID_PRIVATE", "")
            out_file = os.path.join(private_dir, "stockfish_bin")
            
            with zipfile.ZipFile(apk_path, "r") as z:
                target_entry = "lib/" + target_abi + "/libstockfish.so"
                if target_entry not in z.namelist():
                    return None
                    
                with open(out_file, "wb") as f:
                    f.write(z.read(target_entry))
            
            os.chmod(out_file, 0o755)
            return out_file
            
        except Exception as e:
            return None

    if renpy.android:
        if mas_android_has_permission():
            
            if hasattr(store, 'mas_chess'):
                store.mas_chess.CHESS_SAVE_PATH = ANDROID_CHESS_PATH
                sf_path = mas_extract_stockfish()
                if sf_path:
                    store.mas_chess.STOCKFISH_PATH = sf_path
                else:
                    p_dir = os.environ.get('ANDROID_PRIVATE', '')
                    store.mas_chess.STOCKFISH_PATH = os.path.join(p_dir, "files", "stockfish_bin")
            
            if hasattr(store, 'mas_docking_station'):
                store.mas_docking_station.station = ANDROID_CHARACTERS_PATH
                if not os.path.isdir(ANDROID_CHARACTERS_PATH):
                    try: os.makedirs(ANDROID_CHARACTERS_PATH)
                    except: pass

            """
            Redirects Python logging to the external storage folder.
            This ensures logs are accessible without root access.
            """
            from store.mas_logging import loghandlers
            import logging
            root_logger = logging.getLogger()
            
            try:
                log_file = os.path.join(ANDROID_LOG_PATH, "mas_log.txt")
                hdlr = loghandlers.RotatingFileHandler(
                    log_file, 
                    maxBytes=5242880, 
                    backupCount=5
                )
                formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
                hdlr.setFormatter(formatter)
                root_logger.addHandler(hdlr)

                extra_loggers = ["aff_log", "pnm", "submod_log", "spj", "mfgen"]
                for log_name in extra_loggers:
                    try:
                        tgt_log = logging.getLogger(log_name)
                        for h in tgt_log.handlers[:]:
                            tgt_log.removeHandler(h)
                            h.close()
                        
                        l_file = os.path.join(ANDROID_LOG_PATH, log_name + ".txt")
                        l_hdlr = loghandlers.RotatingFileHandler(
                            l_file, maxBytes=5242880, backupCount=5
                        )
                        l_hdlr.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
                        tgt_log.addHandler(l_hdlr)
                    except: pass
            except: pass
        else:
            pass


init 10 python:
    """
    NOTIFICATION CLEANUP - STARTUP EXECUTION
    This logic is placed here to group it with the Notification Cleanup section,
    but it runs at Priority 10 to ensure the backend functions (init -5) are fully loaded first.
    """

    
    if store.mas_android_cancel_standard_only:
        try:
            store.mas_android_cancel_standard_only()
        except:
            pass


    if store.mas_android_cancel_type_sleep:
        try:
            store.mas_android_cancel_type_sleep()
        except:
            pass

    
    if store.mas_android_cancel_valentine:
        try:
            import datetime
            today = datetime.date.today()
            if today.month == 2 and today.day == 14:
                store.mas_android_cancel_valentine()
        except:
            pass



init python:
    
    def mas_android_check_readme():
        """
        Checks if the README file exists in public storage.
        If missing or outdated, exacts it from the APK assets.
        """
        if not renpy.android: return

        try:
            target_path = os.path.join(ANDROID_PUBLIC_PATH, "README.html")
            import zipfile
            CurrentActivity = mas_get_current_activity()
            if not CurrentActivity: return
            
            context = CurrentActivity.getApplicationContext()
            apk_path = context.getApplicationInfo().publicSourceDir
            
            with zipfile.ZipFile(apk_path, "r") as z:
                readme_candidates = [f for f in z.namelist() if f.lower().endswith("readme.html")]
                readme_candidates.sort(key=len)
                
                if readme_candidates:
                    found_entry = readme_candidates[0]
                    do_extract = False
                    
                    if not os.path.exists(target_path):
                        do_extract = True
                    else:
                        apk_info = z.getinfo(found_entry)
                        local_size = os.path.getsize(target_path)
                        if apk_info.file_size != local_size:
                            do_extract = True
                            
                    if do_extract:
                        with open(target_path, "wb") as f:
                            f.write(z.read(found_entry))

        except:
            pass

    mas_android_check_readme()

    def mas_android_copy_logs():
        """
        Runs on Quit to sync critical log files from internal private storage
        to the external public folder, ensuring they are accessible to the user.
        Also translates standard Ren'Py error messages to Spanish.
        """
        if not renpy.android: return
        import os
        import sys
        
        try:
            sys.stdout.flush()
            sys.stderr.flush()
        except: pass

        sources = []
        private_dir = os.environ.get("ANDROID_PRIVATE", "")
        if private_dir:
            sources.append(private_dir)
            sources.append(os.path.join(private_dir, "files"))
        
        if hasattr(renpy.config, "log_directory") and renpy.config.log_directory:
            sources.append(renpy.config.log_directory)
        
        try:
            from jnius import autoclass
            act = mas_get_current_activity()
            if act:
                ext_files = act.getExternalFilesDir(None)
                if ext_files: sources.append(ext_files.getAbsolutePath())
        except: pass
        sources.append(os.getcwd())

        def find_best_source(filename):
            """
            Scans all potential source directories to find the most likely
            location of the requested log file.
            """
            for src in sources:
                fpath = os.path.join(src, filename)
                if os.path.exists(fpath):
                    return fpath
            return None

        def copy_and_mask_log(source_path, dest_filename):
            """
            Copies the log file to the public logging directory, applying
            Spanish translations to standard error headers.
            """
            if not source_path: return
            try:
                with open(source_path, "r") as f:
                    content = f.read()
                
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
                for en, es in replacements.items():
                    if en in content: content = content.replace(en, es)
                
                dest_path = os.path.join(store.ANDROID_PUBLIC_PATH, dest_filename)
                with open(dest_path, "w") as f:
                    f.write(content)
            except: pass

        copy_and_mask_log(find_best_source("log.txt"), "log.txt")
        copy_and_mask_log(find_best_source("traceback.txt"), "traceback.txt")

    def mas_android_rescue_saves():
        """
        Attempts to rescue save files from the internal private directory
        and move them to the external public folder if they are stranded.
        """
        if not renpy.android: return
        if config.savedir != ANDROID_SAVES_PATH: return
        try:
            private_dir = os.environ.get('ANDROID_PRIVATE', '')
            internal_saves = os.path.join(private_dir, "files/saves")
            if os.path.exists(internal_saves):
                for f in os.listdir(internal_saves):
                    src = os.path.join(internal_saves, f)
                    dst = os.path.join(ANDROID_SAVES_PATH, f)
                    if os.path.isfile(src) and not os.path.exists(dst):
                        shutil.copy2(src, dst)
        except: pass
    
    mas_android_rescue_saves()

    def mas_android_open_help():
        """
        Attempts to open the README.html file using an external intent.
        Uses StrictMode overrides to allow FileUri exposure.
        """
        import os, webbrowser
        path = store.ANDROID_PUBLIC_PATH
        if not path: return
        readme_path = os.path.join(path, "README.html")
        encoded_url = "file://" + readme_path.replace(" ", "%20")
        try:
            from jnius import autoclass
            Intent = autoclass("android.content.Intent")
            Uri = autoclass("android.net.Uri")
            File = autoclass("java.io.File")
            StrictMode = autoclass("android.os.StrictMode")
            Builder = autoclass("android.os.StrictMode$VmPolicy$Builder")
            
            StrictMode.setVmPolicy(Builder().build())
            intent = Intent(Intent.ACTION_VIEW)
            intent.setDataAndType(Uri.fromFile(File(readme_path)), "text/html")
            intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
            mas_get_current_activity().startActivity(intent)
        except:
            try: webbrowser.open(encoded_url)
            except: pass


init 500 python:
    """
    INTENT HANDLER
    Checks if the game was launched via a notification by inspecting the Intent extras.
    Rewards affection and cleans up notifications if true.
    """
    mas_android_intent_checked = False
    def mas_android_check_notif_launch(label, abnormal):
        global mas_android_intent_checked
        if mas_android_intent_checked: return
        if label == "ch30_init":
            mas_android_intent_checked = True
            if not renpy.android: return
            try:
                intent = mas_get_current_activity().getIntent()
                if intent.getBooleanExtra("launch_from_notif", False):
                    if hasattr(store, "mas_gainAffection"):
                        store.mas_gainAffection(1.0, bypass=True)
                        if hasattr(store, "mas_android_cancel_all_notifs"):
                            store.mas_android_cancel_all_notifs()
                        if hasattr(store, "mas_android_clear_active_notifications"):
                            store.mas_android_clear_active_notifications()
            except: pass
    
    config.label_callback = mas_android_check_notif_launch


init 999 python:
    """
    LATE ANDROID CLEANUP & CRASH VERSION CALCULATION
    """
    if renpy.android:
        store.mas_android_cancel_all_notifs()
        if hasattr(store, "mas_android_clear_active_notifications"):
            store.mas_android_clear_active_notifications()
        config.after_load_callbacks.append(store.mas_android_cancel_all_notifs)
    
    """
    Calculates the crash version string safely at the end of initialization
    to ensure all config variables are loaded.
    """
    mas_CRASH_MAP = {
        "Parsing the script failed.": "Fallo al analizar el script.",
        "Ren'Py has detected that...": "Ren'Py ha detectado que...",
        "After initialization, but before game start.": "Tras la inicialización, pero antes de iniciar el juego:",
        "I'm sorry, but an uncaught exception occurred.": "Lo sentimos, pero ha ocurrido un error inesperado.",
        "An exception has occurred.": "Ha ocurrido un error.",
    }

    def mas_get_version_info():
        """
        Dynamically calculates the version info string for the crash screen.
        Safe to call at any point in the init process.
        """
        try:
            _v1 = str(config.version) if config.version else "Unknown"
            _v2 = str(renpy.version_string).replace("Ren'Py ", "") if renpy.version_string else "Unknown"
            _v3 = str(renpy.platform) if renpy.platform else "Unknown"
            return "{}\\n{}\\n{}".format(_v1, _v2, _v3)
        except:
            return "Versión: Error"

    def mas_format_traceback_spanish(s):
        """
        Translates the standard Ren'Py traceback to Spanish.
        
        IN:
            s - Original traceback string
        
        RETURNS:
            Translated string
        """
        if not s: return s

        for en, es in mas_CRASH_MAP.items():
            if en in s:
                s = s.replace(en, es)

        s = s.replace("While running game code:", "Mientras se ejecutaba el código del juego:")
        s = s.replace("Full traceback:", "Rastreo completo:")
        s = s.replace("The full traceback has been saved in a file named:", "El reporte completo se ha guardado en el archivo:")
        s = s.replace("The full traceback has been saved to:", "El reporte completo se ha guardado en:")
        s = s.replace("Mon ", "Lun ").replace("Tue ", "Mar ").replace("Wed ", "Mié ").replace("Thu ", "Jue ").replace("Fri ", "Vie ").replace("Sat ", "Sáb ").replace("Sun ", "Dom ")
        s = s.replace(" Jan ", " Ene ").replace(" Feb ", " Feb ").replace(" Mar ", " Mar ").replace(" Apr ", " Abr ").replace(" May ", " May ").replace(" Jun ", " Jun ")
        s = s.replace(" Jul ", " Jul ").replace(" Aug ", " Ago ").replace(" Sep ", " Sep ").replace(" Oct ", " Oct ").replace(" Nov ", " Nov ").replace(" Dec ", " Dic ")
        return s
        
    def mas_rewrite_traceback_file(fn):
        """
        Rewrites the traceback file on disk to ensure it opens in Spanish.
        
        IN:
            fn - filename to rewrite
        """
        try:
            import os
            if not fn or not os.path.exists(fn): return
            with open(fn, "rb") as f:
                content = f.read().decode("utf-8")
            new_content = mas_format_traceback_spanish(content)
            if new_content != content:
                with open(fn, "wb") as f:
                    f.write(new_content.encode("utf-8"))
        except: pass
        return True

    def mas_get_formatted_traceback(s):
        """
        Formats the traceback string for display on the screen, adding
        links to files and lines.

        IN:
            s - Traceback string

        RETURNS:
            Formatted string for text displayable
        """
        try:
            s = mas_format_traceback_spanish(s)
            lines = [ i.replace("{", "{{") for i in s.split("\\n") ]
            import re
            rv = []
            if lines:
                header_size = int(gui._scale(22))
                rv.append(u"{{size={}}}{}{{/size}}".format(header_size, lines[0]))
            for i in lines[1:]:
                i = re.sub(r'(File "(.*)", line (\d+))', r'{a=edit:\3:\2}\1{/a}', i)
                rv.append("  " + i)
            return "\\n".join(rv)
            return s
        except Exception as e:
            return s

    def mas_get_exception_title(s):
        """
        Parses the exception string to return a localized Spanish title based on the error header.

        IN:
            s - Short exception string

        RETURNS:
            Localized title
        """
        if not s: return "Ha ocurrido un error."

        for en, es in mas_CRASH_MAP.items():
            if en in s:
                return es

        return "Ha ocurrido un error."

    class MasErrorQuit(Action):
        def __call__(self): renpy.quit(status=1)
    
    class MasReload(Action):
        def __call__(self): renpy.utter_restart()

    class MasTooltip(object):
        def __init__(self, default):
            self.value = default
            self.default = default
        def action(self, value):
            return SetField(self, "value", value)

    class MasCopyFile(Action):
        def __init__(self, filename): self.filename = filename
        def __call__(self):
            import pygame.scrap
            try:
                with open(self.filename, "rb") as f:
                    f.read(3) 
                    s = u"[code]\\n{}[/code]\\n".format(f.read().decode("utf-8"))
                s = s.replace("\\n", "\\r\\n").replace("\\r\\r", "\\r")
                pygame.scrap.put(pygame.SCRAP_TEXT, s.encode("utf-8"))
                renpy.notify("Copiado al portapapeles.")
            except: renpy.notify("Error al copiar.")

    class MasCopyMarkdown(Action):
        def __init__(self, filename): self.filename = filename
        def __call__(self):
            import pygame.scrap
            try:
                with open(self.filename, "rb") as f:
                    f.read(3)
                    s = u"```\\n{}\\n```\\n".format(f.read().decode("utf-8"))
                s = s.replace("\\n", "\\r\\n").replace("\\r\\r", "\\r")
                pygame.scrap.put(pygame.SCRAP_TEXT, s.encode("utf-8"))
                renpy.notify("Copiado Markdown al portapapeles.")
            except: renpy.notify("Error al copiar.")

    class MasOpenFileAction(Action):
        def __init__(self, filename): self.filename = filename
        def __call__(self):
            try:
                renpy.notify("Abriendo: " + str(self.filename))
                if globals().get("mas_android_open_help"):
                    import webbrowser
                    webbrowser.open("file://" + self.filename)
                else:
                    renpy.launch_editor([self.filename], 1)
            except: pass


"""
SCREEN OVERRIDE
The actual screen definition that overrides Ren'Py's internal _exception screen.
"""
screen _exception:
    modal True
    zorder 1090
    
    default _rewrite_trigger = mas_rewrite_traceback_file(traceback_fn)
    default tt = MasTooltip("")
    default fmt_short = mas_get_formatted_traceback(short)

    default fmt_full = mas_get_formatted_traceback(full)
    default failure_title = mas_get_exception_title(short)

    frame:
        style_group ""
        has side "t c b":
            spacing gui._scale(10)


        fixed:
            ysize gui._scale(60) 
            

            text failure_title size gui._scale(40) align (0.0, 0.0)
            

        vbox:
            align (1.0, 0.0)
            text mas_get_version_info() text_align 1.0 size gui._scale(14) bold False

        viewport:
            id "viewport"
            child_size (4000, None)
            mousewheel True
            draggable True
            scrollbars "both"

            has vbox
            text fmt_short substitute False
            text fmt_full substitute False

        vbox:
            hbox:
                spacing gui._scale(25)

                if rollback_action:
                    textbutton "Retroceder":
                        action rollback_action
                        hovered tt.action("Intenta volver a un momento anterior para guardar o elegir diferente.")

                if ignore_action:
                    textbutton "Ignorar":
                        action ignore_action
                        hovered tt.action("Ignora la excepción y continúa. Esto suele provocar más errores.")

                if config.developer and not renpy.mobile:
                    textbutton "Recargar":
                        action MasReload()
                        hovered tt.action("Recarga el juego desde el disco, restaurando el estado si es posible.")

                textbutton "Abrir":
                    action MasOpenFileAction(traceback_fn)
                    hovered tt.action("Abre el archivo traceback.txt en un editor de texto.")

                textbutton "Copiar BBCode":
                    action MasCopyFile(traceback_fn)
                    hovered tt.action("Copia el archivo traceback.txt al portapapeles como BBcode para foros.")

                textbutton "Copiar Markdown":
                    action MasCopyMarkdown(traceback_fn)
                    hovered tt.action("Copia el archivo traceback.txt al portapapeles como Markdown para Discord.")

                vbox:
                    xfill True
                    textbutton "Salir":
                        xalign 1.0
                        action Quit(confirm=False)
                        hovered tt.action("Salir del juego.")

            text tt.value