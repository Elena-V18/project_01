# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no

print('Пункт A:')

def remove_exclamation_marks(s):
    s1 = ''
    for i in s:
        if i != '!':
            s1 += i
    return s1
print("Hi! Hello! ->", remove_exclamation_marks("Hi! Hello"))
print("  ->", remove_exclamation_marks("")) 
print("Oh, no!!! ->", remove_exclamation_marks("Oh, no!!!"))

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

print('Пункт B:')

def remove_last_em(s):
    i = 0
    while i < 1 and s [-1] == "!":
        s = s [:-1]
        i += 1
    return s
print(remove_last_em("Hi!") == "Hi")
print(remove_last_em("Hi!!!") == "Hi!!") 
print(remove_last_em("!Hi") == "!Hi")



# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

print('Пункт C:')

def remove_word_with_one_em(s):
#делим строку на слова
    words = s.split(' ')
# фрагмент по которому удаляем слова
    fragment = 'Hi!'        
# новый список оставшихся слов
    new_words = []
    for word in words:
        if fragment not in word:
            new_words.append(word)
    return new_words
r = ' '.join(remove_word_with_one_em("Hi!"))
print('Hi! ->', r)
r1 = ' '.join(remove_word_with_one_em("Hi! Hi!"))
print('Hi! Hi! ->', r1)
r2 = ' '.join(remove_word_with_one_em("Hi! Hi! Hi!"))
print('Hi! Hi! Hi! ->', r2)
r3 = ' '.join(remove_word_with_one_em("Hi Hi! Hi!"))
print('Hi Hi! Hi! ->', r3)
r4 = ' '.join(remove_word_with_one_em("Hi! !Hi Hi!"))
print('Hi! !Hi Hi! ->', r4)
r5 = ' '.join(remove_word_with_one_em("Hi! Hi!! Hi!"))
print('Hi! Hi!! Hi! ->', r5)
r6 = ' '.join(remove_word_with_one_em("Hi! !Hi! Hi!"))
print('Hi! !Hi! Hi! ->', r6)


# Супер, вот для пункта C покороче
def remove_word_with_one_em(s):
    return ' '.join([w for w in s.split(' ') if w.count('!')!=1])

print(remove_word_with_one_em("Hi! Hi!! Hi!"))

