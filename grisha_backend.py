# from audio_input import Audio
# from googletrans import *
from datetime import datetime
from time import *
import pytz


# class Translate(Audio):
#
#     def __init__(self) -> None:
#         super(Translate, self).__init__()
#         self.translator = Translator()
#
#     def translate(self):
#         # self.result = self.translator.translate(self.text , dest="ru")
#         # print(self.result)
#         print(self.text)

class Time:
    # Timer, alarm, stopwatch, time in other region
    def __init__(self) -> None:
        pass

    def stopwatch(self):
        pass

    def alarm(self):
        pass

    def timer(self):
        print("Timer started")
        # Time sleep - get from user
        time_sleep = 3
        sleep(time_sleep)
        print("Timer finished")

    def time(self):
        # Parsing time
        current_date = datetime.now()
        current_time = current_date.time()


class GoogleSearch:

    def __init__(self) -> None:
        pass


class Weather:
    # Check weather in all world(today, tomorrow...)
    # Scraping

    pass


class CurrencyConvertor:
    # To convertor currency
    pass


class WikipediaSearch:
    # Search in wikipedia
    pass


class SendEmail:
    # Send email with voice
    pass

class Calculator:
    """
    Человек говорит - 2 + 2
    У нас есть список команд(умножить, разделить и тд)
    мы проверям какая команда в тексте
    а потом делаем: первый индекс фразы - дейтвие - второй индекс фразы
    """
    pass