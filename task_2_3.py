# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

number = int(input('Введите число от 0 до 9: '))
sw = ['Zero', 'One','Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
def switch_it_up(number):
    while 9 < number or number < 0:
        return 'Такого числа нет в диапазоне от 0 до 9'
    else:
        return sw [number]
print(switch_it_up(number))

