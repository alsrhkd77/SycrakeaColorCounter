import sys
import tkinter
from tkinter import messagebox
from tk_winodw import TkWindow
from initializer import Initializer
from pynput import keyboard


def color1_plus():
    global tk
    tk.plus(0)


def color2_plus():
    global tk
    tk.plus(1)


def color3_plus():
    global tk
    tk.plus(2)


def color4_plus():
    global tk
    tk.plus(3)


def color1_minus():
    global tk
    tk.minus(0)


def color2_minus():
    global tk
    tk.minus(1)


def color3_minus():
    global tk
    tk.minus(2)


def color4_minus():
    global tk
    tk.minus(3)


def reset():
    global tk
    tk.init()


def toggle_overlay():
    global tk
    tk.set_overlay(not tk.overlay)


def destroy():
    global tk
    tk.destroy()
    sys.exit()


def show_error(errors):
    string = "설정이 올바르지 않아\n기본 설정이 적용되었습니다\n"
    for e in errors:
        string = string + "\n" + e
    messagebox.showwarning("설정 적용 불가", string)


if __name__ == '__main__':
    global tk, window, hot_keys
    hot_key = {}
    functions = {
        "colors_1+": color1_plus,
        "colors_2+": color2_plus,
        "colors_3+": color3_plus,
        "colors_4+": color4_plus,
        "colors_1-": color1_minus,
        "colors_2-": color2_minus,
        "colors_3-": color3_minus,
        "colors_4-": color4_minus,
        "reset": reset,
        "toggle_overlay": toggle_overlay,
        "exit_program": destroy,
    }
    initializer = Initializer()
    if len(initializer.error) > 0:
        show_error(initializer.error)
    for h in initializer.settings["hot_keys"].keys():
        if initializer.settings["hot_keys"][h] != "":
            hot_key[initializer.settings["hot_keys"][h]] = functions[h]
    window = tkinter.Tk()
    tk = TkWindow(window, initializer.settings)
    hot_keys = keyboard.GlobalHotKeys(hot_key)
    hot_keys.start()
    window.mainloop()
