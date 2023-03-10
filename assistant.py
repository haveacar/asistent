import sys
from tkinter import *
from PIL import ImageTk, Image
from constans import *
import speech_recognition as sr

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
            bg_image = ImageTk.PhotoImage(img.resize(size=(650, 430)))

        # Buttons
        self.btn_voice = Button(master=self.bottom_frame, image=voice_image, command=self.voice_click,
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
              foreground='gold', highlightbackground='#404040').pack(side=LEFT)
        voice_img_lbl = Label(master=self.central_frame, image=bg_image)
        voice_img_lbl.pack(side=TOP, before=self.btn_help)
        self.voice_say_lbl = Label(master=self.central_frame, text=" ", foreground='gold', font=("Comic Sans MS", 20),
                                   highlightbackground='#404040')
        self.voice_say_lbl.pack(side=TOP, before=self.btn_help, pady=5)

        self.mainloop()

    def presentation(self) -> None:
        """func display greetings labels """

        self.btn_help.config(state='disabled')  # botton disabled

        for next_tex in tuple_greetings:
            btn = Button(master=self.central_frame, text=next_tex, font=20, anchor='center',
                         highlightbackground='#404040')
            btn.pack(pady=20, side=LEFT)

    def voice_input(self):
        """
        voice input function from microphone
        """
        # create a recognizer object
        r = sr.Recognizer()

        # set the timeout to 2 seconds
        r.pause_threshold = 2

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

    def voice_click(self) -> None:
        self.voice_input()
