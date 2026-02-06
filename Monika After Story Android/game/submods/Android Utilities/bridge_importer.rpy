init -999 python:
    import json
    import os
    import datetime
    import shutil

    # Define the bridge file path
    # config.savedir on Windows typically points to %APPDATA%/RenPy/Monika After Story
    MAS_BRIDGE_FILE = os.path.join(config.savedir, "monika_bridge.json").replace("\\", "/")
    # MAS_BRIDGE_LOG = os.path.join(config.savedir, "bridge_log.txt").replace("\\", "/")

    def mas_bridge_log(msg):
        pass
        # try:
        #     with open(MAS_BRIDGE_LOG, "a") as f:
        #         f.write(str(msg) + "\n")
        #         f.flush()
        #         os.fsync(f.fileno())
        # except:
        #     pass
    # ... (keep mas_bridge_reconstruct_key and mas_bridge_reconstruct as is) ...

    def mas_bridge_reconstruct_key(k):
        """
        Reconstructs a key from its string representation.
        """
        if not isinstance(k, basestring):
            return k
            
        if k.startswith("__bridge_k_T__"):
            val = k.replace("__bridge_k_T__", "")
            try:
                if "." in val:
                    return datetime.datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    return datetime.datetime.strptime(val, "%Y-%m-%dT%H:%M:%S")
            except:
                return val
        elif k.startswith("__bridge_k_D__"):
            val = k.replace("__bridge_k_D__", "")
            try:
                return datetime.datetime.strptime(val, "%Y-%m-%d").date()
            except:
                return val
        return k

    def mas_bridge_reconstruct(data, depth=0):
        """
        Recursively reconstructs data from JSON-safe format.
        Restores datetime and date objects from their tagged representation.
        Also restores KEYS.
        """
        if isinstance(data, dict):
            # Robust Bridge Object Detection
            # We iterate keys to handle potential unicode/str mismatches in Python 2
            b_type = None
            val = None
            
            # Helper to find key irrespective of encoding
            for k in data.keys():
                sk = str(k)
                if sk == "__bridge_type__":
                    b_type = data[k]
                elif sk == "value":
                    val = data[k]
            
            if b_type:
                # Log detection of bridge object (only first few to avoid spam)
                if depth < 2:
                    mas_bridge_log("Found bridge object type: " + str(b_type))
                
                # Normalize types
                b_type = str(b_type)
                
                if val is None:
                    mas_bridge_log("ERROR: Object " + b_type + " has no value.")
                    return None
                
                if b_type == "datetime":
                    try:
                        # Try full format with microseconds
                        if "." in val:
                            return datetime.datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                        # Try seconds only
                        else:
                            return datetime.datetime.strptime(val, "%Y-%m-%dT%H:%M:%S")
                    except:
                        # Fallback suite
                        try:
                            return datetime.datetime.strptime(val, "%Y-%m-%d %H:%M:%S.%f")
                        except:
                            try:
                                return datetime.datetime.strptime(val, "%Y-%m-%d %H:%M:%S")
                            except Exception as e:
                                mas_bridge_log("ERROR parsing datetime '" + str(val) + "': " + str(e))
                                return None

                elif b_type == "date":
                    try:
                        return datetime.datetime.strptime(val, "%Y-%m-%d").date()
                    except Exception as e:
                        mas_bridge_log("ERROR parsing date '" + str(val) + "': " + str(e))
                        return None
                
                else:
                    # Unknown type, log warning but don't crash, return None
                    mas_bridge_log("WARNING: Unknown bridge type: " + str(b_type))
                    return None

            # Normal Dict: Recursive with key reconstruction
            new_dict = {}
            for k, v in data.items():
                new_key = mas_bridge_reconstruct_key(k)
                new_dict[new_key] = mas_bridge_reconstruct(v, depth+1)
            return new_dict
            
        elif isinstance(data, list):
            return [mas_bridge_reconstruct(v, depth+1) for v in data]
        
        return data
    def mas_bridge_restore():
        """
        Checks for bridge file and restores data.
        """
        mas_bridge_log("--------------------------------------------------")
        mas_bridge_log("Bridge Init Started. Path: " + MAS_BRIDGE_FILE)

        # DIAGNOSTIC: Check persistent.sessions BEFORE import
        if hasattr(persistent, "sessions"):
            mas_bridge_log("PRE-IMPORT: persistent.sessions exists.")
        else:
            mas_bridge_log("PRE-IMPORT: persistent.sessions does NOT exist.")

        # SANITIZATION: NUCLEAR OPTION
        # Unconditionally delete history saved data cache to prevent dictionary-datetime crashes.
        # This data is just internal scheduling triggers and will be safely regenerated by MAS.
        if hasattr(persistent, "_mas_history_mhs_data"):
            mas_bridge_log("SANITIZATION: Found _mas_history_mhs_data. Attempting delete...")
            try:
                del persistent._mas_history_mhs_data
                mas_bridge_log("SANITIZATION: Delete successful.")
            except Exception as e:
                mas_bridge_log("SANITIZATION: Delete failed (" + str(e) + "). Forcing to empty dict.")
                persistent._mas_history_mhs_data = {}
        else:
            mas_bridge_log("SANITIZATION: _mas_history_mhs_data not found (Clean).")

        # SANITIZATION PHASE 2: Deep Clean of Corrupt Datetimes
        # Scans for lingering corrupt data from previous failed imports (ghosts)
        # Specifically targets variables ending in _dt that are dicts (should be datetime)
        mas_bridge_log("SANITIZATION PHASE 2: Scanning for corrupt time variables...")
        keys_to_purge = []
        if persistent.__dict__:
            mas_bridge_log("Scanning " + str(len(persistent.__dict__)) + " persistent variables...")
            for k, v in persistent.__dict__.items():
                if isinstance(v, dict):
                    # CHECK 1: Naming Convention (Legacy corruptions)
                    if k.endswith("_dt") or k.endswith("_date") or k == "_mas_last_hold_dt" or k == "_mas_first_kiss":
                        mas_bridge_log("Found suspicious variable name: " + k + ". Marking for purge.")
                        keys_to_purge.append(k)
                    
                    # CHECK 2: Content Inspection (Universal Bridge Cleaner)
                    # If it has __bridge_type__, it's a raw bridge object that wasn't reconstructed.
                    elif "__bridge_type__" in v:
                        mas_bridge_log("Found unconstructed bridge object: " + k + ". Marking for purge.")
                        keys_to_purge.append(k)
        
        # TARGETED CHECKS for known crashers
        # These variable are prone to "ghost" corruption (appearing as dicts instead of dates)
        # We explicitly purge them if found as dicts.
        known_crashers = [
            "_mas_last_hold_dt", 
            "_mas_first_kiss", 
            "_mas_last_monika_ily", 
            "_mas_last_kiss",
            "_mas_monika_lovecountertime"
        ]
        
        for target in known_crashers:
            if hasattr(persistent, target):
                v = getattr(persistent, target)
                # STRICTER CHECK: If it's NOT a datetime (and not None), kill it.
                # This catches dicts, strings, lists, or even wrong object types.
                # We specifically want these to be dates/datetimes.
                if v is not None and not isinstance(v, datetime.datetime) and not isinstance(v, datetime.date):
                    mas_bridge_log("TARGET CHECK: " + target + " is corrupted (Type: " + str(type(v)) + "). Force purging.")
                    keys_to_purge.append(target)

        # Deduplicate keys
        keys_to_purge = list(set(keys_to_purge))

        for k in keys_to_purge:
            try:
                delattr(persistent, k)
                mas_bridge_log("Purged corrupt variable: " + k)
            except Exception as e:
                mas_bridge_log("Failed to purge " + k + ": " + str(e))

        if not os.path.exists(MAS_BRIDGE_FILE):
            mas_bridge_log("Bridge file not found at: " + MAS_BRIDGE_FILE)
            return

        try:
            with open(MAS_BRIDGE_FILE, "r") as f:
                import_data = json.load(f)
            
            mas_bridge_log("JSON loaded successfully.")

            count = 0
            
            # 1. Restore Persistent Data
            if "persistent" in import_data:
                
                p_data = mas_bridge_reconstruct(import_data["persistent"])
                
                # CRITICAL SAFETY: Validate 'sessions' before applying
                if "sessions" in p_data:
                    new_sessions = p_data["sessions"]
                    is_safe = True
                    
                    if not isinstance(new_sessions, dict):
                        mas_bridge_log("WARNING: Imported sessions is NOT a dict. Ignoring.")
                        is_safe = False
                    else:
                        fs = new_sessions.get("first_session")
                        if fs and isinstance(fs, dict) and not isinstance(fs, datetime.datetime):
                            # Double check it's not a datetime subclass (unlikely but possible)
                            mas_bridge_log("WARNING: Imported first_session is a raw DICT (Bridge Fail). Ignoring sessions update.")
                            mas_bridge_log("Bad first_session val: " + str(fs))
                            is_safe = False
                    
                    if not is_safe:
                        # Remove bad sessions from data so it doesn't get set
                        del p_data["sessions"]
                        mas_bridge_log("Skipped updating persistent.sessions to prevent crash.")
                    else:
                        mas_bridge_log("Imported sessions valid. Allowing update.")

                # Filter out variables that are known to cause crashes or are problematic
                # These are either corrupt, or Ren'Py internal variables that shouldn't be overwritten
                skip_keys = [
                    "_mas_history_saved_data", # Corrupt history data
                    "_mas_history_mhs_data",   # Corrupt history data
                    "_seen_ever",              # RESTORED via custom logic below
                    "_mas_player_bday",        # Handled by specific logic, avoid direct overwrite
                    "_seen_translates",        # Internal Ren'Py variable
                    "_seen_images",            # Internal Ren'Py variable
                    "_seen_audio",             # Internal Ren'Py variable
                    "sessions",                # Corrupt sessions data
                    "_mas_affection_backups",  # Corrupt date data
                    "_mas_absence_time",       # Corrupt timedelta data
                    "_mas_last_hold_dt",       # Corrupt datetime data
                    "_mas_first_kiss",         # Corrupt datetime data
                    "_mas_last_monika_ily",    # Corrupt datetime data
                    "_mas_last_kiss",          # Corrupt datetime data
                    "_mas_monika_lovecountertime", # Corrupt datetime data
                    "event_database"           # PROTECT: Don't overwrite local DB with potentially empty/bad export
                ]

                for k, v in p_data.items():
                    # RESTORE: _seen_ever (Seen Events)
                    # Critical for preventing repeated topics.
                    # Needs specific handling to merge safely as a set.
                    if k == "_seen_ever":
                        if v is not None:
                            try:
                                if not hasattr(persistent, "_seen_ever") or persistent._seen_ever is None:
                                    persistent._seen_ever = set()
                                
                                # Case 1: List (JSON default for set)
                                if isinstance(v, list):
                                    persistent._seen_ever.update(v)
                                    mas_bridge_log("Restored _seen_ever from LIST (Merged " + str(len(v)) + " items).")
                                
                                # Case 2: Dict (Possible corruption or set->dict JSONify)
                                elif isinstance(v, dict):
                                    persistent._seen_ever.update(v.keys())
                                    mas_bridge_log("Restored _seen_ever from DICT keys (Merged " + str(len(v)) + " items).")
                                
                                else:
                                    mas_bridge_log("Skipping _seen_ever: Unknown type " + str(type(v)))
                            except Exception as e:
                                mas_bridge_log("Error restoring _seen_ever: " + str(e))
                        continue

                    # FILTER: Skip problematic keys
                    if k in skip_keys:
                        mas_bridge_log("Skipping " + k + " due to skip list.")
                        continue
                
                    # --- POST-UPDATE SYNCHRONIZATION ---
                    # Now that valid variables are restored and garbage is skipped,
                    # we must sync _seen_ever with event_database.
                    # Since we skipped importing event_database (to avoid corruption),
                    # we use _seen_ever to tell the local event_database what we've already seen.
                    if hasattr(persistent, "event_database") and hasattr(persistent, "_seen_ever"):
                        mas_bridge_log("SYNC: Synchronizing 'Seen' status from _seen_ever to event_database...")
                        sync_count = 0
                        if persistent.event_database:
                            for ev_label, ev_obj in persistent.event_database.items():
                                if ev_label in persistent._seen_ever:
                                    # It's seen, so make sure shown_count reflects that
                                    if hasattr(ev_obj, "shown_count") and ev_obj.shown_count == 0:
                                        ev_obj.shown_count = 1
                                        sync_count += 1
                        mas_bridge_log("SYNC: Updated " + str(sync_count) + " events to 'seen' status.")

                    # FILTER: Player birthday. If this is a dict, it breaks poem unlocking logic.
                    if k == "_mas_player_bday":
                        mas_bridge_log("Skipping _mas_player_bday to prevent crash. (Will use existing or prompt).")
                        continue

                    # FILTER: RenPy internal sets.
                    if k in ["_seen_translates", "_seen_images", "_seen_audio"]:
                        mas_bridge_log("Skipping " + k + " to prevent crash.")
                        continue

                    # FILTER: Affection Backups and Absence Time. corrupted dates here crash the Affection Log.
                    if k in ["_mas_affection_backups", "_mas_absence_time"]:
                        mas_bridge_log("Skipping " + k + " to prevent crash.")
                        continue

                    # FILTER: Explicit check for known crashers to prevent re-infection
                    if k in ["_mas_last_hold_dt", "_mas_first_kiss", "_mas_last_monika_ily", "_mas_last_kiss"]:
                        mas_bridge_log("Skipping " + k + " to prevent crash.")
                        continue

                    # FILTER: Generic Corrupt Datetime Protector
                    # If key suggests it's a date/time, but value is a raw dict, SKIP IT.
                    # This handles any other variable we might have missed.
                    if isinstance(v, dict) and (k.endswith("_dt") or k.endswith("_date")):
                        mas_bridge_log("Skipping corrupt time variable " + k + " (value is dict).")
                        continue

                    setattr(persistent, k, v)
                    count += 1
                
                # Post-Import Check for sessions
                if hasattr(persistent, "sessions") and persistent.sessions:
                    fs = persistent.sessions.get("first_session")
                    mas_bridge_log("POST-IMPORT fs type: " + str(type(fs)))
                
                # SAFETY: Ensure _seen_ever is not None
                if not hasattr(persistent, "_seen_ever") or persistent._seen_ever is None:
                    mas_bridge_log("WARNING: persistent._seen_ever is missing or None. Initializing to empty dict.")
                    persistent._seen_ever = {}

                # SAFETY: Ensure _seen_translates is not None (Fixes 'NoneType not iterable' crash)
                if not hasattr(persistent, "_seen_translates") or persistent._seen_translates is None:
                    mas_bridge_log("WARNING: persistent._seen_translates is missing. Initializing to empty set.")
                    persistent._seen_translates = set()
                
                # SAFETY: Proactive checks for other sets
                if not hasattr(persistent, "_seen_images") or persistent._seen_images is None:
                    persistent._seen_images = dict()
                if not hasattr(persistent, "_seen_audio") or persistent._seen_audio is None:
                    persistent._seen_audio = dict()

                # REPAIR: Fix integer keys for _mas_current_consumable
                # JSON converts dict keys to strings ("0", "1"), but MAS expects integers (0, 1).
                if hasattr(persistent, "_mas_current_consumable"):
                    pc = persistent._mas_current_consumable
                    mas_bridge_log("DEBUG: _mas_current_consumable type: " + str(type(pc)))
                     
                    if isinstance(pc, dict):
                        mas_bridge_log("DEBUG: Keys found: " + str(pc.keys()))
                         
                        fixed_consumables = {}
                        was_fixed = False
                         
                        for k, v in pc.items():
                            # Log key type
                            mas_bridge_log("DEBUG: Key " + str(k) + " type: " + str(type(k)))
                             
                            if isinstance(k, basestring) and k.isdigit():
                                try:
                                    new_k = int(k)
                                    fixed_consumables[new_k] = v
                                    was_fixed = True
                                    mas_bridge_log("DEBUG: Converted " + str(k) + " -> " + str(new_k))
                                except:
                                    fixed_consumables[k] = v
                            else:
                                fixed_consumables[k] = v
                         
                        # Force Ensure existence of 0 and 1 (Drink/Food)
                        if 0 not in fixed_consumables:
                            mas_bridge_log("DEBUG: Key 0 missing. Initializing default.")
                            fixed_consumables[0] = {"prep_time": None, "consume_time": None, "id": None}
                            was_fixed = True
                             
                        if 1 not in fixed_consumables:
                            mas_bridge_log("DEBUG: Key 1 missing. Initializing default.")
                            fixed_consumables[1] = {"prep_time": None, "consume_time": None, "id": None}
                            was_fixed = True

                        if was_fixed:
                            persistent._mas_current_consumable = fixed_consumables
                            mas_bridge_log("REPAIR: Fixed _mas_current_consumable keys/structure.")
                     
                    else:
                        # It's not a dict? Re-init
                        mas_bridge_log("ERROR: _mas_current_consumable is NOT a dict. Resetting.")
                        persistent._mas_current_consumable = {
                            0: {"prep_time": None, "consume_time": None, "id": None},
                            1: {"prep_time": None, "consume_time": None, "id": None}
                        }

            # 2. Restore Calendar Data
            if "calendar" in import_data:
                mas_bridge_log("Restoring calendar data...")
                cal_data = mas_bridge_reconstruct(import_data["calendar"])
                store.mas_bridge_calendar_backup = cal_data

            mas_bridge_log("Bridge Data Loaded: {} persistent variables updated.".format(count))
            
            # Delete file to prevent re-import and keep directory clean
            try:
                os.remove(MAS_BRIDGE_FILE)
                mas_bridge_log("Bridge file deleted successfully.")
            except Exception as e:
                mas_bridge_log("Error deleting bridge file: " + str(e))

        except Exception as e:
            mas_bridge_log("Bridge Import CRITICAL ERROR: " + str(e))

    # Run the restore
    mas_bridge_restore()

init 10 python:
    try:
        if hasattr(store, "mas_bridge_calendar_backup"):
            if hasattr(store, "mas_calendar"):
                # We overwrite the database
                db = store.mas_bridge_calendar_backup
                
                new_db = {}
                for month, days in db.items():
                    try:
                        m_int = int(month)
                        new_days = {}
                        for day, events in days.items():
                            try:
                                d_int = int(day)
                                new_days[d_int] = events
                            except:
                                new_days[day] = events
                        new_db[m_int] = new_days
                    except:
                        new_db[month] = days
                 
                store.mas_calendar.calendar_database = new_db
                del store.mas_bridge_calendar_backup
                print("Bridge Calendar Data Injected.")
    except Exception as e:
        print("Bridge Calendar Injection Error: " + str(e))
