
init -10 python:
    if persistent._mas_dtm_overrides is None:
        persistent._mas_dtm_overrides = {
            "eye_map": {},         # Maps original eye ID to replacement (e.g. "e": "my_eyes")
            "table": "def",        # Table ID, default relies on MAS's default table "def"
            "chess_pieces": {},    # Maps piece ID to image path
            "pong_field": None     # Path for pong field
        }

init 999 python in dtm_core:
    import store

    # Store original configuration to allow resetting
    if not hasattr(store, "_mas_dtm_originals"):
        store._mas_dtm_originals = {
            "eye_map": store.mas_sprite_decoder.EYE_MAP.copy(),
            "tablechair": "def"
        }

    def force_update_mas_visuals():
        """
        Forces Ren'Py to redraw all screens and dynamic displayables immediately.
        This is the core of the 'hot-swap' feature.
        """
        renpy.restart_interaction()

    def set_eye_texture(eye_id, new_texture_value):
        """
        Overrides an eye texture mapping.
        """
        store.persistent._mas_dtm_overrides["eye_map"][eye_id] = new_texture_value
        apply_sprite_overrides()
        force_update_mas_visuals()

    def reset_eye_textures():
        """
        Resets eye textures to MAS defaults.
        """
        store.persistent._mas_dtm_overrides["eye_map"].clear()
        apply_sprite_overrides()
        force_update_mas_visuals()

    def apply_sprite_overrides():
        """
        Applies overrides by hooking into mas_sprites._rk_face to inject absolute paths for custom eyes.
        We avoid modifying EYE_MAP directly for custom paths to prevent MAS from attaching 'mod_assets/monika/f/' and '.png' to them.
        """
        if not hasattr(store, "_mas_dtm_original_rk_face"):
            store._mas_dtm_original_rk_face = store.mas_sprites._rk_face

        def custom_rk_face(rk_list, eyes, eyebrows, nose, mouth, flt, fpfx, lean, sweat, tears, emote):
            # Let the original function run first
            original_len = len(rk_list)
            store._mas_dtm_original_rk_face(rk_list, eyes, eyebrows, nose, mouth, flt, fpfx, lean, sweat, tears, emote)
            
            # If nothing was added or we don't have this override, do nothing
            if len(rk_list) == original_len or eyes not in store.persistent._mas_dtm_overrides["eye_map"]:
                return
            
            # Re-construct the specific face composite with our absolute path for eyes
            custom_eye_path = store.persistent._mas_dtm_overrides["eye_map"][eyes]
            
            # We must recreate the img_str_list used in building the face Composite
            img_str_list = [
                (0, 0), custom_eye_path,
                (0, 0), "".join((store.mas_sprites.F_T_MAIN, fpfx, store.mas_sprites.PREFIX_EYEB, eyebrows, store.mas_sprites.FILE_EXT)),
                (0, 0), "".join((store.mas_sprites.F_T_MAIN, fpfx, store.mas_sprites.PREFIX_NOSE, nose, store.mas_sprites.FILE_EXT)),
                (0, 0), "".join((store.mas_sprites.F_T_MAIN, fpfx, store.mas_sprites.PREFIX_MOUTH, mouth, store.mas_sprites.FILE_EXT))
            ]

            if sweat:
                img_str_list.extend(((0,0), "".join((store.mas_sprites.F_T_MAIN, fpfx, store.mas_sprites.PREFIX_SWEAT, sweat, store.mas_sprites.FILE_EXT))))
            if tears:
                img_str_list.extend(((0,0), "".join((store.mas_sprites.F_T_MAIN, fpfx, store.mas_sprites.PREFIX_TEARS, tears, store.mas_sprites.FILE_EXT))))
            if emote:
                img_str_list.extend(((0,0), "".join((store.mas_sprites.F_T_MAIN, fpfx, store.mas_sprites.PREFIX_EMOTE, emote, store.mas_sprites.FILE_EXT))))
            
            # Replace the last added render key (which is the face composite) with our patched one
            last_rk = list(rk_list[-1])
            last_rk[2] = renpy.display.im.Composite((1280, 850), *img_str_list)
            rk_list[-1] = tuple(last_rk)

        # Apply the hook
        store.mas_sprites._rk_face = custom_rk_face

    def set_table_texture(new_table_id):
        """
        Overrides the table texture. 
        Note: The user should ensure 'mod_assets/table/table-[new_table_id].png' exists or similar MAS table asset format.
        """
        store.persistent._mas_dtm_overrides["table"] = new_table_id
        apply_table_overrides()
        force_update_mas_visuals()

    def reset_table_texture():
        store.persistent._mas_dtm_overrides["table"] = "def"
        apply_table_overrides()
        force_update_mas_visuals()

    def apply_table_overrides():
        """
        Overrides the actual table property in the sitting Monika instance.
        """
        if hasattr(store, "monika_chr") and hasattr(store.monika_chr, "tablechair"):
            # Update the table property 
            store.monika_chr.tablechair.table = store.persistent._mas_dtm_overrides["table"]

    def set_pong_textures(new_pong_folder_path):
        """
        Sets the pong mod folder path. This folder should contain:
        - pong.png
        - pong_ball.png
        - pong_field.png
        """
        store.persistent._mas_dtm_overrides["pong_field"] = new_pong_folder_path
        apply_pong_overrides()

    def reset_pong_textures():
        store.persistent._mas_dtm_overrides["pong_field"] = None
        renpy.display.image.images[("bg", "pong", "field")] = store.Image("mod_assets/games/pong/pong_field.png")
        if hasattr(store, "_mas_dtm_original_pong_init") and hasattr(store, "PongDisplayable"):
            store.PongDisplayable.__init__ = store._mas_dtm_original_pong_init
        if hasattr(store, "_mas_dtm_pong_surfaces"):
            del store._mas_dtm_pong_surfaces

    def apply_pong_overrides():
        """
        Applies pong texture overrides.
        - Copies the 3 pong images from external storage to an internal game cache folder.
        - Loads them via standard store.Image() with relative paths (fast, cached by IM).
        """
        pong_folder = store.persistent._mas_dtm_overrides.get("pong_field", None)
        
        if not pong_folder:
            return
            
        import os
        import shutil
        
        # Internal cache dir (writable, fast Android internal storage)
        cache_dir = os.path.join(renpy.config.gamedir, "_dtm_cache", "pong")
        try:
            if not os.path.exists(cache_dir):
                os.makedirs(cache_dir)
        except Exception:
            return
        
        # Copy the 3 pong images from external storage to internal cache
        copied = {}
        for fname in ("pong_field.png", "pong.png", "pong_ball.png"):
            src = os.path.join(pong_folder, fname)
            dst = os.path.join(cache_dir, fname)
            if os.path.isfile(src):
                try:
                    shutil.copy2(src, dst)
                    # Relative path from gamedir (how store.Image resolves it)
                    copied[fname] = "_dtm_cache/pong/" + fname
                except Exception:
                    pass
        
        store._mas_dtm_pong_surfaces = copied
        
        # 1. Background image override with internal-path Image
        if "pong_field.png" in copied:
            renpy.display.image.images[("bg", "pong", "field")] = store.Image(copied["pong_field.png"])
            
        # 2. Hook into PongDisplayable to override paddle and ball
        if hasattr(store, "PongDisplayable"):
            if not hasattr(store, "_mas_dtm_original_pong_init"):
                store._mas_dtm_original_pong_init = store.PongDisplayable.__init__
                
            def custom_pong_init(self, *args, **kwargs):
                store._mas_dtm_original_pong_init(self, *args, **kwargs)
                cached = getattr(store, "_mas_dtm_pong_surfaces", {})
                if "pong.png" in cached:
                    self.paddle = store.Image(cached["pong.png"])
                if "pong_ball.png" in cached:
                    self.ball = store.Image(cached["pong_ball.png"])

            store.PongDisplayable.__init__ = custom_pong_init

    def set_chess_piece(piece_symbol, new_image_path):
        """
        Piece symbols generally: wP, wN, wB, wR, wQ, wK, bP, bN, bB, bR, bQ, bK
        """
        store.persistent._mas_dtm_overrides["chess_pieces"][piece_symbol] = new_image_path
        apply_chess_overrides()
        force_update_mas_visuals()

    def reset_chess_pieces():
        store.persistent._mas_dtm_overrides["chess_pieces"].clear()
        # Restore chess piece dict (assumes original MASPiece.IMG_MAP defaults or re-importing)
        # We need to rebuild or trigger MAS's native setup if needed, but for now we'll do simple restore.
        # Actually chess IMG_MAP is built on import. We'll store a copy on init if possible.
        if hasattr(store, "mas_chess") and hasattr(store.mas_chess, "MASPiece"):
            if not hasattr(store, "_mas_dtm_original_chess_map"):
                pass # Can't restore properly if we didn't save it. So we'll save it at initial hook.
            else:
                for k, v in store._mas_dtm_original_chess_map.items():
                    store.mas_chess.MASPiece.IMG_MAP[k] = v
        force_update_mas_visuals()

    def apply_chess_overrides():
        if hasattr(store, "mas_chess") and hasattr(store.mas_chess, "MASPiece"):
            # Prepare backup map first time
            if not hasattr(store, "_mas_dtm_original_chess_map"):
                store._mas_dtm_original_chess_map = store.mas_chess.MASPiece.IMG_MAP.copy()
            
            # Apply 
            for p_sym, img_path in store.persistent._mas_dtm_overrides["chess_pieces"].items():
                store.mas_chess.MASPiece.IMG_MAP[p_sym] = img_path

    # ==========================================
    # NOU (UNO) TEXTURE LOGIC
    # ==========================================
    def set_nou_textures(new_nou_folder_path):
        """
        Sets the NOU mod folder path. This folder should contain cards/, desks/, sfx/, note.png, and pen.png
        """
        if "nou_theme" not in store.persistent._mas_dtm_overrides:
            store.persistent._mas_dtm_overrides["nou_theme"] = None
        store.persistent._mas_dtm_overrides["nou_theme"] = new_nou_folder_path
        apply_nou_overrides()

    def reset_nou_textures():
        store.persistent._mas_dtm_overrides["nou_theme"] = None
        # Restore constants
        if hasattr(store, "_mas_dtm_original_nou_assets"):
            if hasattr(store, "mas_nou"):
                store.mas_nou.ASSETS = store._mas_dtm_original_nou_assets
            if hasattr(store, "mas_cardgames"):
                store.mas_cardgames.DESK_SPRITES_PATH = store._mas_dtm_original_nou_desks
        # Restore filter switch
        if hasattr(store, "_mas_dtm_original_filter_switch"):
            store.MASFilterSwitch = store._mas_dtm_original_filter_switch
        # Reload native SFX and desks
        if hasattr(store, "mas_nou") and hasattr(store.mas_nou.NOU, "_load_sfx"):
            store.mas_nou.NOU._load_sfx()
        if hasattr(store, "mas_cardgames") and hasattr(store.mas_cardgames, "_m1_zz_cardgames__scanDeskSprites"):
            store.mas_cardgames.DESK_SPRITES_MAP.clear()
            store.mas_cardgames._m1_zz_cardgames__scanDeskSprites()

    def apply_nou_overrides():
        """
        Copies NOU textures to internal cache, overrides MAS_NOU assets constants, and reloads sfx/desks.
        """
        if "nou_theme" not in store.persistent._mas_dtm_overrides:
            store.persistent._mas_dtm_overrides["nou_theme"] = None
            
        nou_folder = store.persistent._mas_dtm_overrides.get("nou_theme", None)
        
        if not nou_folder:
            return
            
        import os
        import shutil
        
        # Save originals first
        if not hasattr(store, "_mas_dtm_original_nou_assets") and hasattr(store, "mas_nou"):
            store._mas_dtm_original_nou_assets = store.mas_nou.ASSETS
            if hasattr(store, "mas_cardgames"):
                store._mas_dtm_original_nou_desks = store.mas_cardgames.DESK_SPRITES_PATH
            else:
                store._mas_dtm_original_nou_desks = "mod_assets/games/nou/desks/"
        
        # 1. Copy the entire custom NOU folder to internal cache
        cache_dir = os.path.join(renpy.config.gamedir, "_dtm_cache", "nou")
        try:
            if os.path.exists(cache_dir):
                shutil.rmtree(cache_dir)
            shutil.copytree(nou_folder, cache_dir)
        except Exception:
            return
            
        # The internal path representation needed by Ren'Py config/searchpaths
        internal_nou_path = "_dtm_cache/nou/"
        
        # 2. Override dynamic map variables
        if hasattr(store, "mas_nou"):
            store.mas_nou.ASSETS = internal_nou_path
        if hasattr(store, "mas_cardgames"):
            store.mas_cardgames.DESK_SPRITES_PATH = internal_nou_path + "desks/"
            
        # 3. Handle static UI overrides (note.png, pen.png) via MASFilterSwitch hook
        if not hasattr(store, "_mas_dtm_original_filter_switch"):
            store._mas_dtm_original_filter_switch = store.MASFilterSwitch

        def custom_filter_switch(img):
            if isinstance(img, basestring):
                if img == "mod_assets/games/nou/note.png" and os.path.isfile(os.path.join(cache_dir, "note.png")):
                    img = internal_nou_path + "note.png"
                elif img == "mod_assets/games/nou/pen.png" and os.path.isfile(os.path.join(cache_dir, "pen.png")):
                    img = internal_nou_path + "pen.png"
            return store._mas_dtm_original_filter_switch(img)
            
        store.MASFilterSwitch = custom_filter_switch
            
        # 4. Reload Desks by manually scanning os.listdir (since renpy.list_files ignores our cache)
        if hasattr(store, "mas_cardgames") and hasattr(store, "mas_background"):
            store.mas_cardgames.DESK_SPRITES_MAP.clear()
            desk_dir = os.path.join(cache_dir, "desks")
            if os.path.exists(desk_dir):
                sprites_map = {}
                for f in os.listdir(desk_dir):
                    if os.path.isfile(os.path.join(desk_dir, f)):
                        key = f.rpartition(".")[0]
                        if key:
                            sprites_map[key] = f
                
                fb = sprites_map.get(store.mas_background.MBG_DEF)
                for bg_id in store.mas_background.BACKGROUND_MAP.iterkeys():
                    if bg_id not in store.mas_cardgames.DESK_SPRITES_MAP:
                        filename = sprites_map.get(bg_id, fb)
                        if filename:
                            store.mas_cardgames.DESK_SPRITES_MAP[bg_id] = store.MASFilterSwitch(internal_nou_path + "desks/" + filename)

        # 5. Reload SFX by manually scanning os.listdir
        if hasattr(store, "mas_nou"):
            store.mas_nou.NOU._reset_sfx()
            sfx_dir = os.path.join(cache_dir, "sfx")
            if os.path.exists(sfx_dir):
                name_to_sfx_list_map = {
                    "shuffle": store.mas_nou.NOU.SFX_SHUFFLE,
                    "move": store.mas_nou.NOU.SFX_MOVE,
                    "slide": store.mas_nou.NOU.SFX_DRAW,
                    "place": store.mas_nou.NOU.SFX_PLAY,
                    "shove": store.mas_nou.NOU.SFX_PLAY
                }
                for f in os.listdir(sfx_dir):
                    if not f.endswith(store.mas_nou.NOU.SFX_EXT):
                        continue
                    name, undscr, rest = f.partition("_")
                    sfx_list = name_to_sfx_list_map.get(name, None)
                    if sfx_list is not None:
                        sfx_list.append(internal_nou_path + "sfx/" + f)

# Auto-apply on game start
init 1000 python:
    store.dtm_core.apply_sprite_overrides()
    store.dtm_core.apply_table_overrides()
    if hasattr(store, "mas_chess"):
        store.dtm_core.apply_chess_overrides()
    store.dtm_core.apply_pong_overrides()
    store.dtm_core.apply_nou_overrides()
