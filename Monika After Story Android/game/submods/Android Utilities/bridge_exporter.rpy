init 5 python:
    import json
    import os
    import datetime
    import shutil

    # CRITICAL: Prevent execution on PC to avoid crashes
    # if not renpy.android: return <- This causes SyntaxError in init blocks
    # Instead, we rely on checking renpy.android before executing hooks below.

    # Define the bridge file path
    MAS_BRIDGE_FILE = os.path.join(config.savedir, "monika_bridge.json").replace("\\", "/")

    def mas_bridge_sanitize_key(k):
        """
        Sanitizes dictionary keys to strings, adding prefixes for reconstruction if needed.
        """
        if isinstance(k, datetime.datetime):
            return "__bridge_k_T__" + k.isoformat()
        elif isinstance(k, datetime.date):
            return "__bridge_k_D__" + k.isoformat()
        else:
            return str(k)

    def mas_bridge_sanitize(data):
        """
        Recursively sanitizes data to be JSON-safe.
        Handles datetime, date, sets, and ignores unknown objects.
        Now supports RenPy's Revertable types via duck typing.
        """
        # 1. Dictionaries (and RevertableDict)
        if isinstance(data, dict) or (hasattr(data, "items") and hasattr(data, "get")):
            # Sanitize both keys and values
            new_dict = {}
            for k, v in data.items():
                # FILTER: Skip specific internal keys that cause crashes on PC import
                if k in ["_mas_history_mhs_data", "_mas_history_saved_data", "_seen_translates", "_seen_images", "_seen_audio", "_mas_player_bday"]:
                    continue

                new_key = mas_bridge_sanitize_key(k)
                new_dict[new_key] = mas_bridge_sanitize(v)
            return new_dict
        
        # 2. Lists/Tuples (and RevertableList)
        elif isinstance(data, (list, tuple)) or hasattr(data, "__iter__") and not isinstance(data, basestring):
            # Special check for Set behavior (duck typing)
            if hasattr(data, "add") and not hasattr(data, "append"): # Likely a Set
                return [mas_bridge_sanitize(v) for v in data]
            
            return [mas_bridge_sanitize(v) for v in data]

        # 3. Explicit Sets (and RevertableSet)
        elif isinstance(data, set):
            return [mas_bridge_sanitize(v) for v in data]

        # 4. Datetime Objects (The heavy hitters)
        elif isinstance(data, (datetime.datetime, datetime.date)):
            return {
                "__bridge_type__": "datetime" if isinstance(data, datetime.datetime) else "date",
                "value": data.isoformat()
            }
        
        # 5. Primitives
        elif isinstance(data, (int, float, bool, basestring, type(None))):
            return data
            
        else:
            # Unknown object? Try string representation as fallback, or None.
            # Returning None is safer than crashing logic.
            return None

    def mas_bridge_export():
        """
        Exports persistent and specific store data to a JSON file.
        """
        try:
            export_data = {}

            # 1. Export Persistent Data
            # key-value pairs from persistent
            # We filter out internal renpy stuff starting with _ (except _mas variables which might be internal but useful)
            # Actually, let's grab everything that looks relevant.
            
            p_dict = {}
            if persistent.__dict__:
                for k, v in persistent.__dict__.items():
                    # Filter out heavy RenPy internals if needed, but MAS uses a lot of custom persistent vars
                    if k.startswith("_renpy") or k.startswith("_preference"):
                        continue
                    p_dict[k] = v
            
            export_data["persistent"] = mas_bridge_sanitize(p_dict)

            # 2. Export Calendar Data
            # Based on checking zz_calendar.rpy, the database is in store.mas_calendar.calendar_database
            if hasattr(store, "mas_calendar") and hasattr(store.mas_calendar, "calendar_database"):
                export_data["calendar"] = mas_bridge_sanitize(store.mas_calendar.calendar_database)
            
            # Write to file
            with open(MAS_BRIDGE_FILE, "w") as f:
                json.dump(export_data, f, indent=4)
            
            # renpy.notify("Bridge Data Exported!") # Optional notification
            
        except Exception as e:
            try:
                with open(os.path.join(config.basedir, "bridge_error.txt"), "w") as f:
                    f.write(str(e))
            except:
                pass

    # Hook into quit action to ensure it runs on exit
    if renpy.android:
        if "python_exit_callbacks" in config.__dict__:
            config.python_exit_callbacks.append(mas_bridge_export)
        
        # Hook into save action (after save)
        # Checks if the list exists (RenPy 7.X standard)
        if not hasattr(config, "after_save_callbacks"):
            config.after_save_callbacks = []
        config.after_save_callbacks.append(mas_bridge_export)

        # Run ONCE at startup to ensure the file exists immediately (for user peace of mind)
        mas_bridge_export()

# Also adding a manual call option for testing or if callbacks fail
label mas_force_bridge_export:
    python:
        if renpy.android:
            mas_bridge_export()
    return
