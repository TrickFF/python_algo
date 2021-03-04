# Создал алгоритм нахождения медианы в неотсортированном массиве размером 2m + 1, где m — натуральное число
# Поиск идет перебором в цикле.
# Показалось интересным, оставлю тут, может кому-то пригодится
import random

l_num = 1
r_num = 100
m = 10
array = [random.randint(l_num, r_num) for _ in range(2 * m + 1)]

print('Исходный массив:')
print(array)
print(f'{"*" * 50}\n')

def mediana(array):
    l = 0 # Количество элементов, которые меньше текущего
    s = 0 # Количество элементов, которые больше текущего
    med = 0 # Медиана
    a = len(array) + 1
    spam = 0

    for i in array:
        for j in array:
            if i > j:
                l += 1
            elif i < j:
                s += 1
            elif i == j and j is not i:
                l += 1
                s += 1
            if l >= len(array) // 2 and s >= len(array) // 2:
                med = i
                break
        if abs(l - s) < a:
            a = abs(l - s)
            spam = i
        l = 0
        s = 0
    if med == 0:
        med = spam
    return med

print(f'Найденная медиана массива: {mediana(array)}\n')

# Выводим отсортированный массив просто для проверки
print(f'Выводим отсортированный массив просто для проверки:\n{sorted(array)}')
test_array = sorted(array)
print(f'Элемент в середине отсортированного массива: {test_array[len(test_array) // 2]}')
