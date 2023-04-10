# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!

arr = [
  [4,6,2,1,9,63,-134,566],
  [-52, 56, 30, 29, -54, 0, -110],
  [42, 54, 65, 87, 0],
  [5]
]

def minimum(arr):
  print ("МИНИМАЛЬНЫЕ ЗНАЧЕНИЯ")
  for sorted_list in arr:
    sorted_list = sorted(sorted_list)
    min_num = sorted_list[0]
    print("Минимальное значение из массива:", sorted_list, min_num)
minimum(arr)

def maximum(arr):
  print ("МАКСИМАЛЬНЫЕ ЗНАЧЕНИЯ")
  for sorted_list in arr:
    sorted_list = sorted(sorted_list)
    max_num = sorted_list[-1]
    print("Максимальное значение из массива:", sorted_list, max_num)
maximum(arr)

# ээх) я там забыл поставтить в задании, что функцию sorted тоже использовать нельзя)
# ну вот если интересно варианты с разными сортировками
# Вариант 1
# сортировка выбором
def minimum(arr):
    min_num = arr[0]
    for i in range(len(arr)):
        if arr[i] < min_num:
            min_num = arr[i]
    return min_num


def maximum(arr):
    max_num = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
    return max_num

print('\nСортировка выбором')
print('min =', minimum([4,6,2,1,9,63,-134,566]))
print('max =', maximum([4,6,2,1,9,63,-134,566]))


# Вариант 2
# используем сортировку пузырьком
def bubblesort(l):
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

# Максимум - это последний элемент отсортированного списка
def maximum(arr):
    return bubblesort(arr)[-1]

 # Минимум - это первый элемент отсортированного списка
def minimum(arr):
    return bubblesort(arr)[0]

print('\nСортировка пузырьком')
print('min =', minimum([4,6,2,1,9,63,-134,566]))
print('max =', maximum([4,6,2,1,9,63,-134,566]))


# Вариант 2
# Быстрая сортировка
def quicksort(arr):
    if len(arr) < 2:
        # базовый случай, массив с 0 или 1 элементом уже отсортирован
        return arr
    else:
        # рекурсивный случай. выберем опорный элемент pivot
        pivot = arr[0]
        # подмассив всех элементов, меньших, чем опорный элемент pivot
        less = [i for i in arr[1:] if i <= pivot]
        # подмассив всех элементов, превышающих опорный элемент pivot
        greater = [i for i in arr[1:] if i > pivot]
        # обединяем в порядке "сортировка для меньшего подмассива – опорный элемент – сортировка для большего подмассив"
        return quicksort(less) + [pivot] + quicksort(greater)

# Максимум - это последний элемент отсортированного списка
def maximum(arr):
    return quicksort(arr)[-1]

 # Минимум - это первый элемент отсортированного списка
def minimum(arr):
    return quicksort(arr)[0]
print('\nБыстрая сортировка')
print('min =', minimum([4,6,2,1,9,63,-134,566]))
print('max =', maximum([4,6,2,1,9,63,-134,566]))

