import tkinter
import functools


class TkWindow:
    def __init__(self, window, settings: dict):
        self.overlay_button = None
        self.refresh_button = None
        self.overlay_text_label = None

        hot_keys = settings["hot_keys"]

        # Set value
        self.overlay = False
        self.color_label = []
        self.hot_key_label = []
        self.plus_button = []
        self.minus_button = []
        self.settings = settings
        self.hot_keys = [hot_keys["colors_1+"], hot_keys["colors_2+"], hot_keys["colors_3+"], hot_keys["colors_4+"], ]
        self.font_size = 25
        self.counter = {}
        self.fontFamily = "맑은 고딕"
        self.init()

        # TkInter setting
        self.window = window
        self.window.title("Sycrakea Color Counter - 햄뮤@Inven")
        self.window.configure(background="#353535")
        self.window.resizable(False, False)  # Height, Width

        self.set_overlay(self.overlay)

    # Init counter & label
    def init(self):
        self.counter.clear()
        for c in self.settings["colors"]:
            self.counter[c] = 0
        if len(self.color_label) > 0:
            for i in range(len(self.color_label)):
                self.color_label[i].config(text=self.settings["colors"][i][0].upper(), font=(self.fontFamily, self.font_size))

    def destroy(self):
        self.window.destroy()

    def set_overlay(self, check):
        self.overlay = check
        self.window.overrideredirect(check)
        self.window.lift()
        self.window.wm_attributes("-topmost", check)
        self.window.wm_attributes("-disabled", check)  # Click through
        if check:
            self.window.geometry("300x120-8+18")  # Width X Height + x + y
            self.window.wm_attributes("-transparentcolor", "#353535")
            self.window.wm_attributes("-alpha", self.settings["overlay_alpha"])
            self.build_overlay_color_widget()
        else:
            self.window.geometry("400x200-0+0")  # Width X Height + x + y
            self.window.wm_attributes("-transparentcolor", "#EAEAEA")
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
        w = 300 / (len(self.settings["colors"]) + 1)
        for i in range(len(self.settings["colors"])):
            # Color label
            label_text = str(self.counter[self.settings["colors"][i]])
            label = tkinter.Label(self.window, text=label_text, font=(self.fontFamily, self.font_size, "bold"), width=0, height=0,
                                  background="#353535", foreground=self.settings["colors"][i], relief="flat")
            label.place(x=w * (i + 1), rely=0.175, anchor="center")
            self.color_label.append(label)
            hot_label = tkinter.Label(self.window, text=self.hot_keys[i].upper(), font=(self.fontFamily, 8, "bold"),
                                      width=0,
                                      height=0, background="#353535", foreground=self.settings["colors"][i],
                                      relief="flat")
            hot_label.place(x=w * (i + 1), rely=0.45, anchor="center")
            self.hot_key_label.append(hot_label)
        self.overlay_text_label = tkinter.Label(self.window,
                                                text=self.settings["hot_keys"]["reset"].upper() + "를 눌러 카운터 초기화\n" +
                                                     self.settings["hot_keys"][
                                                         "toggle_overlay"].upper() + "를 눌러 오버레이 종료\n" +
                                                     self.settings["hot_keys"]["exit_program"].upper() + "를 눌러 프로그램 종료",
                                                font=(self.fontFamily, 8, "bold"), width=0, height=0,
                                                background="#353535",
                                                foreground="white", relief="flat")
        self.overlay_text_label.place(relx=0.2, rely=0.55)

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
        for i in range(len(self.settings["colors"])):
            # Color label
            label_text = str(self.counter[self.settings["colors"][i]])
            label = tkinter.Label(self.window, text=label_text, font=(self.fontFamily, self.font_size, "bold"), width=3, height=1,
                                  background=self.settings["colors"][i], foreground=self.settings["font_colors"][i],
                                  relief="flat")
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
        self.counter[self.settings["colors"][index]] += 1
        self.color_label[index].config(text=str(self.counter[self.settings["colors"][index]]),
                                       font=(self.fontFamily, self.font_size, "bold"))

    def minus(self, index):
        if self.counter[self.settings["colors"][index]] > 0:
            self.counter[self.settings["colors"][index]] -= 1
        self.color_label[index].config(text=str(self.counter[self.settings["colors"][index]]),
                                       font=(self.fontFamily, self.font_size, "bold"))
