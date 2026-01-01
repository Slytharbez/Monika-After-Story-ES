init 999 python:
    # Force the flags to True so the UI buttons appear
    store.mas_windowreacts.can_do_windowreacts = True
    store.mas_windowreacts.can_show_notifs = True

    # Define a dummy function that does nothing but returns True (success)
    def force_ui_dummy_notif(title, body):
        return True

    # Check if the notification function is likely to crash (e.g. if dependencies failed)
    # We simply overwrite it to be safe, since the user said they don't care if it functionality works.
    # This prevents 'NameError' or 'AttributeError' if the original libraries failed to load.
    if store.mas_windowutils._tryShowNotif is None or True: 
        store.mas_windowutils._tryShowNotif = force_ui_dummy_notif

    # Also mock window getting functions if they are broken/missing to prevent other crashes
    if not hasattr(store.mas_windowutils, "_window_get") or store.mas_windowutils._window_get is None:
        store.mas_windowutils._window_get = lambda: ""
