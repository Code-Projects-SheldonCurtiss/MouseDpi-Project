import ctypes
import keyboard
import tkinter as tk
# import Tkinter as tk

# Settings
# Set to whatever will allow you to easily navigate menus
NavigationSpeed = 2
# 10 = 5/10 which is the default windows sensitivity you should be using this
GamingSpeed = 10
# Speed when application is closed - Either NavigationSpeed or GamingSpeed
CloseSpeed = NavigationSpeed
NavigationHotkey = 'alt+1'
GamingHotkey = 'alt+2'

# Func for changing mouse speed
def change_speed(speed=10):
    set_mouse_speed = 113  # 0x0071 for SPI_SETMOUSESPEED
    ctypes.windll.user32.SystemParametersInfoA(set_mouse_speed, 0, speed, 0)

# Resets Mouse to default speed on application close
def proper_close():
    change_speed(CloseSpeed)
    root.destroy()

root = tk.Tk()
root.protocol('WM_DELETE_WINDOW', proper_close)

# Simple way to set the window size because I'm lazy.
tk.Button(root, text='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~').pack(expand=True, fill='x')

# Sets to really slow so we can use desktop like normal.
tk.Button(root, text='Navigation', command=lambda: change_speed(NavigationSpeed)).pack(expand=True, fill='x')

# Sets to 6/11 so we can use in game.
tk.Button(root, text='Gaming', command=lambda: change_speed(GamingSpeed)).pack(expand=True, fill='x')

# Hotkeys
keyboard.add_hotkey(NavigationHotkey, lambda: change_speed(NavigationSpeed))
keyboard.add_hotkey(GamingHotkey, lambda: change_speed(GamingSpeed))

root.mainloop()
