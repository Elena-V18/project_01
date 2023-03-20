my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Да, ваше решение рабочее, но мы могли бы его улучшить. 
# Например, не вручную посчитать индекс строки, а попробовать найти индекс через метод для строк find и rfind

# Решение с помощью индекции строк

first_song = my_favorite_songs [
    : my_favorite_songs.find(',')
]

last_song = my_favorite_songs [
    my_favorite_songs.rfind('N') :
]

second_song = my_favorite_songs[
     my_favorite_songs.find('S') : 
     my_favorite_songs.find(', A')
]

previous_song = my_favorite_songs [
    my_favorite_songs.rfind('St') : 
    my_favorite_songs.rfind(', N')
    ]

print(first_song, last_song, second_song, previous_song)


# Второй вариант, мы можем воспользоваться методом разделения строк по символам. split.
# Полученный в результате список проиндексируем по песням

# Решение с помощью метода split() и индексации списков
songs = my_favorite_songs.split(', ')

print(songs[0], songs[-1], songs[1], songs[-2])
