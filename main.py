import tkinter
from tk_winodw import TkWindow
from pynput import keyboard


def first():
    global tk
    tk.plus(0)


def second():
    global tk
    tk.plus(1)


def third():
    global tk
    tk.plus(2)


def fourth():
    global tk
    tk.plus(3)


def overlay():
    global tk
    tk.set_overlay(False)


def destroy():
    global tk, hot_keys
    hot_keys.stop()
    tk.destroy()


if __name__ == '__main__':
    global tk, window, hot_keys
    colors = ["red", "blue", "yellow", "white"]
    colors_korean = {"red": "빨", "blue": "파", "white": "흰", "yellow": "노"}
    hot_key = {
        "<alt>+a": first,
        "<alt>+s": second,
        "<alt>+d": third,
        "<alt>+f": fourth,
        "<alt>+o": overlay,
        "<alt>+q": destroy,
    }
    hot_keys = keyboard.GlobalHotKeys(hot_key)
    hot_keys.start()
    window = tkinter.Tk()
    tk = TkWindow(window, colors=colors, colors_korean=colors_korean, font_size=25)
    window.mainloop()
    hot_keys.join()
