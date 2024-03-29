# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# импортировать случайным образом

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# импортировать случайным образом


import random
import datetime

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

song1, song2, song3 = random.sample(my_favorite_songs, 3)
sum = song1[1] + song2[1] + song3[1]
song = song1[0], song2[0], song3[0]
print('А: Три песни звучат - ', int(sum), 'минут')
print('С/А: Случайные песни -', song)

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

minutes = int(sum)
seconds = int(sum * 100 % 100)
print('D/A: Три песни звучат - ', datetime.time(00, minutes, seconds).strftime('%M:%S'))

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

ran = random.sample(list(my_favorite_songs_dict.items()),3)
sum1 = ran [0][1] + ran [1][1] + ran [2][1]
song1 = ran [0][0], ran [1][0], ran [2][0]
print('B: Три песни звучат - ', int(sum1), 'минут')
print('С/B: Случайные песни -', song1)

minutes1 = int(sum1)
seconds1 = int(sum1 * 100 % 100)
print('D/B: Три песни звучат - ', datetime.time(00, minutes1, seconds1).strftime('%M:%S'))
