import ctypes
from ctypes import wintypes
import sys
import os

# Load DLLs
user32 = ctypes.windll.user32
shell32 = ctypes.windll.shell32
kernel32 = ctypes.windll.kernel32

# Define types
HWND = wintypes.HWND
RECT = wintypes.RECT
POINT = wintypes.POINT
LPARAM = wintypes.LPARAM
BOOL = wintypes.BOOL
HANDLE = wintypes.HANDLE
HICON = wintypes.HANDLE
HINSTANCE = wintypes.HANDLE
HMODULE = wintypes.HANDLE
LPCTSTR = ctypes.c_wchar_p

# Constants
NIM_ADD = 0
NIM_MODIFY = 1
NIM_DELETE = 2
NIF_MESSAGE = 0x00000001
NIF_ICON = 0x00000002
NIF_TIP = 0x00000004
NIF_INFO = 0x00000010
NIF_REALTIME = 0x00000040

NIIF_NONE = 0x00000000   
NIIF_INFO = 0x00000001
NIIF_WARNING = 0x00000002
NIIF_ERROR = 0x00000003
NIIF_USER = 0x00000004
NIIF_NOSOUND = 0x00000010
NIIF_LARGE_ICON = 0x00000020

WM_USER = 0x0400
WM_DESTROY = 0x0002

WS_OVERLAPPED = 0x00000000
WS_SYSMENU = 0x00080000
CW_USEDEFAULT = 0x80000000

IMAGE_ICON = 1
LR_LOADFROMFILE = 0x00000010
LR_DEFAULTSIZE = 0x00000040

# Window Proc Callback type
WNDPROC = ctypes.WINFUNCTYPE(ctypes.c_long, HWND, ctypes.c_uint, ctypes.c_int, ctypes.c_int)

class WNDCLASS(ctypes.Structure):
    _fields_ = [('style', ctypes.c_uint),
                ('lpfnWndProc', WNDPROC),
                ('cbClsExtra', ctypes.c_int),
                ('cbWndExtra', ctypes.c_int),
                ('hInstance', HINSTANCE),
                ('hIcon', HICON),
                ('hCursor', HANDLE),
                ('hbrBackground', HANDLE),
                ('lpszMenuName', LPCTSTR),
                ('lpszClassName', LPCTSTR)]

class NOTIFYICONDATA(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_uint),
                ("hWnd", HWND),
                ("uID", ctypes.c_uint),
                ("uFlags", ctypes.c_uint),
                ("uCallbackMessage", ctypes.c_uint),
                ("hIcon", HICON),
                ("szTip", ctypes.c_wchar * 128),
                ("dwState", ctypes.c_uint),
                ("dwStateMask", ctypes.c_uint),
                ("szInfo", ctypes.c_wchar * 256),
                ("uTimeout", ctypes.c_uint),
                ("szInfoTitle", ctypes.c_wchar * 64),
                ("dwInfoFlags", ctypes.c_uint)]

def GetForegroundWindow():
    return user32.GetForegroundWindow()

def GetWindowText(hwnd):
    length = user32.GetWindowTextLengthW(hwnd)
    if length > 0:
        buff = ctypes.create_unicode_buffer(length + 1)
        user32.GetWindowTextW(hwnd, buff, length + 1)
        return buff.value
    return u""

def GetWindowRect(hwnd):
    rect = RECT()
    if user32.GetWindowRect(hwnd, ctypes.byref(rect)):
        return (rect.left, rect.top, rect.right, rect.bottom)
    return (-32000, -32000, -32000, -32000)

def GetCursorPos():
    pt = POINT()
    if user32.GetCursorPos(ctypes.byref(pt)):
        return (pt.x, pt.y)
    return (0, 0)

def DestroyWindow(hwnd):
    return user32.DestroyWindow(hwnd)

def find_mas_window_handle(window_title_func):
    found_hwnd = [None]
    WNDENUMPROC = ctypes.WINFUNCTYPE(BOOL, HWND, LPARAM)
    def cb(hwnd, lparam):
        txt = GetWindowText(hwnd)
        if txt == window_title_func():
            found_hwnd[0] = hwnd
            return False 
        return True
    user32.EnumWindows(WNDENUMPROC(cb), 0)
    return found_hwnd[0]

class WindowsBalloonTip:
    def __init__(self):
        self.hwnd = None
        self.hinst = kernel32.GetModuleHandleW(None)
        self.class_name = "PythonTaskbar"
        self._register_class()

    def _register_class(self):
        def wnd_proc(hwnd, msg, wparam, lparam):
            if msg == WM_DESTROY:
                user32.PostQuitMessage(0)
            return user32.DefWindowProcW(hwnd, msg, wparam, lparam)

        self.wnd_proc = WNDPROC(wnd_proc)
        
        wc = WNDCLASS()
        wc.hInstance = self.hinst
        wc.lpszClassName = self.class_name
        wc.lpfnWndProc = self.wnd_proc
        wc.style = WS_OVERLAPPED | WS_SYSMENU
        
        self.class_atom = user32.RegisterClassW(ctypes.byref(wc))

    def showWindow(self, title, msg):
        # Create a hidden dummy window to own the icon
        if not self.hwnd:
            self.hwnd = user32.CreateWindowExW(
                0, self.class_name, "Taskbar",
                0, 0, 0, 0, 0,
                0, 0, self.hinst, None
            )
            user32.UpdateWindow(self.hwnd)

        # Basic ID for logic
        nid = NOTIFYICONDATA()
        nid.cbSize = ctypes.sizeof(NOTIFYICONDATA)
        nid.hWnd = self.hwnd
        nid.uID = 0
        nid.uFlags = NIF_ICON | NIF_MESSAGE | NIF_TIP
        nid.uCallbackMessage = WM_USER + 20
        nid.hIcon = user32.LoadIconW(0, 32512) # IDI_APPLICATION
        nid.szTip = "Monika After Story"

        # Try to load custom icon if it exists
        # Assuming current dir is valid, or search near script
        # icon_path = os.path.abspath("CustomIconWindows.ico")
        # For compatibility with broken renpy paths, let's just use default app icon for now to be safe
        
        if not shell32.Shell_NotifyIconW(NIM_ADD, ctypes.byref(nid)):
            # If add failed, maybe it exists? try modify
            pass

        # Now show the balloon info
        nid.uFlags = NIF_INFO
        nid.szInfo = msg[:255] 
        nid.szInfoTitle = title[:63]
        nid.dwInfoFlags = NIIF_INFO | NIIF_NOSOUND # We handle sound separately in renpy
        
        # Modify to show tip
        success = shell32.Shell_NotifyIconW(NIM_MODIFY, ctypes.byref(nid))
        return bool(success)

    def Destroy(self):
        if self.hwnd:
            nid = NOTIFYICONDATA()
            nid.cbSize = ctypes.sizeof(NOTIFYICONDATA)
            nid.hWnd = self.hwnd
            nid.uID = 0
            shell32.Shell_NotifyIconW(NIM_DELETE, ctypes.byref(nid))
            user32.DestroyWindow(self.hwnd)
            self.hwnd = None

