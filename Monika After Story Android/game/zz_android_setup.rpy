# =================================================================================
# Android Hybrid Storage & Universal Chess System
# =================================================================================
# Este archivo gestiona la lógica específica para Android:
# 1. Solicitud de Permisos
# 2. Creación del Sistema "Mochila" (Hybrid Storage)
# 3. Detección de Arquitectura y Copia de Stockfish
# 4. Redirección de Rutas Críticas (Saves, Logs, Characters, Chess)
# =================================================================================

init -999 python:
    import os
    import platform
    import shutil
    import logging
    from logging import handlers as loghandlers

    # --- CONSTANTES ---
    # Ruta base de la "Mochila" en el almacenamiento externo
    BACKPACK_PATH = "/storage/emulated/0/Monika After Story/"

    # --- FUNCIONES AUXILIARES ---

    def mas_android_request_permissions():
        """
        Solicita permisos de escritura en tiempo de ejecución.
        Esencial para Android 6.0+
        """
        if not renpy.android:
            return

        from jnius import autoclass
        from android.permissions import request_permissions, Permission

        # Solicitar permisos de lectura y escritura
        request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

    def mas_android_setup_backpack():
        """
        Crea la estructura de carpetas necesaria en el almacenamiento externo.
        """
        if not renpy.android:
            return

        dirs_to_create = [
            # Carpetas raíz
            BACKPACK_PATH + "characters",
            BACKPACK_PATH + "chess_games",
            BACKPACK_PATH + "custom_bgm",
            BACKPACK_PATH + "log",
            BACKPACK_PATH + "piano_songs",
            
            # Subcarpetas game/
            BACKPACK_PATH + "game/saves",
            BACKPACK_PATH + "game/submods",
            
            # Subcarpetas mod_assets/
            BACKPACK_PATH + "game/mod_assets/location",
            BACKPACK_PATH + "game/mod_assets/thumbs",
            BACKPACK_PATH + "game/mod_assets/monika/a",
            BACKPACK_PATH + "game/mod_assets/monika/c",
            BACKPACK_PATH + "game/mod_assets/monika/f",
            BACKPACK_PATH + "game/mod_assets/monika/h",
            BACKPACK_PATH + "game/mod_assets/monika/j",
            BACKPACK_PATH + "game/mod_assets/monika/t"
        ]

        for directory in dirs_to_create:
            try:
                if not os.path.exists(directory):
                    os.makedirs(directory)
            except Exception as e:
                # Logueamos en renpy log estandar por ahora pq nuestro sistema de logs aún no está redirigido
                print("[ANDROID_SETUP] Error creando directorio {0}: {1}".format(directory, e))

    def mas_android_install_stockfish():
        """
        Detecta la arquitectura del dispositivo y copia el binario correcto
        de Stockfish a la carpeta privada de ejecución.
        """
        if not renpy.android:
            return

        # 1. Detectar Arquitectura
        arch = platform.machine()
        print("[ANDROID_SETUP] Arquitectura detectada: " + str(arch))

        # Determinar qué binario usar
        # Si es arm64-v8a o aarch64, usamos el de 64 bits. Si no, armv7.
        binary_name = "stockfish-android-armv7" # Default (más compatible)
        if "aarch64" in arch or "armv8" in arch:
            binary_name = "stockfish-android-arm64-v8a"
        
        # 2. Rutas
        # Ruta origen: buscamos en mod_assets/games/chess dentro del APK (game folder)
        source_path = os.path.join(renpy.config.gamedir, "mod_assets/games/chess", binary_name)
        
        # Ruta destino: Carpeta privada ejecutable (internal storage)
        # os.environ['ANDROID_PRIVATE'] apunta a /data/data/package/files
        dest_dir = os.path.join(os.environ['ANDROID_PRIVATE'], "files") 
        dest_path = os.path.join(dest_dir, "stockfish_android") # Nombre genérico en destino

        # 3. Copia y Permisos
        try:
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            # Copiar siempre para asegurar que sea la versión correcta o si se borró
            # OJO: renpy.file() lee de archivos, pero shutil.copy necesita path real.
            # En Android el 'gamedir' suele ser accesible si no está en un .rpa.
            # Asumimos que el usuario puso los binarios como archivos sueltos, NO en los .rpa
            if os.path.exists(source_path):
                shutil.copyfile(source_path, dest_path)
                print("[ANDROID_SETUP] Stockfish copiado exitosamente desde " + source_path)
                
                # Dar permisos de ejecución (chmod 755)
                os.chmod(dest_path, 0o755)
                print("[ANDROID_SETUP] Permisos 755 aplicados a Stockfish.")
            else:
                print("[ANDROID_SETUP] ADVERTENCIA: No se encontró el binario de Stockfish en: " + source_path)

        except Exception as e:
            print("[ANDROID_SETUP] Error instalando Stockfish: " + str(e))


init python:
    # --- EJECUCIÓN INICIAL (Permisos y Setup) ---
    if renpy.android:
        # 1. Pedir Permisos
        try:
            mas_android_request_permissions()
        except Exception as e:
            print("[ANDROID_SETUP] Error solicitando permisos: " + str(e))

        # 2. Crear Mochila (Estructura de Carpetas)
        mas_android_setup_backpack()

        # 3. Instalar Motor de Ajedrez
        mas_android_install_stockfish()

        # 4. Redirección TEMPRANA (Saves)
        # Esto debe hacerse antes de que Ren'Py intente cargar saves si es posible, 
        # aunque el init de saves de renpy suele ser interno. Configurar config.savedir aquí 
        # debería afectar a los nuevos saves y al escaneo.
        config.savedir = os.path.join(BACKPACK_PATH, "game/saves")
        print("[ANDROID_SETUP] config.savedir redirigido a: " + config.savedir)


init 999 python:
    # --- REDIRECCIÓN TARDÍA (Variables de Juego y Logs) ---
    # Usamos init 999 para asegurarnos de que los módulos originales (chess, logging, dockstat)
    # ya se hayan inicializado (suelen ser init 0 o -X).

    if renpy.android:
        # A. Redirigir Ajedrez (Archivos PGN)
        if hasattr(store, "mas_chess"):
            store.mas_chess.CHESS_SAVE_PATH = os.path.join(BACKPACK_PATH, "chess_games/")
            # Recreamos la carpeta por si acaso la variable se usa para otros chequeos
            if not os.path.exists(store.mas_chess.CHESS_SAVE_PATH):
                try:
                    os.makedirs(store.mas_chess.CHESS_SAVE_PATH)
                except:
                    pass
            print("[ANDROID_SETUP] Ajedrez redirigido a: " + store.mas_chess.CHESS_SAVE_PATH)
        
        # B. Redirigir Docking Station (Characters / Regalos)
        if hasattr(store, "mas_docking_station"):
            # store.mas_docking_station es la INSTANCIA de MASDockingStation.
            # Necesitamos cambiar su atributo .station
            store.mas_docking_station.station = os.path.join(BACKPACK_PATH, "characters/")
            
            # Asegurar que existe
            if not os.path.exists(store.mas_docking_station.station):
                try:
                    os.makedirs(store.mas_docking_station.station)
                except:
                    pass
            print("[ANDROID_SETUP] DockingStation redirigida a: " + store.mas_docking_station.station)
        
        # C. Redirigir LOGS (Crítico)
        # Iteramos sobre todos los loggers registrados en mas_logging.LOG_MAP
        # y reemplazamos sus handlers para que apunten a la mochila.
        
        if hasattr(store, "mas_logging") and hasattr(store.mas_logging, "LOG_MAP"):
            new_log_dir = os.path.join(BACKPACK_PATH, "log/")
            if not os.path.exists(new_log_dir):
                try:
                    os.makedirs(new_log_dir)
                except:
                    pass

            print("[ANDROID_SETUP] Iniciando redirección de logs...")
            
            for log_name, logger in store.mas_logging.LOG_MAP.iteritems():
                try:
                    # 1. Cerrar y remover handlers antiguos
                    handlers_to_remove = []
                    for h in logger.handlers:
                        # Identificamos si es un FileHandler
                        if isinstance(h, logging.FileHandler):
                            h.close()
                            handlers_to_remove.append(h)
                    
                    for h in handlers_to_remove:
                        logger.removeHandler(h)

                    # 2. Crear nuevo handler apuntando a la mochila
                    # Usamos RotatingFileHandler como en el original
                    new_log_file = os.path.join(new_log_dir, log_name + ".log")
                    
                    # Usamos los mismos parámetros que 0utils.rpy init_log por defecto
                    new_handler = loghandlers.RotatingFileHandler(
                        new_log_file,
                        maxBytes=5242880, # 5MB
                        backupCount=5,
                        encoding="utf-8"
                    )
                    
                    # Formato por defecto de MAS
                    new_handler.setFormatter(store.mas_logging.MASLogFormatter())
                    new_handler.setLevel(logging.DEBUG)
                    
                    logger.addHandler(new_handler)
                    # logger.info("Log redirigido existosamente a Android Backpack.")

                except Exception as e:
                    print("[ANDROID_SETUP] Error redirigiendo log {0}: {1}".format(log_name, e))

            print("[ANDROID_SETUP] Redirección de logs completada.")
