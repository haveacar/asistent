from audio_input import  Audio
from googletrans import *
class Translate(Audio):


    def __init__(self) -> None:
        super(Translate, self).__init__()
        self.translator = Translator()

    def translate(self):
        # self.result = self.translator.translate(self.text , dest="ru")
        # print(self.result)
        print(self.text)