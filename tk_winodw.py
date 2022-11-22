import tkinter
import functools
import sys


class TkWindow:
    def __init__(self, window, colors=None, colors_korean=None, hot_keys=None, font_size=25):
        self.overlay_button = None
        self.refresh_button = None
        self.overlay_text_label = None
        if colors is None:
            colors = ["red", "blue", "yellow", "white"]
        if colors_korean is None:
            colors_korean = {"red": "빨강", "blue": "파랑", "white": "하양", "yellow": "노랑"}
        if hot_keys is None:
            hot_keys = ["<alt>+a", "<alt>+s", "<alt>+d", "<alt>+f", "<alt>+q"]

        # Set value
        self.color_label = []
        self.hot_key_label = []
        self.plus_button = []
        self.minus_button = []
        self.colors = colors
        self.colors_korean = colors_korean
        self.hot_keys = hot_keys
        self.font_size = font_size
        self.counter = {}
        self.fontFamily = "맑은 고딕"
        self.init()

        # TkInter setting
        self.window = window
        self.window.title("Sycrakea Color Counter - 햄뮤@Inven")
        self.window.configure(background="#353535")
        self.window.resizable(False, False)  # Height, Width

        self.set_overlay(False)

    # Init counter & label
    def init(self):
        self.counter.clear()
        for c in self.colors:
            self.counter[c] = 0
        if len(self.color_label) > 0:
            for i in range(len(self.color_label)):
                self.color_label[i].config(text=self.colors_korean[self.colors[i]], font=(self.fontFamily, 25))

    def destroy(self):
        self.window.destroy()
        sys.exit()

    def set_overlay(self, check):
        self.window.overrideredirect(check)
        self.window.lift()
        self.window.wm_attributes("-topmost", check)
        self.window.wm_attributes("-disabled", check)  # Click through
        if check:
            self.window.geometry("300x120-5+4")  # Width X Height + x + y
            self.window.wm_attributes("-transparentcolor", "#353535")
            self.window.wm_attributes("-alpha", "0.6")
            self.build_overlay_color_widget()
        else:
            self.window.geometry("400x200-0+0")  # Width X Height + x + y
            # self.window.wm_attributes("-transparentcolor", "#353535")
            self.window.wm_attributes("-alpha", "1.0")
            self.build_foreground_color_widget()

    def build_overlay_color_widget(self):
        # Clear foreground widget
        for c in range(len(self.color_label)):
            self.color_label[c].destroy()
            self.plus_button[c].destroy()
            self.minus_button[c].destroy()
        self.color_label.clear()
        self.plus_button.clear()
        self.minus_button.clear()
        if self.refresh_button is not None:
            self.refresh_button.destroy()
            self.refresh_button = None
        if self.overlay_button is not None:
            self.overlay_button.destroy()
            self.overlay_button = None

        between = 0.2
        for i in range(len(self.colors)):
            # Color label
            label_text = self.colors_korean[self.colors[i]] if self.counter[self.colors[i]] == 0 else str(
                self.counter[self.colors[i]])
            label = tkinter.Label(self.window, text=label_text, font=(self.fontFamily, 25), width=0, height=0,
                                  background="#353535", foreground=self.colors[i], relief="flat")
            label.place(relx=0.1 + (between * i), rely=0.025)
            self.color_label.append(label)
            hot_label = tkinter.Label(self.window, text=self.hot_keys[i].upper(), font=(self.fontFamily, 8, "bold"),
                                      width=0,
                                      height=0, background="#353535", foreground=self.colors[i], relief="flat")
            hot_label.place(relx=0.07 + (between * i), rely=0.45)
            self.hot_key_label.append(hot_label)
        self.overlay_text_label = tkinter.Label(self.window, text="<ALT>+O를 눌러 오버레이 종료\n<ALT>+Q를 눌러 프로그램 종료",
                                                font=(self.fontFamily, 8, "bold"), width=0, height=0,
                                                background="#353535",
                                                foreground="white", relief="flat")
        self.overlay_text_label.place(relx=0.2, rely=0.65)

    def build_foreground_color_widget(self):
        # Clear overlay widget
        for j in range(len(self.color_label)):
            self.color_label[j].destroy()
            self.hot_key_label[j].destroy()
        self.color_label.clear()
        self.hot_key_label.clear()
        if self.overlay_text_label is not None:
            self.overlay_text_label.destroy()
            self.overlay_text_label = None

        between = 0.2
        self.refresh_button = tkinter.Button(self.window, text="초기화", font=(self.fontFamily, 10), width=6, height=0,
                                             command=self.init)
        self.refresh_button.place(relx=0.025, rely=0.07)
        self.overlay_button = tkinter.Button(self.window, text="오버레이 모드", font=(self.fontFamily, 10), width=12,
                                             height=0,
                                             command=functools.partial(self.set_overlay, True))
        self.overlay_button.place(relx=0.74, rely=0.07)
        for i in range(len(self.colors)):
            # Color label
            label_text = self.colors_korean[self.colors[i]] if self.counter[self.colors[i]] == 0 else str(
                self.counter[self.colors[i]])
            label = tkinter.Label(self.window, text=label_text, font=(self.fontFamily, 25), width=3, height=1,
                                  background=self.colors[i], foreground="black", relief="flat")
            label.place(relx=0.125 + (between * i), rely=0.275)
            self.color_label.append(label)
            # Plus button
            plus_button = tkinter.Button(self.window, text="+", font=(self.fontFamily, 10), width=4, height=0,
                                         command=functools.partial(self.plus, index=i))
            plus_button.place(relx=0.16 + (between * i), rely=0.575)
            self.plus_button.append(plus_button)

            # Minus button
            minus_button = tkinter.Button(self.window, text="-", font=(self.fontFamily, 10), width=4, height=0,
                                          command=functools.partial(self.minus, index=i))
            minus_button.place(relx=0.16 + (between * i), rely=0.75)
            self.minus_button.append(minus_button)

    def plus(self, index):
        self.counter[self.colors[index]] += 1
        self.color_label[index].config(text=str(self.counter[self.colors[index]]), font=(self.fontFamily, 25, "bold"))

    def minus(self, index):
        if self.counter[self.colors[index]] > 0:
            self.counter[self.colors[index]] -= 1
        self.color_label[index].config(text=str(self.counter[self.colors[index]]), font=(self.fontFamily, 25, "bold"))
