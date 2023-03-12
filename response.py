import wikipedia
from wikipedia import WikipediaException
import time

class Response:

    """ User response class"""
    def __init__(self):
        pass

    def time_now(self)-> str:
        """
        # Current time now
        :return: time_n
        """
        time_n = time.strftime("%H:%M:%S")
        return time_n

    def day_today(self)->str:
        """
        Current day today
        :return:
        """
        day_n = time.strftime("%D")
        return day_n

    def wikipedia(self, text:str)->str:

        try:
            return wikipedia.search(text)


        except WikipediaException:
          print("You need something to write")


        except Exception as Err:
           print(f"Something wrong!\nCheck internet connection\n{Err}")



# for tests functions !

#responses = Response()
#responses.wikipedia("foto")




