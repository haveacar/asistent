import sys
from tkinter import *
from PIL import ImageTk, Image
from constans import *
import speech_recognition as sr
from response import *

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

    def create_window_wiki(self)->None:

        btns_list = []

        def push_bt(index):
            pass

        def create_bt(titles_search:list)->None:
            """
            create buttons function and Label
            :param titles_search: list(titles wiki_answer)

            """
            if len(titles_search) > 0:

                for i in range(len(titles_search)):
                    new_but = Button(master=wiki, text=titles_search[i], command=lambda: push_bt(i))
                    new_but.pack()
                    btns_list.append(new_but)

            else:
                text.insert(1.0, "Not Found, sorry! ")


        def wiki_request()->None:
            """
            Func to get from wikipedia request titles
            """
            res = entry_search.get().title()
            response_wiki = self.responses.wikipedia(res)
            print(response_wiki)
            create_bt(response_wiki)

        # set up wikipedia window
        wiki= Toplevel()
        wiki.title("Wikipedia desktop")
        wiki.geometry("1000x800+10+100")
        wiki.config(bg='#363535')
        wiki.minsize(100, 800)

        # Label wikipedia
        Label(master=wiki, text="Search in Wikipedia:", font= 20,
              foreground='gold', background='#363535').pack(pady=10)

        # input field
        entry_search = Entry(master=wiki,bg="#1E1D1D", fg='yellow')
        entry_search.pack(padx=100)

        # Action
        Button(master=wiki, text='Search', command=wiki_request).pack()

        # Text field
        text = Text(master=wiki,width=80, height=100, wrap=WORD, bg="#1E1D1D", fg='yellow', font='ariel', padx=3)
        text.pack(pady=20, side=LEFT)




    def user_request(self, text:str):
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
            case "search in wikipedia" |"search wikipedia"| "wikipedia"| "wiki":
                self.create_window_wiki()


                pass
            case _:
                pass