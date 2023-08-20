# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

len_array = int(input('Введите длину списка =>>>  '))
max_num = int(input('Введите максимальное значение диапазона =>>> '))
min_num = int(input('Введите минимальное значение диапазона =>>> '))
array_numbers = [random.randint(-100, 101) for i in range(len_array)]
array_indexes = []
print('Список чисел ', array_numbers)

for i, item in enumerate(array_numbers, 0): #range(len(array_numbers)):
    if item>= min_num and item <= max_num:
    #if array_numbers[i] >= min_num and array_numbers[i] <=max_num:
        array_indexes.append(i)
print('Список индексов ', array_indexes)
