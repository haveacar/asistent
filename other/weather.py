"""
Погода в Москве. Как понять в каком городе мы просим? Итак:
1. Берем создаем список всех возможных городов
2. Проверка текста, есть ли какой то город из списка в нашей фразе
3.Еслм да, парсим погоду по совпаднию города из текстовой фразы
Пример:
l = [Moscow, Jerusalim, Haifa]
req = "Weather in haifa"
for i in req:
if i in l:
    parsing...(i)
"""
from bs4 import BeautifulSoup
import requests

israel_cities = ['Jerusalem',
               'Tel Aviv-Yafo',
               'Haifa',
               'Rishon LeZion',
               'Petah Tikva',
               'Ashdod',
               'Netanya',
               'Beersheba',
               'Holon',
               'Bnei Brak',
               'Ramat Gan',
               'Bat Yam',
               'Rehovot',
               'Herzliya',
               'Kfar Saba',
               'Modiin-Maccabim-Reut',
               'Ashkelon',
               'Hadera',
               'Hod HaSharon',
               'Raanana',
               'Kiryat Ata',
               'Kiryat Bialik',
               'Kiryat Gat',
               'Kiryat Malakhi',
               'Kiryat Motzkin',
               'Kiryat Ono',
               'Kiryat Shmona',
               'Kiryat Tivon',
               'Kiryat Yam',
               'Lod',
               'Nahariya',
               'Nazareth',
               'Nazareth Illit',
               'Nesher',
               'Netivot',
               'Ofakim',
               'Or Akiva',
               'Or Yehuda',
               'Sderot',
               'Tiberias',
               'Tirat Carmel',
               'Yokneam']

url = 'https://www.accuweather.com/en/world-weather'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

print(soup)

# Creating the requests
url = 'https://www.accuweather.com/en/world-weather'
res = requests.get(url)
print("The object type:", type(res))

# Convert the request object to the Beautiful Soup Object
soup = BeautifulSoup(res.text, 'html5lib')
print("The object type:", type(soup))

