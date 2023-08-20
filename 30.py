# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_element = int(input('Введите первый элемент прогрессии =>  '))
difference = int(input('Введите разность =>  '))
len_list = int(input('Введите количество элементов прогрессии =>  '))


def progression(a1, n, d):
    arithmetic_progression = []  # создаем пустой список для элементов арифметической прогрессии
    for i in range(d):
        a_i = a1 + i * n  # находим каждый элемент прогрессии. Единицу не вычитаем, т.к. нумерация с о
        arithmetic_progression.append(a_i)
    return arithmetic_progression


print(progression(first_element,difference,len_list))
