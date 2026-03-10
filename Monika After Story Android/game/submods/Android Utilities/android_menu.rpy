init -998 python:
    # [SAFETY] Variable Fallback Checks
    # Ensure ANDROID constants exist even if zz_android_setup was skipped or failed
    if not hasattr(store, 'ANDROID_PUBLIC_PATH'):
        store.ANDROID_PUBLIC_PATH = "/storage/emulated/0/Monika After Story/"
    
    if not hasattr(store, 'ANDROID_CHARACTERS_PATH'):
        store.ANDROID_CHARACTERS_PATH = os.path.join(store.ANDROID_PUBLIC_PATH, "characters/")

    if not hasattr(store, 'ANDROID_CUSTOM_GIFTS_PATH'):
        store.ANDROID_CUSTOM_GIFTS_PATH = os.path.join(store.ANDROID_PUBLIC_PATH, "custom_gifts/")

# =============================================================================
# SUBMOD SETTINGS PANE
# =============================================================================
screen mas_mobile_utils_settings():
    vbox:
        pass

init python:
    import os

    def mas_android_create_gift(filename, content=""):
        """
        Creates a gift file in the characters directory.
        Modern replacement for the legacy open() calls.
        
        IN:
            filename: Name of the file (e.g., 'coffee.gift')
            content: Optional content to write (default empty for gifts)
        """
        try:
            # User Request: Ensure we use the correct internal/external path map
            # Since zz_android_setup redirects basedir, ANDROID_CHARACTERS_PATH is the correct place
            # for MAS to find it.
            target_path = os.path.join(store.ANDROID_CHARACTERS_PATH, filename)
            
            # Ensure directory exists just in case
            if not os.path.exists(store.ANDROID_CHARACTERS_PATH):
                try:
                    os.makedirs(store.ANDROID_CHARACTERS_PATH)
                except:
                    pass

            # Create the file
            with open(target_path, "w") as f:
                f.write(content)
            
            renpy.notify("Archivo creado: " + filename)
            
        except Exception as e:
            renpy.notify("Error creando archivo: " + str(e))
            print("[Mobile Utilities] Error creating gift: " + str(e))


# =============================================================================
# MODERNIZED UI
# =============================================================================


style mas_android_choice_vbox is talk_choice_vbox
style mas_android_choice_button is talk_choice_button:
    xsize 460
    padding (20, 5, 20, 5)
style mas_android_choice_button_dark is talk_choice_button_dark:
    xsize 460
    padding (20, 5, 20, 5)
style mas_android_choice_button_text is talk_choice_button_text
style mas_android_choice_button_text_dark is talk_choice_button_text_dark

screen mas_android_talk_choice(items):
    style_prefix "mas_android_choice"

    viewport:
        id "android_choice_vp"
        area (800, 40, 480, 640) # Ajustado más a la derecha
        scrollbars "vertical"
        mousewheel True
        draggable True
        
        vbox:
            # We explicitly override the style's potential positional properties 
            # to ensure it sits inside the viewport correctly
            xalign 0.5
            yalign 0.0
            
            for i in items:
                textbutton renpy.substitute(i.caption) action i.action

# =============================================================================
# ANDROID MENU LOGIC
# =============================================================================

default persistent._mas_hidesearch = False

label anmenu:
    # Main Entry Point
    python:
        menu_items = [
            (_("Crear un regalo"), "giftmenu"),
            (_("Ver afecto"), "aff_android_log"),
            (_("Cambiar texturas"), "dtm_android_main")
        ]
        
        if persistent._mas_hidesearch:
            menu_items.append((_("Activar la barra de búsqueda"), "toggle_search"))
        else:
            menu_items.append((_("Desactivar la barra de búsqueda"), "toggle_search"))
            
        menu_items.append((_("Regresar"), "return"))

    $ result = renpy.display_menu(menu_items, screen="mas_android_talk_choice")

    if result == "giftmenu":
        jump giftmenu
    elif result == "aff_android_log":
        jump aff_android_log

    elif result == "toggle_search":
        $ persistent._mas_hidesearch = not persistent._mas_hidesearch
        if persistent._mas_hidesearch:
            $ renpy.notify("La barra de búsqueda está desactivada.")
        else:
            $ renpy.notify("La barra de búsqueda está activada.")
        jump anmenu
    
    elif result == "return":
        jump prompt_menu
    
    elif result == "dtm_android_main":
        jump dtm_android_main

    else:
        jump prompt_menu

label aff_android_log:
    $ current_aff = int(round(_mas_getAffection()))
    $ nickname = persistent._mas_player_nickname
    "El afecto de [m_name] es de [current_aff] puntos."
    jump anmenu



# =============================================================================
# GIFT MENUS
# =============================================================================

label giftmenu:
    python:
        gift_categories = [
            ("Cintas", "menuCinta"),
            ("Consumibles", "menucnsb"),
            ("Ropa", "ropa_menu"),
            ("Accesorios", "acsand"),
            ("Otros", "others"),
            ("Volver", "return")
        ]
    
    $ cat_res = renpy.display_menu(gift_categories, screen="mas_android_talk_choice")
    
    if cat_res == "return":
        jump anmenu
    else:
        jump expression cat_res

label menuCinta:
    python:
        cintas = [
            ("Cinta color amarillo", "cintaamarilla.gift"),
            ("Cinta color azul", "cintaazul.gift"),
            ("Cinta color azul cerceta", "cintaazulcerceta.gift"),
            ("Cinta blanca y negra", "cintablancaynegra.gift"),
            ("Cinta color anaranjado", "cintacoloanaranjado.gift"),
            ("Cinta color azul cielo", "cintacolorazulcielo.gift"),
            ("Cinta color azul marino", "cintacolorazulmarino.gift"),
            ("Cinta color bronce", "cintacolorbronce.gift"),
            ("Cinta color café", "cintacolorcafe.gift"),
            ("Cinta color lila", "cintacolorlila.gift"),
            ("Cinta color marrón", "cintacolormarron.gift"),
            ("Cinta color oro", "cintacolororo.gift"),
            ("Cinta color púpura royal", "cintacolorpupuraroyal.gift"),
            ("Cinta color rosa caliente", "cintacolorrosacaliente.gift"),
            ("Cinta color verde lima", "cintacolorverdelima.gift"),
            ("Cinta color durazno", "cintadurazno.gift"),
            ("Cinta color esmeralda", "cintaesmeralda.gift"),
            ("Cinta color gris", "cintagris.gift"),
            ("Cinta color negro", "cintanegra.gift"),
            ("Cinta color plateada", "cintaplateada.gift"),
            ("Cinta color platino", "cintaplatino.gift"),
            ("Cinta color púpura claro", "cintapurpuraclaro.gift"),
            ("Cinta color púpura oscuro", "cintapurpuraoscuro.gift"),
            ("Cinta color roja", "cintaroja.gift"),
            ("Cinta color rosada", "cintarosada.gift"),
            ("Cinta color rubí", "cintarubi.gift"),
            ("Cinta color verde", "cintaverde.gift"),
            ("Cinta color zafiro", "cintazafiro.gift"),
            ("Cinta color amarillo tipo-s", "cintacoloramarillotipos.gift"),
            ("Cinta color azul tipo-s", "cintacolorazultipos.gift"),
            ("Cinta color blanco tipo-s", "cintacolorblancotipos.gift"),
            ("Cinta color esmeralda tipo-s", "cintacoloresmeraldatipos.gift"),
            ("Cinta color gris tipo-s", "cintacolorgristipos.gift"),
            ("Cinta color melocotón tipo-s", "cintacolormelocotontipos.gift"),
            ("Cinta color negro tipo-s", "cintacolornegrotipos.gift"),
            ("Cinta color plata tipo-s", "cintacolorplatatipos.gift"),
            ("Cinta color platino tipo-s", "cintacolorplatinotipos.gift"),
            ("Cinta color púpura claro tipo-s", "cintacolorpupuraclarotipos.gift"),
            ("Cinta color púpura oscuro tipo-s", "cintacolorpupuraoscurotipos.gift"),
            ("Cinta color rojo tipo-s", "cintacolorrojotipos.gift"),
            ("Cinta color rosa tipo-s", "cintacolorrosatipos.gift"),
            ("Cinta color ruby tipo-s", "cintacolorrubytipos.gift"),
            ("Cinta color safiro tipo-s", "cintacolorsafirotipos.gift"),
            ("Cinta color turqueza tipo-s", "cintacolorturquezatipos.gift"),
            ("Cinta color verde tipo-s", "cintacolorverdetipos.gift"),
            ("Cinta color vinp tipo-s", "cintacolorvinptipos.gift"),
            ("Cinta gemela color amarillo", "cintagemelacoloramarillo.gift"),
            ("Cinta gemela color azul", "cintagemelacolorazul.gift"),
            ("Cinta gemela color rosa", "cintagemelacolorrosa.gift"),
            ("Cinta gemela color verde", "cintagemelacolorverde.gift"),
            ("Cinta con degradado", "cintacondegradado.gift"),
            ("Cinta con degradado arco iris", "cintacondegradadoarcoiris.gift"),
            ("Cinta con degradado de bajo poliéster", "cintacondegradadodebajopoliester.gift"),
            ("Cinta con lunares blancos sobre rojo", "cintaconlunaresblancossobrerojo.gift"),
            ("Cinta con rayas azules y blancas", "cintaconrayasazulesyblancas.gift"),
            ("Cinta con rayas rosas y blancas", "cintaconrayasrosasyblancas.gift"),
            ("Cinta con temática del orgullo bisexual", "cintaorgullobisexual.gift"),
            ("Cinta con temática del orgullo transexual", "cintacontematicadelorgullotransexual.gift"),
            ("Cinta amdek ámbar", "cintaamdekambar.gift"),
            ("Cinta azul 8-bit", "cintaazul8bit.gift"),
            ("Cinta blanca 8-bit", "cintablanca8bit.gift"),
            ("Cinta cielo negro estrellado", "cintacielonegroestrellado.gift"),
            ("Cinta de cielo rojo estrellado", "cintadecielorojoestrellado.gift"),
            ("Cinta esmeralda 8-bit", "cintaesmeralda8bit.gift"),
            ("Cinta game boy verde", "cintagameboyverde.gift"),
            ("Cinta púrpura 8-bit", "cintapurpura8bit.gift"),
            ("Cinta roja 8-bit", "cintaroja8bit.gift"),
            ("Cinta super game boy verde", "cintasupergameboyverde.gift"),
            ("Coletero azul de conejita", "coleteroazuldeconejita.gift"),
            ("Lazo de color negro", "lazodecolornegro.gift"),
            ("Cintilla color amarillo", "cintillacoloramarillo.gift"),
            ("Cintilla color anaranjado", "cintillacoloranaranjado.gift"),
            ("Cintilla color azul cielo", "cintillacolorazulcielo.gift"),
            ("Cintilla color azul royal", "cintillacolorazulroyal.gift"),
            ("Cintilla color blanco", "cintillacolorblanco.gift"),
            ("Cintilla color gris", "cintillacolorgris.gift"),
            ("Cintilla color negro", "cintillacolornegro.gift"),
            ("Cintilla color púrpura", "cintillacolorpurpura.gift"),
            ("Cintilla color rojo", "cintillacolorrojo.gift"),
            ("Cintilla color rosa", "cintillacolorrosa.gift"),
            ("Cintilla color rosa oscuro", "cintillacolorrosaoscuro.gift"),
            ("Cintilla color verde pálido", "cintillacolorverdepalido.gift"),
            ("Volver", "return")
        ]
    
    $ result = renpy.display_menu(cintas, screen="mas_android_talk_choice")
    
    if result == "return":
        jump giftmenu
    else:
        $ mas_android_create_gift(result)
        jump menuCinta

label menucnsb:
    python:
        consumables = [
            ("Chocolates", "chocolates.gift"),
            ("Café", "cafe.gift"),
            ("Dulce", "dulce.gift"),
            ("Maíz Dulce", "maizdulce.gift"),
            ("Chocolate Caliente", "chocolatecaliente.gift"),
            ("Caramelo", "caramelo.gift"),
            ("Galletas de Navidad", "galletanavideña.gift"),
            ("Bastones de Caramelo", "bastonescaramelo.gift"),
            ("Cupcake", "cupcake.gift"),
            ("Volver", "return")
        ]
    
    $ result = renpy.display_menu(consumables, screen="mas_android_talk_choice")
    
    if result == "return":
        jump giftmenu
    else:
        $ mas_android_create_gift(result)
        jump menucnsb

label ropa_menu:
    python:
        clothes = [
            ("Bikini de color amarillo con escote de corazón", "bikinidecoloramarilloconescotedecorazon.gift"),
            ("Bikini de color blanco con escote de corazón", "bikinidecolorblancoconescotedecorazon.gift"),
            ("Bikini de color negro con escote de corazón", "bikinidecolornegroconescotedecorazon.gift"),
            ("Bikini de color púrpura con escote de corazón", "bikinidecolorpurpuraconescotedecorazon.gift"),
            ("Bikini de color rosa con escote de corazón", "bikinidecolorrosaconescotedecorazon.gift"),
            ("Bikini de color verde con escote de corazón", "bikinidecolorverdeconescotedecorazon.gift"),
            ("Bikini de concha", "bikinideconcha.gift"),
            ("Camisa color rosa", "camisacolorrosa.gift"),
            ("Camisa de flores", "camisadeflores.gift"),
            ("Camiseta blanca de tirantes cruzados de corte en V", "camisetablancadetirantescruzadosdecorteenv.gift"),
            ("Camiseta de color azul", "camisetadecolorazul.gift"),
            ("Camiseta de Jurassic Park", "camisetadejurassicpark.gift"),
            ("Camiseta de Jurassic World", "camisetadejurassicworld.gift"),
            ("Camiseta descansa aquí", "camisetadescansaaqui.gift"),
            ("Camiseta pon cara de felicidad", "camisetaponcaradefelicidad.gift"),
            ("Camiseteta color blanco", "camisetacolorblanco.gift"),
            ("Chaleco jersey color azul", "chalecojerseycolorazul.gift"),
            ("Chaqueta color marrón", "chaquetacolormarron.gift"),
            ("Corpiño con volantes color rojo", "corpinoconvolantescolorrojo.gift"),
            ("Hatsune Miku", "hatsunemiku.gift"),
            ("Jersey beige de cuello alto", "jerseybeigedecuelloalto.gift"),
            ("Jersey color vino asimétrico", "jerseycolorvinoasimetrico.gift"),
            ("Jersey con rayas blancas y negras", "jerseyconrayasblancasynegras.gift"),
            ("Jersey sin hombros", "jerseysinhombros.gift"),
            ("Kimono color rosa", "kemonorosa.gift"),
            ("Sakuya Izayoi", "sakuyaizayoi.gift"),
            ("Sudadera color verde con capucha", "sudaderacolorverdeconcapucha.gift"),
            ("Suéter color negro sin mangas", "suetercolornegrosinmangas.gift"),
            ("Uniforme de la academia Shuchi'in", "uniformedelaacademiashuchiin.gift"),
            ("Vestido blanco con azul marino", "vestidoblancoconazulmarino.gift"),
            ("Vestido color azul oscuro brillante", "vestidocolorazuloscurobrillante.gift"),
            ("Vestido de color verde", "vestidodecolorverde.gift"),
            ("YoRHa Nº2 Tipo B", "yorhanotipob.gift"),
            ("Volver", "return")
        ]
        
    $ result = renpy.display_menu(clothes, screen="mas_android_talk_choice")
    
    if result == "return":
        jump giftmenu
    else:
        $ mas_android_create_gift(result)
        jump ropa_menu

label acsand:
    python:
        accessories = [
            ("Flor rosada", "florrosada.gift"),
            ("Gargantilla blanca de seda", "gargantillablancadeseda.gift"),
            ("Gargantilla con pinchos de estrellas", "gargantillaconpinchosdeestrellas.gift"),
            ("Gargantilla corazón", "gargantillacorazon.gift"),
            ("Gargantilla de ancla", "gargantilladeancla.gift"),
            ("Gargantilla de Animal Crossing", "gargantilladeanimalcrossing.gift"),
            ("Gargantilla de cactus", "gargantilladecactus.gift"),
            ("Gargantilla de cadena de oro", "gargantilladecadenedeoro.gift"),
            ("Gargantilla de cadena plateada", "gargantillacadenaplata.gift"),
            ("Gargantilla de caracol", "gargantilladecaracol.gift"),
            ("Gargantilla de espiral negra", "gargantilladeespiralnegra.gift"),
            ("Gargantilla de estrella púrpura", "gargantilladestrellapurpura.gift"),
            ("Gargantilla de girasol", "gargantilladegirasol.gift"),
            ("Gargantilla de hilos", "gargantilladehilos.gift"),
            ("Gargantilla de lazo rojo", "gargantilladelazorojo.gift"),
            ("Gargantilla de margaritas blancas", "gargantillademargaritasblancas.gift"),
            ("Gargantilla de triforce", "gargantilladetriforce.gift"),
            ("Gargantilla de volantes rojos", "gargantilladevolantesrojos.gift"),
            ("Gargantilla floreada", "gargantillafloreada.gift"),
            ("Gargantilla simple", "gargantillasimple.gift"),
            ("Gargantilla verde esmeralda", "gargantillaverdeesmeralda.gift"),
            ("Gargantillad de plata brillante", "gargantilladdeplatabrillante.gift"),
            ("Horquilla 8ª nota", "horquilla8nota.gift"),
            ("Horquilla de calabaza", "horquilladecalabaza.gift"),
            ("Horquilla de cereza", "horquilladecereza.gift"),
            ("Horquilla de corazón", "horquilladecorazon.gift"),
            ("Horquilla de fantasma", "horquilladefantasma.gift"),
            ("Horquilla de luna creciente", "horquilladelunacreciente.gift"),
            ("Horquilla de murciélago", "horquillademurcielago.gift"),
            ("Lazo delantero negro", "lazodelanteronegro.gift"),
            ("Pendientes de perlas", "pendientesdeperlas.gift"),
            ("Piercings negro-plata", "piercingsnegroplata.gift"),
            ("Volver", "return")
        ]
    
    $ result = renpy.display_menu(accessories, screen="mas_android_talk_choice")
    
    if result == "return":
        jump giftmenu
    else:
        $ mas_android_create_gift(result)
        jump acsand

label others:
    python:
        others_list = [
            ("Rosas", "rosas.gift"),
            ("Peluche quetzal", "peluchequetzal.gift"),
            ("Anillo de promesa", "anillopromesa.gift"),
            ("Taza térmica", "termosolomonika.gift"),
            ("Volver", "return")
        ]
    
    $ result = renpy.display_menu(others_list, screen="mas_android_talk_choice")
    
    if result == "return":
        jump giftmenu
    else:
        $ mas_android_create_gift(result)
        jump others


# Helper screen for simple gift lists to reduce code duplication

# =============================================================================
# ANDROID TEXTURE MANAGER
# =============================================================================

init python:
    def mas_android_get_texture_folders(sub_path):
        import os
        base_path = os.path.join(store.ANDROID_PUBLIC_PATH, "textures", sub_path)
        folders = []
        if os.path.exists(base_path):
            for d in os.listdir(base_path):
                if os.path.isdir(os.path.join(base_path, d)):
                    folders.append(d)
        return folders

label dtm_android_main:
    python:
        dtm_main_items = [
            ("Monika", "dtm_android_monika"),
            ("Juegos", "dtm_android_games"),
            ("Volver", "return")
        ]
    $ result = renpy.display_menu(dtm_main_items, screen="mas_android_talk_choice")
    if result == "return":
        jump anmenu
    else:
        jump expression result

label dtm_android_monika:
    python:
        dtm_m_items = [
            ("Ojos", "dtm_android_scan_eyes"),
            ("Boca", "dtm_android_scan_mouth"),
            ("Volver", "return")
        ]
    $ result = renpy.display_menu(dtm_m_items, screen="mas_android_talk_choice")
    if result == "return":
        jump dtm_android_main
    else:
        jump expression result

label dtm_android_games:
    python:
        dtm_g_items = [
            ("Ajedrez", "dtm_android_scan_chess"),
            ("Pong", "dtm_android_scan_pong"),
            ("NOU", "dtm_android_scan_nou"),
            ("Volver", "return")
        ]
    $ result = renpy.display_menu(dtm_g_items, screen="mas_android_talk_choice")
    if result == "return":
        jump dtm_android_main
    else:
        jump expression result

label dtm_android_scan_eyes:
    python:
        folders = mas_android_get_texture_folders("monika/eyes")
        items = [(f, f) for f in folders]
        items.append(("Restaurar Original", "restaurar"))
        items.append(("Volver", "return"))
    $ result = renpy.display_menu(items, screen="mas_android_talk_choice")
    if result == "return":
        jump dtm_android_monika
    elif result == "restaurar":
        python:
            if hasattr(store, "dtm_core"):
                store.dtm_core.reset_eye_textures()
        $ renpy.notify("Texturas restauradas")
        jump dtm_android_scan_eyes
    else:
        python:
            if hasattr(store, "dtm_core"):
                # Asumimos override general o pasamos el nombre de la carpeta para futuro mapeo
                store.dtm_core.set_eye_texture("e", result)
        $ renpy.notify("Textura cambiada exitosamente")
        jump dtm_android_scan_eyes

label dtm_android_scan_mouth:
    python:
        folders = mas_android_get_texture_folders("monika/mouth")
        items = [(f, f) for f in folders]
        items.append(("Restaurar Original", "restaurar"))
        items.append(("Volver", "return"))
    $ result = renpy.display_menu(items, screen="mas_android_talk_choice")
    if result == "return":
        jump dtm_android_monika
    elif result == "restaurar":
        # Placeholder till mouth reset is implemented
        $ renpy.notify("Texturas restauradas")
        jump dtm_android_scan_mouth
    else:
        $ renpy.notify("Textura cambiada exitosamente")
        jump dtm_android_scan_mouth

label dtm_android_scan_chess:
    python:
        folders = mas_android_get_texture_folders("games/chess")
        items = [(f, f) for f in folders]
        items.append(("Restaurar Original", "restaurar"))
        items.append(("Volver", "return"))
    $ result = renpy.display_menu(items, screen="mas_android_talk_choice")
    if result == "return":
        jump dtm_android_games
    elif result == "restaurar":
        python:
            if hasattr(store, "dtm_core"):
                store.dtm_core.reset_chess_pieces()
        $ renpy.notify("Texturas restauradas")
        jump dtm_android_scan_chess
    else:
        python:
            # Pasa el nombre de la carpeta como identificador
            pass
        $ renpy.notify("Textura cambiada exitosamente")
        jump dtm_android_scan_chess

label dtm_android_scan_pong:
    python:
        folders = mas_android_get_texture_folders("games/pong")
        items = [(f, f) for f in folders]
        items.append(("Restaurar Original", "restaurar"))
        items.append(("Volver", "return"))
    $ result = renpy.display_menu(items, screen="mas_android_talk_choice")
    if result == "return":
        jump dtm_android_games
    elif result == "restaurar":
        python:
            if hasattr(store, "dtm_core"):
                store.dtm_core.reset_pong_textures()
        $ renpy.notify("Texturas restauradas")
        jump dtm_android_scan_pong
    else:
        python:
            if hasattr(store, "dtm_core"):
                import os
                # Pasamos la ruta completa de la carpeta del pong seleccionado
                pong_folder = os.path.join(store.ANDROID_PUBLIC_PATH, "textures", "games", "pong", result)
                store.dtm_core.set_pong_textures(pong_folder)
        $ renpy.notify("Textura cambiada exitosamente")
        jump dtm_android_scan_pong

label dtm_android_scan_nou:
    python:
        folders = mas_android_get_texture_folders("games/nou")
        items = [(f, f) for f in folders]
        items.append(("Restaurar Original", "restaurar"))
        items.append(("Volver", "return"))
    $ result = renpy.display_menu(items, screen="mas_android_talk_choice")
    if result == "return":
        jump dtm_android_games
    elif result == "restaurar":
        $ renpy.notify("Texturas restauradas")
        jump dtm_android_scan_nou
    else:
        $ renpy.notify("Textura cambiada exitosamente")
        jump dtm_android_scan_nou
