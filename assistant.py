import sys
from tkinter import *
from PIL import ImageTk, Image
from constans import *
import speech_recognition as sr
from response import *
from tkinter import messagebox
import math

if __name__ == '__main__':
    sys.exit()


class Assistant(Tk):
    """ Main class Assistant"""

    def __init__(self):
        super().__init__()

        # screen set up
        self.title("AIBO Voice Assistant")
        self.geometry("1100x768")
        self.config(bg='#404040')
        self.minsize(1000, 750)

        # frames
        self.top_frame = Frame(bg='#404040', width=1100, height=150)
        self.central_frame = Frame(bg='#404040')
        self.bottom_frame = Frame(bg='#404040', width=1100, height=150)

        # lists
        self.greetings_label_list = []

        # init class response
        self.responses = Response()

    def validate(self, new_value) -> str | int:
        """
        validation function int
        :param new_value: string Entry()
        :return: "" or int
        """
        return new_value == "" or new_value.isnumeric()

    def start(self) -> None:
        """Start func
        Create labels, place frames, buttons,
        """
        # grid
        self.top_frame.pack(side=TOP)
        self.central_frame.pack(side=TOP, pady=20)
        self.bottom_frame.pack(side=BOTTOM, pady=20)

        # load voice image
        with Image.open(VOICE_PATH) as img:
            voice_image = ImageTk.PhotoImage(img.resize(size=(30, 30)))

        # load voice image
        with Image.open(IMAGE_PATH) as img:
            bg_image = ImageTk.PhotoImage(img.resize(size=(552, 365)))

        # Buttons
        self.btn_voice = Button(master=self.bottom_frame, image=voice_image, command=self.voice_input,
                                highlightbackground='#404040')
        self.btn_voice.grid(column=0, row=0, sticky='nsew')
        self.entry_text = Entry(master=self.bottom_frame, width=40, highlightbackground='#404040')
        self.entry_text.grid(column=1, row=0)
        btn_menu = Button(master=self.top_frame, text="Menu", highlightbackground='#404040')
        btn_menu.pack(side=LEFT)
        self.btn_help = Button(master=self.central_frame, text="How I can help?", font=20, command=self.presentation,
                               highlightbackground='#404040')
        self.btn_help.pack(side=TOP, pady=20)

        # Labels
        Label(master=self.top_frame, text="AIBO Voice Assistant", font=("Arial", 25, "bold"),
              foreground='gold', background='#404040').pack(side=LEFT)
        voice_img_lbl = Label(master=self.central_frame, image=bg_image)
        voice_img_lbl.pack(side=TOP, before=self.btn_help)
        self.voice_say_lbl = Label(master=self.central_frame, text=" ", foreground='gold', font=("Comic Sans MS", 20),
                                   background='#404040')
        self.voice_say_lbl.pack(side=TOP, before=self.btn_help, pady=5)

        self.response_lbl = Label(master=self.central_frame, text=" ", foreground='gold', font=("Comic Sans MS", 25),
                                  background='#404040')
        self.response_lbl.pack(side=TOP, after=self.voice_say_lbl, pady=5)

        # Bind event Enter
        self.entry_text.bind("<Return>", self.callback)

        # wiki
        self.response_wiki = []
        self.status = False

        # timer constants
        self.flag = False
        self.timer = None
        self.work_min = 1

        # validation numer
        self.vcmd = (self.register(self.validate), '%P')

        self.mainloop()

    def presentation(self) -> None:
        """func display greetings labels """

        self.btn_help.config(state='disabled')  # botton disabled

        for next_tex in tuple_greetings:
            btn = Button(master=self.central_frame, text=next_tex, font=20, anchor='center',
                         highlightbackground='#404040')
            btn.pack(pady=5, side=LEFT)

    def voice_input(self) -> None:
        """
        voice input function from microphone
        """
        # create a recognizer object
        r = sr.Recognizer()

        # set the timeout to 1 seconds
        r.pause_threshold = 1

        # capture audio from the default microphone
        with sr.Microphone() as source:
            print("Say something!")
            self.voice_say_lbl.config(text="Say something!")
            audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            result = r.recognize_google(audio, show_all=True)

        except sr.UnknownValueError:
            self.voice_say_lbl.config(text="Google Speech Recognition could not understand audio")
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            self.voice_say_lbl.config(
                text="Could not request results from Google Speech Recognition service; {0}".format(e))
        else:
            if len(result) != 0:
                text = result.get('alternative')[0].get('transcript')
                self.voice_say_lbl.config(text=text.title())
                print(text)
                self.user_request(text)

    def callback(self, e) -> None:
        """
        CallBack func get str from Entry()
        :param e: e.widget
        """
        text = self.entry_text.get()
        print(text)
        self.user_request(text)

    def create_window_wiki(self) -> None:
        """
        func create wikipedia window
        """
        self.btns_list = []

        def push_bt(title: str) -> None:
            """
            Func push button, destroy Buttons, text insert from wiki
            :param title: str tittle
            """

            for b in self.btns_list: b.destroy()  # destroy tittle Buttons
            wiki_text = self.responses.wiki_text_answer(title)
            text_w.insert(1.0, wiki_text)

        def create_bt(titles_search: list) -> None:
            """
            create buttons function and Label
            :param titles_search: list(titles wiki_answer)
            """
            if self.status:
                for b in self.btns_list: b.destroy()  # destroy tittle Buttons

            self.status = True
            if len(titles_search) > 0:  # check titles response wikipedia

                new_but0 = Button(master=wiki, text=titles_search[0], command=lambda: push_bt(titles_search[0]))
                new_but1 = Button(master=wiki, text=titles_search[1], command=lambda: push_bt(titles_search[1]))
                new_but2 = Button(master=wiki, text=titles_search[2], command=lambda: push_bt(titles_search[2]))
                new_but3 = Button(master=wiki, text=titles_search[3], command=lambda: push_bt(titles_search[3]))
                new_but4 = Button(master=wiki, text=titles_search[4], command=lambda: push_bt(titles_search[4]))
                new_but5 = Button(master=wiki, text=titles_search[5], command=lambda: push_bt(titles_search[5]))
                new_but6 = Button(master=wiki, text=titles_search[6], command=lambda: push_bt(titles_search[6]))
                new_but7 = Button(master=wiki, text=titles_search[7], command=lambda: push_bt(titles_search[7]))
                new_but8 = Button(master=wiki, text=titles_search[8], command=lambda: push_bt(titles_search[8]))
                new_but9 = Button(master=wiki, text=titles_search[9], command=lambda: push_bt(titles_search[9]))

                self.btns_list = [new_but0, new_but1, new_but2, new_but3, new_but4, new_but5, new_but6, new_but7,
                                  new_but8, new_but9]

                for next_btn in self.btns_list: next_btn.pack()

            else:
                text_w.insert(1.0, "Not Found, sorry! ")

        def wiki_request() -> None:
            """
            Func to get from wikipedia request titles
            """
            res = entry_search.get().title()
            if len(res) != 0:
                try:
                    self.response_wiki = self.responses.wikipedia(res)
                except Exception as Err:
                    messagebox.showerror(f"Ops something wrong:({Err}")

                else:
                    create_bt(self.response_wiki)

        # set up wikipedia window
        wiki = Toplevel()
        wiki.title("Wikipedia desktop")
        wiki.geometry("1000x800+10+100")
        wiki.config(bg='#363535')
        wiki.minsize(100, 800)

        # Label wikipedia
        Label(master=wiki, text="Search in Wikipedia:", font=20,
              foreground='gold', background='#363535').pack(pady=10)

        # input field
        entry_search = Entry(master=wiki, bg="#1E1D1D", fg='yellow')
        entry_search.pack(padx=100)

        # Action
        Button(master=wiki, text='Search', command=wiki_request).pack()

        # Text field
        text_w = Text(master=wiki, width=80, height=100, wrap=WORD, bg="#1E1D1D", fg='yellow', font='ariel', padx=3)
        text_w.pack(pady=20, side=LEFT)

        # found label
        found_l = Label(master=wiki, text="Found Pages:", font=('Ariel', 25), bg='#363535', padx=150, pady=10)
        found_l.pack()

    def create_timer_window(self):
        """Timer Func"""

        # Colors Constants
        RED = "#e7305b"
        GREEN = "#9bdeac"
        YELLOW = "#f7f5dd"
        FONT_NAME = "Courier"

        def set_up() -> None:
            """
            Func set up timer
            """
            entry_get = entry_setup.get()
            if len(entry_get) != 0: self.work_min = int(entry_get)

        def reset_timer() -> None:
            """ Reset timer func"""
            if self.flag:
                button_start.config(state="normal")
                window_timer.after_cancel(self.timer)
                canvas.itemconfig(timer_text, text="00:00")
                my_label_checkmark.config(text="")
                my_label_timer.config(text="Timer", fg=GREEN)

        def start_timer() -> None:
            """Start timer func"""
            self.flag = True
            button_start.config(state="disabled")
            work_sec = self.work_min * 60
            my_label_timer.config(text="Timer work!", fg=RED)
            count_down(work_sec)

        def count_down(count: int) -> None:
            """
            Count func sec
            :param count: int sec
            """

            count_min = math.floor(count / 60)
            count_sec = count % 60
            if count_sec < 10:
                count_sec = f"0{count_sec}"

            canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
            if count > 0:

                self.timer = window_timer.after(1000, count_down, count - 1)
            else:
                messagebox.showinfo("Time !")

        # set up window
        window_timer = Toplevel()
        window_timer.title("Timer")
        window_timer.config(padx=100, pady=50, bg=YELLOW)
        window_timer.resizable(False, False)

        # Labels & Buttons
        my_label_timer = Label(master=window_timer, text="Timer", font=("Algerian", 50), fg=GREEN, bg=YELLOW)
        my_label_timer.grid(column=1, row=0)

        my_label_checkmark = Label(master=window_timer, fg=GREEN, bg=YELLOW, font=("Arial", 20))
        my_label_checkmark.grid(column=1, row=3)

        button_start = Button(master=window_timer, text="Start", highlightthickness=0, command=start_timer,
                              highlightbackground=YELLOW)
        button_start.grid(column=0, row=2)

        button_reset = Button(master=window_timer, text="Reset", highlightthickness=0, command=reset_timer,
                              highlightbackground=YELLOW)
        button_reset.grid(column=2, row=2)

        entry_setup = Entry(master=window_timer, highlightthickness=0, width=5, validate='key',
                            validatecommand=self.vcmd)
        entry_setup.grid(column=1, row=3)

        button_setup = Button(master=window_timer, text="set up", highlightthickness=0, command=set_up,
                              highlightbackground=YELLOW)
        button_setup.grid(column=1, row=4)

        canvas = Canvas(master=window_timer, width=200, height=224, bg=YELLOW, highlightthickness=0)
        tomato_img = PhotoImage(file=TIMER_PATH)
        canvas.create_image(100, 112, image=tomato_img)
        timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
        canvas.grid(column=1, row=1)

        window_timer.mainloop()

    def user_request(self, text: str):
        """
        Func processing user requests
        :param text: str
        :return:
        """
        match text:
            # current time now
            case "what's time now" | "time now":
                response = self.responses.time_now()
                self.response_lbl.config(text=response)

            # current date now
            case "what's the day today" | "date today" | "date now" | "what's the date today" | "day today":
                response = self.responses.day_today()
                self.response_lbl.config(text=response)

            # wikipedia request
            case "search in wikipedia" | "search wikipedia" | "wikipedia" | "wiki":
                self.create_window_wiki()
            # timer
            case "timer" | "turn on timer" | "Set timer" | "set a timer":
                self.create_timer_window()

            case _:
                self.response_lbl.config(text="I don't know this command:(")
                pass
