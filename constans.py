import os

tuple_greetings = ('Play favorite Song', 'Check weather in Your City', 'Currency Convertor', 'Search Images', 'Search in Wiki', ' Set Timer',
'Send Mail')

my_name = 'My name is AIBO'


# path images
DIR_PATH = os.path.join(os.path.dirname(__file__), 'img')
VOICE_PATH = os.path.join(DIR_PATH, 'voice2.jpeg')
IMAGE_PATH = os.path.join(DIR_PATH, 'voice bg.jpg')