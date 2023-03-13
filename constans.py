import os

tuple_greetings = ('Play favorite Song', 'Check weather in Your City', 'Currency Convertor', 'Search Images', 'Search in Wiki', ' Set Timer',
'Send Mail')

my_name = 'My name is AIBO'


# path images
DIR_PATH = os.path.join(os.path.dirname(__file__), 'img')
VOICE_PATH = os.path.join(DIR_PATH, 'voice2.jpeg')
IMAGE_PATH = os.path.join(DIR_PATH, 'voice bg.jpg')
TIMER_PATH = os.path.join(DIR_PATH, 'tomato.png')
TIMER_PATH = os.path.join(DIR_PATH, 'tomato.png')

commands_list = {
    "commands": {
        "time_now": ["what's time now", "time now"],
        "day_today":["what's the day today","date today","date now", "what's the date today", "day today"],
        "create_window_wiki": ["search in wikipedia", "search wikipedia", "wikipedia", "wiki"],
        "create_timer_window":["timer", "turn on timer", "Set timer", "set a timer"]

    }
}