import wikipedia
from wikipedia import WikipediaException
import time
import os, json, requests
import sys
from datetime import datetime
class Response():

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

    def wikipedia(self, text:str)->list:
        """
        func get wikipedia tittles
        :param text: str user input
        :return: list  wikipedia titles
        """
        try:
            return wikipedia.search(text)

        except WikipediaException:
          print("You need something to write")
        except Exception as Err:
           print(f"Something wrong!\nCheck internet connection\n{Err}")

    def wiki_text_answer(self, text:str)->str:
        """
        func to get response wikipedia
        :param text: str request wikipedia
        :return: str response wikidedia
        """
        print(text)
        try:
            response = wikipedia.page(text).content

        except:
            response = f"Not found Page:{text}, try another request"

        return  response


    def currency_convector(self):
        # api key and request url
        API_KEY = "c66xOBOerxjgjCqRfbT3MzvIIqMoDm6e"
        REQUEST_URL = "https://api.apilayer.com/fixer/latest?base=USD"

        def receive_data():
            """
            Receive_data func check
            :return:  dict(collected_rates) or False
            """
            try:
                # receive data
                response_data = requests.get(REQUEST_URL, headers={"UserAgent": "XY", "apikey": API_KEY})
                collected_rates = json.loads(response_data.text)
                if collected_rates.get("success") == True: return collected_rates

            except:
                return False

        pass
# for tests functions !

#responses = Response()
#responses.currency_convector()




