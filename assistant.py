import sys
from tkinter import *
from PIL import ImageTk, Image
from constans import *

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
        self.top_frame = Frame(bg='#404040')
        self.left_frame = Frame(bg='#404040')
        self.right_frame = Frame(bg='#404040')
        self.bottom_frame = Frame(bg='#404040')

        # lists
        self.greetings_label_list = []

    def start(self):
        # display frames
        self.top_frame.grid(column=0, row=0)
        self.left_frame.grid(column=0, row=1)
        self.right_frame.grid(column=1, row=1, padx=10, sticky='nsew', rowspan=2, columnspan=2)
        self.bottom_frame.grid(column=0, row=2)

        # load left image
        with Image.open(BG_PATH) as img:
            bg_image = ImageTk.PhotoImage(img)

        # load voice image
        with Image.open(VOICE_PATH) as img:
            voice_image = ImageTk.PhotoImage(img)

        # set up bground image
        background_label = Label(self.left_frame, image=bg_image)
        background_label.pack()

        # Labels
        top_lbl = Label(master=self.top_frame, text="AIBO Voice Assistant", font=("Arial", 25, "bold"),
                        foreground='gold')
        top_lbl.pack(side=LEFT, padx=10)
        lbl_name = Label(master=self.right_frame, text=my_name, font=25, foreground='gold', bg='#404040')
        lbl_name.pack(side=TOP, anchor=N)

        # Buttons
        Button(self.top_frame, padx=1, pady=5, text="MENU").pack(side=LEFT, before=top_lbl)
        Button(self.bottom_frame, image=voice_image).pack(side=RIGHT, padx=20)
        Button(self.bottom_frame, text="TEXT", height=6, width=7).pack(side=RIGHT, padx=20)
        self.btn_what_know = Button(self.right_frame, text='What I know:', command=self.presentation)
        self.btn_what_know.pack(side=TOP, anchor=N)

        self.mainloop()

    def presentation(self) -> None:
        """func display greetings labels """

        self.btn_what_know.config(state='disabled')  # botton disabled

        for next_tex in tuple_greetings:
            btn = Button(master=self.right_frame, text=next_tex, font=20, anchor='center')
            btn.pack(pady=20)
            self.greetings_label_list.append(btn)
