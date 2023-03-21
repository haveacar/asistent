import os

tuple_greetings = ('Play favorite Song', 'Check weather in Your City', 'Currency Convertor', 'Search Images', 'Search in Wiki', ' Set Timer',
'Send Mail')

my_name = 'My name is AIBO'

# path images files
DIR_PATH = os.path.join(os.path.dirname(__file__), 'img')
VOICE_PATH = os.path.join(DIR_PATH, 'voice2.jpeg')
IMAGE_PATH = os.path.join(DIR_PATH, 'voice bg.jpg')
TIMER_PATH = os.path.join(DIR_PATH, 'tomato.png')

CURRENT_PATH = os.path.dirname(__file__)
CURRENT_PATCH_JASON = os.path.join(CURRENT_PATH, "static")

# DataBase
HOST = "127.0.0.1"
USER = "postgres"
PASSWORD = "Lenin_1917"
DB_NAME = "users"



# Colors Constants
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


# api key and request url
API_KEY = "c66xOBOerxjgjCqRfbT3MzvIIqMoDm6e"
REQUEST_URL = "https://api.apilayer.com/fixer/latest?base=USD"



commands_list = {

    "commands": {
        "time_now": ["what's time now", "time now"],
        "day_today":["what's the day today","date today","date now", "what's the date today", "day today"],
        "create_window_wiki": ["search in wikipedia", "search wikipedia", "wikipedia", "wiki"],
        'create_timer_window':["timer", "turn on timer", "Set timer", "set a timer"],
        'play_sound':['sound']

    }
}