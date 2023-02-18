# Подсчёт положительных и отрицательных чисел.

a, b, c = map(int, input('Введите три числа через пробел: ').split())
sum_positive_number = 0
sum_negative_number = 0
if a > 0:
    sum_positive_number += 1
else:
    sum_negative_number += 1
if b > 0:
    sum_positive_number += 1
else:
    sum_negative_number += 1
if c > 0:
    sum_positive_number += 1
else:
    sum_negative_number += 1
print(f"Количество положительных чисел: {sum_positive_number} \nКоличество отрицательных чисел: {sum_negative_number}")
