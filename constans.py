import os

tuple_greetings = ('Play favorite Song', 'Check weather in Your City', 'Currency Convertor', 'Search Images', 'Search in Wiki', ' Set Timer',
'Send Mail', 'It\'s not all, I\'m learn everytime' )

my_name = 'My name is AIBO'


# path images
DIR_PATH = os.path.join(os.path.dirname(__file__), 'img')
BG_PATH = os.path.join(DIR_PATH, 'robot.jpeg')
VOICE_PATH = os.path.join(DIR_PATH, 'voice2.jpeg')
ROBOT_PATH = os.path.join(DIR_PATH, 'robot_bg.jpeg')