# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = input('Введите трехзначное число: ')
if len(number) == 3:
    first_num = int(number[0])
    second_num = int(number[1])
    third_num = int(number[2])
    print('Сумма данного числа: ', first_num + second_num + third_num)
else:
    print('Некорректное число!')