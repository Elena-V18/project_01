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


