import wikipedia
from wikipedia import WikipediaException
import time
import  json, requests
from datetime import datetime
from constans import *

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


    def currency_convector(self,f_rates):

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

        def reload_rates() -> dict:
            """
            Func Reload_data checks date from file
            if date!= date.now try upload
            :return: dict (rates)
            """
            rates = {}
            time_now = datetime.now().strftime("%Y-%m-%d")
            # open rates from file
            with open(os.path.join(CURRENT_PATCH_JASON, "data_rates.json")) as f:
                rates_from_file = json.load(f)
            rates = rates_from_file

            # check from file current date
            if rates_from_file.get("date") != time_now:
                print("Uploading Data")
                rates = receive_data()

                # cannot receive data
                if rates == False:
                    print("Cannot update")
                    rates = rates_from_file
                else:
                    print("Uploading successful")
                    # create file
                    with open(os.path.join(CURRENT_PATCH_JASON, "data_rates.json"), "w") as f:
                        json.dump(rates, f, indent=4)
                        pass
            return rates


        all_rates = reload_rates()

        # create dict favorite rates
        dict_favorite_rates = dict.fromkeys(f_rates, 0)

        for next_key in f_rates:
            dict_favorite_rates[next_key] = all_rates.get("rates").get(next_key)

        return dict_favorite_rates




# for tests functions !

#responses = Response()
#responses.currency_convector()




