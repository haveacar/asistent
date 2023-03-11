
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


# for tests functions !
#responses = Response()




