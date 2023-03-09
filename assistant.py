import sys
from tkinter import *
from PIL import ImageTk, Image
from constans import *
from audio_input import *

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

        # audio input
        self.audio = Audio()



    def start(self)->None:
        '''Start func
        Create labels, place frames, buttons,
        '''

        # grid
        self.top_frame.pack(side=TOP)
        self.central_frame.pack(side=TOP, pady=20)
        self.bottom_frame.pack(side=BOTTOM, pady=20)


        # load voice image
        with Image.open(VOICE_PATH) as img:
            voice_image = ImageTk.PhotoImage(img.resize(size=(30,30)))

        # load voice image
        with Image.open(IMAGE_PATH) as img:
            bg_image = ImageTk.PhotoImage(img.resize(size=(700, 457)))

        # Buttons
        self.btn_voice = Button(master=self.bottom_frame, image=voice_image, command=self.voice_click)
        self.btn_voice.grid(column=0, row=0, sticky='nsew')
        self.entry_text = Entry(master=self.bottom_frame, width=40)
        self.entry_text.grid(column=1, row=0)
        btn_menu = Button(master=self.top_frame, text="Menu")
        btn_menu.pack(side=LEFT)
        self.btn_help= Button(master=self.central_frame, text="How I can help?", font=20, command=self.presentation)
        self.btn_help.pack(side=TOP, pady=20)

        # Labels
        Label(master=self.top_frame, text="AIBO Voice Assistant", font=("Arial", 25, "bold"),
              foreground='gold').pack(side=LEFT)
        voice_img_lbl=Label(master=self.central_frame, image=bg_image)
        voice_img_lbl.pack(side=TOP, before=self.btn_help)



        self.mainloop()

    def presentation(self) -> None:
        """func display greetings labels """

        self.btn_help.config(state='disabled')  # botton disabled

        for next_tex in tuple_greetings:
            btn = Button(master=self.central_frame, text=next_tex, font=20, anchor='center')
            btn.pack(pady=20, side=LEFT)


    def voice_click(self):
        label_recording = Label(master=self.bottom_frame, text="Recording...")
        label_recording.grid(column=2, row=0)
        self.audio.voice_input()
        print("wtssteysty")






