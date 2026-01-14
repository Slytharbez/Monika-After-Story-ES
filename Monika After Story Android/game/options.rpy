










python early:
    import os
    """
    Note: Android Fix
    Prevent Ren'Py from creating auto-saves (_reload-...) when app pauses or quits.
    This keeps the save folder clean.
    """
    config.save_on_mobile_background = False
    
    if renpy.android:
        """
        Note: Force External Storage
        Logic moved to zz_android_setup.rpy (python early) for earlier execution.
        """
        pass


define gui.show_name = False




define gui.about = _("")






define build.name = "Monika_After_Story"
define config.window_icon = None

define build.icon_presplash = "android-icon.png"

define build.android_icon_foreground = "android-icon-foreground.png"
define build.android_icon_background = "#febce1"

default preferences.text_cps = 50




default preferences.afm_time = 15

default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75



init 50 python:

    from __future__ import print_function

    config.lint_hooks = [
        lambda: print(),
        lambda: print("#"*5, "START MAS LINT HOOKS", "#"*5),
        
        lambda: print(
            "Known uses of deprecated functions/classes in initialisation:",
            (
                "\n".join([msg.rjust(len(msg) + 4) for msg in store.mas_utils._deprecation_warnings])
                if store.mas_utils._deprecation_warnings
                else "    None"
            ),
            "",
            sep="\n"
        ),
        lambda: print("#"*5, "END MAS LINT HOOKS", "#"*5)
    ]

init python:

    mas_override_label("_choose_renderer", "mas_choose_renderer_override")



    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014') 
        s = s.replace(' - ', u'\u2014') 
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)







init python:



























    build.include_update = False





    build.classify("game/gui/**", "archive")


    build.classify("game/mod_assets/**", "archive")

    build.classify("game/*.rpyc", "archive") 
    build.classify("game/dev/*.*",None) 
    build.classify("README.html", "archive") 
    build.classify("game/python-packages/**", "archive")
    build.classify("game/characters/**", "archive")
    build.classify("game/chess_games/**", "archive")
    build.classify("game/piano_songs/**", "archive")
    build.classify("CustomIcon**.**", "archive")


    build.package(build.directory_name + "Mod",'zip',build.name,description='DDLC Compatible Mod')

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)
    build.classify('/game/saves/*.*', None)
    build.classify('**.rpa', "archive")
    build.classify("game/mod_assets/api_keys.json", None)
    build.classify("**.pem", None)




    build.documentation('*.html')
    build.documentation('*.txt')
    build.documentation('*.md')

    build.include_old_themes = False

init python:

    if hasattr(config, "android_permissions"):
        config.android_permissions = [
            "android.permission.VIBRATE",
            "android.permission.WRITE_EXTERNAL_STORAGE",
            "android.permission.READ_EXTERNAL_STORAGE",
            "android.permission.MANAGE_EXTERNAL_STORAGE", 
            "android.permission.POST_NOTIFICATIONS",
            "android.permission.SCHEDULE_EXACT_ALARM"
        ]

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc