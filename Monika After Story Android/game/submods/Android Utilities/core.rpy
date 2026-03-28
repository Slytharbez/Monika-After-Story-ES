init -10 python:
    if persistent._mas_dtm_overrides is None:
        persistent._mas_dtm_overrides = {
            "eye_map": {},         
            "table": "def",        
            "chess_pieces": {},    
            "pong_field": None     
        }

init 999 python in dtm_core:
    import store

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

    # ==========================================
    # PONG TEXTURE LOGIC
    # ==========================================
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
        renpy.display.im.cache.clear()

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
        
        cache_dir = os.path.join(renpy.config.gamedir, "_dtm_cache", "pong")
        try:
            if not os.path.exists(cache_dir):
                os.makedirs(cache_dir)
        except Exception:
            return
        
        copied = {}
        for fname in ("pong_field.png", "pong.png", "pong_ball.png"):
            src = os.path.join(pong_folder, fname)
            dst = os.path.join(cache_dir, fname)
            if os.path.isfile(src):
                try:
                    shutil.copy2(src, dst)
                    copied[fname] = "_dtm_cache/pong/" + fname
                except Exception:
                    pass
        
        store._mas_dtm_pong_surfaces = copied
        
        renpy.display.im.cache.clear()
        
        if "pong_field.png" in copied:
            renpy.display.image.images[("bg", "pong", "field")] = store.Image(copied["pong_field.png"])
            
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

    # ==========================================
    # CHESS TEXTURE LOGIC
    # ==========================================
    def set_chess_textures(chess_folder_path):
        """
        Sets the chess texture folder. This folder should contain:
        - chess_board.png (background board)
        - pieces/ folder with wP, wN, wB, wR, wQ, wK, bP, bN, bB, bR, bQ, bK (or lower-case b*)
        """
        if "chess_theme" not in store.persistent._mas_dtm_overrides:
            store.persistent._mas_dtm_overrides["chess_theme"] = None
        store.persistent._mas_dtm_overrides["chess_theme"] = chess_folder_path
        apply_chess_overrides()

    def reset_chess_textures():
        store.persistent._mas_dtm_overrides["chess_theme"] = None
        if hasattr(store, "MASPiece"):
            if hasattr(store, "_mas_dtm_original_chess_map"):
                store.MASPiece.IMG_MAP.clear()
                store.MASPiece.IMG_MAP.update(store._mas_dtm_original_chess_map)
        if hasattr(store, "_mas_dtm_original_chess_board"):
            store.MASChessDisplayableBase.BOARD_IMAGE = store._mas_dtm_original_chess_board
        if hasattr(store, "_mas_dtm_original_chess_indicator_player"):
            store.MASChessDisplayableBase.MOVE_INDICATOR_PLAYER = store._mas_dtm_original_chess_indicator_player
        if hasattr(store, "_mas_dtm_original_chess_indicator_monika"):
            store.MASChessDisplayableBase.MOVE_INDICATOR_MONIKA = store._mas_dtm_original_chess_indicator_monika
        if hasattr(store, "_mas_dtm_original_chess_hl_green"):
            store.MASChessDisplayableBase.PIECE_HIGHLIGHT_GREEN_IMAGE = store._mas_dtm_original_chess_hl_green
        if hasattr(store, "_mas_dtm_original_chess_hl_red"):
            store.MASChessDisplayableBase.PIECE_HIGHLIGHT_RED_IMAGE = store._mas_dtm_original_chess_hl_red
        if hasattr(store, "_mas_dtm_original_chess_hl_yellow"):
            store.MASChessDisplayableBase.PIECE_HIGHLIGHT_YELLOW_IMAGE = store._mas_dtm_original_chess_hl_yellow
        if hasattr(store, "_mas_dtm_original_chess_hl_magenta"):
            store.MASChessDisplayableBase.PIECE_HIGHLIGHT_MAGENTA_IMAGE = store._mas_dtm_original_chess_hl_magenta
        renpy.display.im.cache.clear()
        force_update_mas_visuals()

    reset_chess_pieces = reset_chess_textures

    def apply_chess_overrides(sync=False):
        """
        Copies chess textures to internal cache and applies them.
        Runs synchronously to avoid async timing bugs on Android UI.
        """
        if "chess_theme" not in store.persistent._mas_dtm_overrides:
            store.persistent._mas_dtm_overrides["chess_theme"] = None
            
        chess_folder = store.persistent._mas_dtm_overrides.get("chess_theme", None)
        if not chess_folder:
            return
            
        import os
        import shutil
        
        store.mas_dtm_trigger_chess_apply = False
        
        reset_chess_textures()
        store.persistent._mas_dtm_overrides["chess_theme"] = chess_folder
        
        def do_copy_chess():
            cache_dir = os.path.join(renpy.config.gamedir, "_dtm_cache", "chess")
            try:
                if os.path.exists(cache_dir):
                    shutil.rmtree(cache_dir, ignore_errors=True)
                if not os.path.exists(cache_dir):
                    os.makedirs(cache_dir)
                    
                for root, dirs, files in os.walk(chess_folder):
                    rel_path = os.path.relpath(root, chess_folder).lower()
                    if rel_path == ".":
                        rel_path = ""
                    dest_dir = os.path.join(cache_dir, rel_path)
                    if not os.path.exists(dest_dir):
                        try:
                            os.makedirs(dest_dir)
                        except Exception:
                            pass
                    
                    is_pieces = rel_path.startswith("pieces")
                    for f in files:
                        src_f = os.path.join(root, f)
                        fname = f if is_pieces else f.lower()
                        dst_f = os.path.join(dest_dir, fname)
                        try:
                            shutil.copy2(src_f, dst_f)
                        except Exception:
                            pass
            except Exception:
                pass
            finally:
                store.mas_dtm_trigger_chess_apply = True
        
        do_copy_chess()
        if sync:
            _finish_apply_chess_overrides(startup=True)
        else:
            _finish_apply_chess_overrides(startup=False)

    def _finish_apply_chess_overrides(startup=False):
        """
        Called by the main thread after the background chess copy completes.
        Patches IMG_MAP and BOARD_IMAGE.
        """
        import os
        cache_dir = os.path.join(renpy.config.gamedir, "_dtm_cache", "chess")
        pieces_dir = os.path.join(cache_dir, "pieces")
        
        if not hasattr(store, "MASPiece"):
            return
            
        if not hasattr(store, "_mas_dtm_original_chess_map"):
            store._mas_dtm_original_chess_map = store.MASPiece.IMG_MAP.copy()
        if not hasattr(store, "_mas_dtm_original_chess_board"):
            store._mas_dtm_original_chess_board = store.MASChessDisplayableBase.BOARD_IMAGE
        if not hasattr(store, "_mas_dtm_original_chess_indicator_player"):
            store._mas_dtm_original_chess_indicator_player = store.MASChessDisplayableBase.MOVE_INDICATOR_PLAYER
        if not hasattr(store, "_mas_dtm_original_chess_indicator_monika"):
            store._mas_dtm_original_chess_indicator_monika = store.MASChessDisplayableBase.MOVE_INDICATOR_MONIKA
        if not hasattr(store, "_mas_dtm_original_chess_hl_green"):
            store._mas_dtm_original_chess_hl_green = store.MASChessDisplayableBase.PIECE_HIGHLIGHT_GREEN_IMAGE
        if not hasattr(store, "_mas_dtm_original_chess_hl_red"):
            store._mas_dtm_original_chess_hl_red = store.MASChessDisplayableBase.PIECE_HIGHLIGHT_RED_IMAGE
        if not hasattr(store, "_mas_dtm_original_chess_hl_yellow"):
            store._mas_dtm_original_chess_hl_yellow = store.MASChessDisplayableBase.PIECE_HIGHLIGHT_YELLOW_IMAGE
        if not hasattr(store, "_mas_dtm_original_chess_hl_magenta"):
            store._mas_dtm_original_chess_hl_magenta = store.MASChessDisplayableBase.PIECE_HIGHLIGHT_MAGENTA_IMAGE
            
        board_path = os.path.join(cache_dir, "chess_board.png")
        if os.path.exists(board_path):
            store.MASChessDisplayableBase.BOARD_IMAGE = store.Image("_dtm_cache/chess/chess_board.png")
            
        ind_player_path = os.path.join(cache_dir, "move_indicator_player.png")
        if os.path.exists(ind_player_path):
            store.MASChessDisplayableBase.MOVE_INDICATOR_PLAYER = store.Image("_dtm_cache/chess/move_indicator_player.png")
            
        ind_monika_path = os.path.join(cache_dir, "move_indicator_monika.png")
        if os.path.exists(ind_monika_path):
            store.MASChessDisplayableBase.MOVE_INDICATOR_MONIKA = store.Image("_dtm_cache/chess/move_indicator_monika.png")

        _chess_hl_map = {
            "piece_highlight_green.png": "PIECE_HIGHLIGHT_GREEN_IMAGE",
            "piece_highlight_red.png": "PIECE_HIGHLIGHT_RED_IMAGE",
            "piece_highlight_yellow.png": "PIECE_HIGHLIGHT_YELLOW_IMAGE",
            "piece_highlight_magenta.png": "PIECE_HIGHLIGHT_MAGENTA_IMAGE",
        }
        for fname, attr in _chess_hl_map.items():
            fpath = os.path.join(cache_dir, fname)
            if os.path.exists(fpath):
                setattr(store.MASChessDisplayableBase, attr, store.Image("_dtm_cache/chess/" + fname))
            
        if os.path.exists(pieces_dir):
            for fname in os.listdir(pieces_dir):
                if not fname.lower().endswith(".png"):
                    continue
                key = fname[:-4]  # strip .png
                cached_rel = "_dtm_cache/chess/pieces/" + fname
                if key in store.MASPiece.IMG_MAP:
                    store.MASPiece.IMG_MAP[key] = store.Image(cached_rel)
                    
        renpy.display.im.cache.clear()
        if not startup:
            force_update_mas_visuals()
            renpy.notify("Texturas de ajedrez aplicadas")

    # ==========================================
    # NOU TEXTURE LOGIC
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

        if hasattr(store, "_mas_dtm_original_filter_switch"):
            store.MASFilterSwitch = store._mas_dtm_original_filter_switch
        if hasattr(store, "mas_nou") and hasattr(store.mas_nou.NOU, "_load_sfx"):
            store.mas_nou.NOU._load_sfx()
        if hasattr(store, "mas_cardgames") and hasattr(store.mas_cardgames, "_m1_zz_cardgames__scanDeskSprites"):
            store.mas_cardgames.DESK_SPRITES_MAP.clear()
            store.mas_cardgames._m1_zz_cardgames__scanDeskSprites()
            
        if hasattr(store, "_mas_dtm_original_nou_init") and hasattr(store, "mas_nou"):
            store.mas_nou.NOU.__init__ = store._mas_dtm_original_nou_init
        if hasattr(store, "_mas_dtm_original_load_card_asset") and hasattr(store, "mas_nou"):
            store.mas_nou.NOU._m1_zz_cardgames__load_card_asset = store._mas_dtm_original_load_card_asset
            
        renpy.display.im.cache.clear()

    def apply_nou_overrides(sync=False):
        """
        Copies NOU textures to internal cache, overrides MAS_NOU assets constants, and reloads sfx/desks.
        Runs synchronously to avoid async timing bugs on Android UI.
        """
        if "nou_theme" not in store.persistent._mas_dtm_overrides:
            store.persistent._mas_dtm_overrides["nou_theme"] = None
            
        nou_folder = store.persistent._mas_dtm_overrides.get("nou_theme", None)
        
        if not nou_folder:
            return
            
        import os
        import shutil
        
        store.mas_dtm_trigger_nou_apply = False
        
        reset_nou_textures()
        store.persistent._mas_dtm_overrides["nou_theme"] = nou_folder

        def do_copy_nou():
            cache_dir = os.path.join(renpy.config.gamedir, "_dtm_cache", "nou")
            try:
                if os.path.exists(cache_dir):
                    shutil.rmtree(cache_dir, ignore_errors=True)
                    
                if not os.path.exists(cache_dir):
                    os.makedirs(cache_dir)
                    
                for root, dirs, files in os.walk(nou_folder):
                    rel_path = os.path.relpath(root, nou_folder).lower()
                    if rel_path == ".":
                        rel_path = ""
                        
                    dest_dir = os.path.join(cache_dir, rel_path)
                    if not os.path.exists(dest_dir):
                        try:
                            os.makedirs(dest_dir)
                        except Exception:
                            pass
                            
                    for f in files:
                        src_f = os.path.join(root, f)
                        dst_f = os.path.join(dest_dir, f.lower())
                        try:
                            shutil.copy2(src_f, dst_f)
                        except Exception:
                            pass
            except Exception:
                pass
            finally:
                store.mas_dtm_trigger_nou_apply = True
                
        do_copy_nou()
        if sync:
            _finish_apply_nou_overrides(startup=True)
        else:
            _finish_apply_nou_overrides(startup=False)
        
    def _finish_apply_nou_overrides(startup=False):
        """
        Called by the main thread after the background copy completes.
        Applies variables and reloads assets.
        """
        import os
        cache_dir = os.path.join(renpy.config.gamedir, "_dtm_cache", "nou")
            
        internal_nou_path = "_dtm_cache/nou/"
        
        if not hasattr(store, "_mas_dtm_original_nou_init") and hasattr(store, "mas_nou"):
            store._mas_dtm_original_nou_init = store.mas_nou.NOU.__init__
            
        def custom_nou_init(self, *args, **kwargs):
            store._mas_dtm_original_nou_init(self, *args, **kwargs)
            cache_back = os.path.join(renpy.config.gamedir, "_dtm_cache", "nou", "cards", "back.png")
            if os.path.exists(cache_back):
                back_img = store.MASFilterSwitch("_dtm_cache/nou/cards/back.png")
                self.table.back = back_img
                for card_obj in self.table.cards.itervalues():
                    card_obj.back = back_img
                    
        if hasattr(store, "mas_nou"):
            store.mas_nou.NOU.__init__ = custom_nou_init
        
        if hasattr(store, "mas_nou") and not hasattr(store, "_mas_dtm_original_load_card_asset"):
            store._mas_dtm_original_load_card_asset = store.mas_nou.NOU._m1_zz_cardgames__load_card_asset
            
        def custom_load_card_asset(self, card):
            store._mas_dtm_original_load_card_asset(self, card)
            card_png = self._m1_zz_cardgames__get_card_filename(card)
            
            eng_card_png = card_png
            if card_png.startswith("c"):
                eng_card_png = "b" + card_png[1:]
            elif card_png.startswith("v"):
                eng_card_png = "g" + card_png[1:]
            elif card_png.startswith("a"):
                eng_card_png = "y" + card_png[1:]
                
            cache_path_sp = os.path.join(renpy.config.gamedir, "_dtm_cache", "nou", "cards", card_png + ".png")
            cache_path_en = os.path.join(renpy.config.gamedir, "_dtm_cache", "nou", "cards", eng_card_png + ".png")
            
            if os.path.exists(cache_path_sp):
                self.table.card(card, "_dtm_cache/nou/cards/" + card_png + ".png")
                self.table.set_faceup(card, False)
            elif os.path.exists(cache_path_en):
                self.table.card(card, "_dtm_cache/nou/cards/" + eng_card_png + ".png")
                self.table.set_faceup(card, False)
                
        if hasattr(store, "mas_nou"):
            store.mas_nou.NOU._m1_zz_cardgames__load_card_asset = custom_load_card_asset
            
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

        if hasattr(store, "mas_nou"):
            sfx_dir = os.path.join(cache_dir, "sfx")
            if os.path.exists(sfx_dir):
                name_to_sfx_list_map = {
                    "shuffle": store.mas_nou.NOU.SFX_SHUFFLE,
                    "move": store.mas_nou.NOU.SFX_MOVE,
                    "slide": store.mas_nou.NOU.SFX_DRAW,
                    "place": store.mas_nou.NOU.SFX_PLAY,
                    "shove": store.mas_nou.NOU.SFX_PLAY
                }
                found_types = set()
                for f in os.listdir(sfx_dir):
                    if f.endswith(store.mas_nou.NOU.SFX_EXT):
                        found_types.add(f.partition("_")[0])
                        
                for t in found_types:
                    lst = name_to_sfx_list_map.get(t)
                    if lst is not None:
                        del lst[:]
                        
                for f in os.listdir(sfx_dir):
                    if f.endswith(store.mas_nou.NOU.SFX_EXT):
                        lst = name_to_sfx_list_map.get(f.partition("_")[0])
                        if lst is not None:
                            lst.append(internal_nou_path + "sfx/" + f)
                        
        renpy.display.im.cache.clear()
        if not startup:
            force_update_mas_visuals()
            renpy.notify("Texturas de NOU aplicadas exitosamente")

    # ==========================================
    # TABLE TEXTURE LOGIC
    # ==========================================
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
            store.monika_chr.tablechair.table = store.persistent._mas_dtm_overrides["table"]

    # ==========================================
    # EYE TEXTURE LOGIC
    # ==========================================
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
            original_len = len(rk_list)
            store._mas_dtm_original_rk_face(rk_list, eyes, eyebrows, nose, mouth, flt, fpfx, lean, sweat, tears, emote)
            
            if len(rk_list) == original_len or eyes not in store.persistent._mas_dtm_overrides["eye_map"]:
                return
            
            custom_eye_path = store.persistent._mas_dtm_overrides["eye_map"][eyes]
            
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
            
            last_rk = list(rk_list[-1])
            last_rk[2] = renpy.display.im.Composite((1280, 850), *img_str_list)
            rk_list[-1] = tuple(last_rk)

        store.mas_sprites._rk_face = custom_rk_face

screen dtm_background_apply_nou_timer():
    timer 0.1 action Hide("dtm_background_apply_nou_timer")

screen dtm_background_apply_chess_timer():
    timer 0.1 action Hide("dtm_background_apply_chess_timer")


init 1000 python:
    store.dtm_core.apply_sprite_overrides()
    store.dtm_core.apply_table_overrides()
    if hasattr(store, "MASChessDisplayableBase"):
        store.dtm_core.apply_chess_overrides(sync=True)
    store.dtm_core.apply_pong_overrides()
    store.dtm_core.apply_nou_overrides(sync=True)
