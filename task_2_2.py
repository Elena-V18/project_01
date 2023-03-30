# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

import datetime
import locale

month = int(input('Введите номер месяц: '))
locale.setlocale(locale.LC_ALL, "ru")
def quarter_of(month):
    if month < 1 or month > 12:
        print('Такого месяца нет!')
    else:
        m = datetime.date(2023, month, 1).strftime('%B')
        if month == 1 or month == 2 or month == 3:
            return f'месяц {m} является частью первого квартала'
        elif month == 4 or month == 5 or month == 6:
            return f'месяц {m} является частью второго квартала'
        elif month == 7 or month == 8 or month == 9:
            return f'месяц {m} является частью третьего квартала'
        elif month == 10 or month == 11 or month == 12:
            return f'месяц {m} является частью четвёртого квартала'
print(quarter_of(month))