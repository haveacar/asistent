import sys
from tkinter import *
from PIL import ImageTk, Image
import speech_recognition as sr
from asistent.database import Database
from response import *
from tkinter import messagebox
import math
from tkinter.ttk import Combobox

if __name__ == '__main__':
    sys.exit()


class Assistant(Tk):
    """ Main class Assistant"""

    def __init__(self):
        super().__init__()

        # screen set up
        self.name = None
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
        self.database = Database()

        self.btn_log = Button(self.top_frame,text="LOGIN", command=self.login, highlightbackground='#404040')
        self.btn_account = Button(self.top_frame, text="Account", command=self.account, highlightbackground='#404040')
        self.current_email = ""
        self.current_password = ""

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
        self.btn_log.pack()

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

        # stopwatch constants
        self.flag_w = False

        # currency constants
        self.favorite_rates = ["USD", "UAH", "EUR", "PLN", "RON", "HUF", "ILS"]

        self.mainloop()

    def presentation(self) -> None:
        """func display greetings labels """

        self.btn_help.config(state='disabled')  # button disabled

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

    def create_stopwatch_window(self):
        """stop watch func"""

        start_w = 0
        self.timer_w = None

        def reset_watch() -> None:
            """ Reset stopwatch func"""
            if self.flag_w:
                button_start.config(state="normal")
                stopwatch.after_cancel(self.timer_w)
                canvas.itemconfig(timer_text, text="00:00")
                my_label_checkmark.config(text="")
                my_label_timer.config(text="StopWatch", fg=GREEN)

        def start_watch() -> None:
            """Start watch func"""
            self.flag_w = True
            button_start.config(state="disabled")
            work_sec = start_w * 60
            my_label_timer.config(text="Work!", fg=RED)
            count_up(work_sec)

        def count_up(count: int) -> None:
            """
            Count func sec
            :param count: int sec
            """
            count_min = math.floor(count / 60)
            count_sec = count % 60
            if count_sec < 10:
                count_sec = f"0{count_sec}"

            canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
            if count >= 0:

                self.timer_w = stopwatch.after(1000, count_up, count + 1)
            else:
                print("pause")

        # set up window
        stopwatch = Toplevel()
        stopwatch.title("StopWatch")
        stopwatch.config(padx=100, pady=50, bg=YELLOW)
        stopwatch.resizable(False, False)

        # Labels & Buttons
        my_label_timer = Label(master=stopwatch, text="StopWatch", font=("Algerian", 50), fg=GREEN, bg=YELLOW)
        my_label_timer.grid(column=1, row=0)

        my_label_checkmark = Label(master=stopwatch, fg=GREEN, bg=YELLOW, font=("Arial", 20))
        my_label_checkmark.grid(column=1, row=3)

        button_start = Button(master=stopwatch, text="Start", highlightthickness=0, command=start_watch,
                              highlightbackground=YELLOW)
        button_start.grid(column=0, row=2)

        button_reset = Button(master=stopwatch, text="Reset", highlightthickness=0, command=reset_watch,
                              highlightbackground=YELLOW)
        button_reset.grid(column=2, row=2)

        button_pause = Button(master=stopwatch, text="Pause", highlightthickness=0,
                              highlightbackground=YELLOW)
        button_pause.grid(column=1, row=4)

        canvas = Canvas(master=stopwatch, width=200, height=224, bg=YELLOW, highlightthickness=0)
        tomato_img = PhotoImage(file=TIMER_PATH)
        canvas.create_image(100, 112, image=tomato_img)
        timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
        canvas.grid(column=1, row=1)

        stopwatch.mainloop()

    def login(self):
        """Function for user login/registration"""

        def create_account_window():
            """
            Function for tkinter settings of window to create new account
            """
            self.login_frame.pack_forget()
            self.create_acc_frame.pack()
            self.email_lbl_1.grid(column=1, row=0)
            self.entry_login_new_acc.grid(column=1, row=1)
            self.passw_lbl.grid(column=1, row=2)
            self.entry_password_new_acc.grid(column=1, row=3)
            self.name_lbl.grid(column=1, row=4)
            self.entry_name.grid(column=1, row=5)
            self.btn_create.grid(column=1, row=6,pady=5, ipadx=5, ipady=5)
            self.btn_exit_to_login.grid(column=1, row=7, pady=100, ipadx=2, ipady=2)

        def create_user_data():
            """
            Creating new account for user
            """
            login = self.entry_login_new_acc.get()
            password = self.entry_password_new_acc.get()
            name = self.entry_name.get()

            if len(login) == 0 or len(password) == 0 or len(name) == 0:
                messagebox.showerror(message="One of the fields is empty")
                return

            else:
                self.database.create_account(login, password, name)
                messagebox.showinfo(message="Registration was successful!")
                self.current_email = login
                self.current_password = password
                login_root.destroy()
                self.btn_log.pack_forget()
                self.btn_account.pack()

        def log_in():
            """
            Function for login user: check data from database and compare it with data from user
            """
            login = self.entry_login_log_in.get()
            password = self.entry_password_log_in.get()
            self.database.log_in(login, password)
            if len(login) == 0 or len(password) == 0:
                messagebox.showwarning(title="Error", message="User name or password are empty")
                return

            if len(self.database.return_query_result()) == 0:
                messagebox.showwarning(title = "Error", message = "Incorrect user name or password")

            else:
                print("[INFO] Login to the account was made successfully")
                messagebox.showinfo(message="Login to the account was made successfully! ")

                self.current_email = login
                self.current_password = password

                login_root.destroy()
                self.btn_log.pack_forget()
                self.btn_account.pack()

        def create_restore_passw_root():
            """
            Function for tkinter settings of window to create new password
            """

            self.login_frame.pack_forget()
            self.forgot_password_frame.pack()
            self.email_lbl_2.grid(column=1, row=0, pady=20)
            self.entry_login_3.grid(column=1, row=1)
            self.btn_restore_passw.grid(column=1, row=2, pady=10, ipady=5)
            self.btn_exit_to_login_1.grid(column=1, row=6, pady=100, ipadx=2, ipady=2)

        def new_password_1():
            """
            Function for write exist email and go to step 3(write new password)
            """
            login = self.entry_login_3.get()

            if len(login) == 0:
                messagebox.showwarning(title="Error", message="E-mail is empty")
                return

            if len(self.database.check_exist_account(login)) == 0:
                messagebox.showwarning(title="Error", message="You don't have an account")
                return

            self.forgot_password_frame.pack_forget()
            self.forgot_password_frame_2.pack()
            self.passw_lbl_2.grid(column=1, row=0, pady=10)
            self.new_passw_entry.grid(column=1, row=1)
            self.new_passw_btn.grid(column=1, row=2, pady=20,ipady=4, ipadx=4)
            self.btn_exit_to_forget.grid(column=1, row=3, pady=50,ipady=4, ipadx=4)

        def new_password_2():
            """
            Function for add new password to database
            """
            login = self.entry_login_3.get()
            password = self.new_passw_entry.get()
            if len(password) == 0:
                messagebox.showwarning(title="Error", message="Password is empty")
                return

            self.database.new_password(login, password)

            messagebox.showinfo(message="Password changed!")
            self.current_email = login
            self.current_password = password
            self.btn_log.pack_forget()
            login_root.destroy()
            self.btn_account.pack()

        def exit_to_forget():
            """
            Function for exit to last step in creating password
            """

            self.forgot_password_frame_2.pack_forget()
            self.forgot_password_frame.pack()

        def exit_to_login():
            """
            Function for exit to login_menu
            """
            self.create_acc_frame.pack_forget()
            self.forgot_password_frame.pack_forget()
            self.login_frame.pack()


        # Login setups
        bg = "#FF7F50"
        login_root = Toplevel(bg=bg)
        self.login_frame = Frame(login_root, bg=bg)
        self.login_frame.pack()
        login_root.title("Registration")
        login_root.geometry("450x400")
        login_root.resizable(False, False)

        # labels
        email_lbl = Label(self.login_frame, text="Enter your e-mail", bg=bg)
        passw_lbl = Label(self.login_frame, text="Password", bg=bg)
        self.error_message_lbl = Label(self.login_frame, bg=bg)

        # Buttons
        btn_create_acc = Button(self.login_frame, text="Create account", command=create_account_window, highlightbackground=bg)
        btn_forgot_pass = Button(self.login_frame, text="Forgot a password?", command=create_restore_passw_root, highlightbackground=bg)
        btn_log_in = Button(self.login_frame, text="Log in", highlightbackground=bg, command=log_in)

        # Entry
        self.entry_login_log_in = Entry(self.login_frame)
        self.entry_password_log_in = Entry(self.login_frame, show="*")

        # Grid
        email_lbl.grid(column=1, row=0)
        self.entry_login_log_in.grid(column=1, row=1)
        passw_lbl.grid(column=1, row=2)
        self.entry_password_log_in.grid(column=1, row=3)
        btn_log_in.grid(column=1, row=4)
        btn_forgot_pass.grid(column=1, row=5)
        btn_create_acc.grid(column=1, row=8)

        # Create account setups
        self.create_acc_frame = Frame(login_root, bg=bg)
        self.email_lbl_1 = Label(self.create_acc_frame, text="Enter your e-mail",font=("Arial",15, "bold"), bg=bg)
        self.entry_login_new_acc = Entry(self.create_acc_frame)
        self.passw_lbl = Label(self.create_acc_frame, text="Password", font=("Arial",15, "bold"), bg=bg)
        self.entry_password_new_acc = Entry(self.create_acc_frame)
        self.name_lbl = Label(self.create_acc_frame, text="Enter Your name", font=("Arial",15, "bold"), bg=bg)
        self.entry_name = Entry(self.create_acc_frame)
        self.btn_create = Button(self.create_acc_frame, text="Create account", command=create_user_data, highlightbackground=bg)
        self.btn_exit_to_login = Button(self.create_acc_frame, text="Exit", command=exit_to_login, highlightbackground=bg)

        # Forgot password setups
        self.forgot_password_frame = Frame(login_root, bg=bg)
        self.email_lbl_2 = Label(self.forgot_password_frame, text="Enter your e-mail", bg=bg, font=("Arial", 20, "bold"))
        self.entry_login_3 = Entry(self.forgot_password_frame)
        self.btn_restore_passw = Button(self.forgot_password_frame, text="Continue", highlightbackground=bg, command=new_password_1)
        self.btn_exit_to_login_1 = Button(self.forgot_password_frame, text="Exit", command=exit_to_login, highlightbackground=bg)

        #  Forgot password 2 setups
        self.forgot_password_frame_2 = Frame(login_root, bg=bg)
        self.passw_lbl_2 = Label(self.forgot_password_frame_2, text="Enter new password", bg=bg, font=("Arial", 20, "bold"))
        self.new_passw_entry = Entry(self.forgot_password_frame_2)
        self.new_passw_btn = Button(self.forgot_password_frame_2, text="Create new password", highlightbackground=bg, command=new_password_2)
        self.btn_exit_to_forget = Button(self.forgot_password_frame_2, text="Exit", command=exit_to_forget, highlightbackground=bg)

        login_root.mainloop()

    def account(self):
        """Function for account root with settings and info about user"""

        def log_out():
            """Function for exit from account"""
            self.account_root.destroy()
            self.btn_account.destroy()
            self.btn_log.pack()

        def contact_root():

            self.contact_root = Toplevel(bg="grey")
            self.contact_root.title("Contact us")
            Label(self.contact_root, text="Please write about your problem", font=("Ariel", 12, 'bold'), bg="grey").pack()
            self.message = Text(self.contact_root)
            self.message.pack()
            button_send = Button(self.contact_root,text="Send", font=("Ariel", 12, "bold"), highlightbackground='grey', command=contact)
            button_send.pack(ipadx=2, ipady=2, pady=25)

        def contact():
            """Function for write user message to database"""
            message = self.message.get("1.0", END)
            login = self.current_email
            name = self.nameс

            if len(message) == 0:
                messagebox.showerror(message="Message is empty")
                return

            else:
                self.database.contact(login, name, message)
                messagebox.showinfo(message="Message was send!")
                print("[INFO] Message was send to developers")

                self.contact_root.destroy()

        def about():
            """
            This function for text label with description about developers
            :return:
            """
            about_root = Toplevel(bg="grey")
            about_root.title("About us")
            label_txt = Label(about_root, text=TEXT, font=("Ariel", 12, 'bold'))
            label_txt.pack()

        def change_login():
            old_login = self.current_email
            new_login = self.new_login.get()
            name = self.name

            if len(new_login) == 0:
                messagebox.showerror(title='Error', message="Field is empty")
                return
            if new_login == old_login:
                messagebox.showerror(title='Error', message="Mew login is copy of old login")
                return

            self.database.change_login(old_login, new_login, name)
            messagebox.showinfo(title="INFO", message="Login was changed")
            print("[INFO] Login was changed")

            self.change_login_root.destroy()

        def change_login_root():
            self.change_login_root = Toplevel(bg="grey")
            self.change_login_root.title("Change login")
            Label(self.change_login_root, text="Enter new login", font=("Ariel", 25, "bold"), bg='grey').pack()
            self.new_login = Entry(self.change_login_root)
            self.new_login.pack()
            self.btn_change = Button(self.change_login_root, text="Change login", highlightbackground='grey', command=change_login)
            self.btn_change.pack(ipady=2, ipadx=2)

        def change_passw():
            login = self.current_email
            old_password = self.current_password
            new_password = self.new_login.get()
            name = self.name

            if len(new_password) == 0:
                messagebox.showerror(title='Error', message="Field is empty")
                return
            if new_password == old_password:
                messagebox.showerror(title='Error', message="Mew password is copy of old password")
                return

            self.database.new_password(login, new_password)
            messagebox.showinfo(title="INFO", message="Password was changed")
            print("[INFO] Password was changed")

            self.change_passw_root.destroy()

        def change_password_root():
            self.change_passw_root = Toplevel(bg="grey")
            self.change_passw_root.title("Change password")
            Label(self.change_passw_root, text="Enter new password", font=("Ariel", 25, "bold"), bg='grey').pack()
            self.new_login = Entry(self.change_passw_root)
            self.new_login.pack()
            self.btn_change = Button(self.change_passw_root, text="Change password", highlightbackground='grey',
                                     command=change_passw)
            self.btn_change.pack(ipady=2, ipadx=2)


        # Top level setups
        bg = "#FF7F50"
        self.account_root = Toplevel(bg=bg)
        self.account_frame = Frame(self.account_root, bg=bg)
        self.account_frame.pack()
        self.account_root.title("Your account")
        self.account_root.resizable(False, False)

        # Account setups
        self.name = self.database.select_name(self.current_email)[0].capitalize()
        name_lbl = Label(self.account_frame, text=f"Hello {self.name}!", font=("Ariel", 20, 'bold'),bg=bg, fg="black")
        change_login = Button(self.account_frame, text="Change login", highlightbackground=bg, command=change_login_root)
        change_password = Button(self.account_frame, text="Change password", highlightbackground=bg, command=change_password_root)


        # Menu
        self.account_root.option_add('*tearOff', False)
        root_menubar = Menu(self.account_root)
        self.account_root.config(menu=root_menubar)
        file_menu = Menu(root_menubar)
        # add menu items to file menu
        file_menu.add_command(label='Contact to developer', command=contact_root)
        file_menu.add_command(label='About program', command=about)
        file_menu.add_separator(background='red')
        file_menu.add_command(label='Log out', command=log_out)
        # Add menu items to root menubar
        root_menubar.add_cascade(label='Options', menu=file_menu)

        # Pack
        name_lbl.pack()
        change_login.pack(side=LEFT)
        change_password.pack(side=LEFT)

    def currency(self):
        """Func Currency Converter"""
        # collect actual favorite rates
        dict_favorite_rates, date, all_rates = self.responses.currency_convector(self.favorite_rates)

        # create all rates name list
        all_rates_list = [key for key in all_rates]

        def convector() -> None:
            """Func convertor convert rates"""
            # take user input keys and amount
            user_input_first = first_combo.get()
            user_input_second = second_combo.get()
            amount = first_rate_entry.get()

            if user_input_first != "" or user_input_second != "":
                # converter if choice==USD
                if user_input_first == "USD":
                    result = float(amount) * float(dict_favorite_rates.get(user_input_second))
                    second_rate.config(text=round(result, 2))

                    # converter if choice!=USD
                else:
                    result = float(amount) * float(dict_favorite_rates.get(user_input_second)) / float(
                        dict_favorite_rates.get(user_input_first))
                    second_rate.config(text=round(result, 2))

        def add_rates_favorite():
            """Func get rates and add to favorites, update rates favorite rates dict (k,v)"""

            # get key, value
            user_key = rates_combo.get()
            rate_value = all_rates.get(user_key)

            if user_key != "":
                # update dictionary
                dict_favorite_rates[user_key] = rate_value
                # update favorite rates list
                self.favorite_rates.insert(0, user_key)
                # update combo
                first_combo.config(values=self.favorite_rates)
                second_combo.config(values=self.favorite_rates)

        # set up window
        window_currency = Toplevel()
        window_currency.title("Currency Convector")
        window_currency.geometry("500x400+800+100")
        window_currency.config(bg=YELLOW)
        window_currency.resizable(False, False)

        # Labels
        Label(master=window_currency, text="Currency Converter", font=(FONT_NAME, 30, "bold")).grid(row=0, columnspan=2,
                                                                                                    pady=10)

        currency_l = Label(master=window_currency, text=f"Last update rates: {date}", font=(FONT_NAME, 20,),
                           highlightbackground=YELLOW, bg=YELLOW, fg="black")
        currency_l.grid(row=1, columnspan=2, pady=10)

        first_rate_entry = Entry(master=window_currency, width=10, font=(FONT_NAME, 25, "bold"), bg=YELLOW, fg="black",
                                 validate='key',
                                 validatecommand=self.vcmd)
        first_rate_entry.grid(row=2, column=0, padx=10)

        second_rate = Label(master=window_currency, text="0", font=(FONT_NAME, 25, "bold"), bg=YELLOW, fg="black")
        second_rate.grid(row=3, column=0, padx=10)

        # combox
        first_combo = Combobox(master=window_currency, values=self.favorite_rates)
        first_combo.grid(row=2, column=1, padx=10, pady=2)

        second_combo = Combobox(master=window_currency, values=self.favorite_rates)
        second_combo.grid(row=3, column=1, padx=10, pady=2)

        rates_combo = Combobox(master=window_currency, values=all_rates_list)
        rates_combo.grid(row=5, column=0)

        # buttons
        Button(master=window_currency, text="Add to Favorites", highlightbackground=YELLOW,
               command=add_rates_favorite).grid(row=6, column=0)
        Button(master=window_currency, text="Convert", highlightbackground=YELLOW, height=3, width=5,
               command=convector).grid(row=4, column=1, pady=20)

        window_currency.mainloop()

    def user_request(self, text: str):

        """
        Func processing user requests
        :param text: str
        """

        match text.lower():
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
            case "timer" | "turn on timer" | "Set timer" | "set up timer":
                self.create_timer_window()

            # stopwatch
            case "stopwatch" | "turn on stopwatch" | "Set stopwatch" | "set up stopwatch":
                self.create_stopwatch_window()
            # currency
            case "currency" | "currency convector" | "currency today":
                self.currency()
            case _:
                self.response_lbl.config(text="I don't know this command:(")



