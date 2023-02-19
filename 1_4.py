# Подсчёт положительных и отрицательных чисел.

first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))
third_num = int(input('Enter third number: '))

col_pos_number = (first_num > 0) + (second_num > 0) + (third_num > 0)
col_neg_number = (first_num < 0) + (second_num < 0) + (third_num < 0)

print(f'Number of positive numbers: {col_pos_number} \nNumber of negative numbers: {col_neg_number}')
