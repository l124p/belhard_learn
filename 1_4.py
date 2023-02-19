# Подсчёт положительных и отрицательных чисел.

first_number = input('Enter first number: ')
second_number = input('Enter second number: ')
third_number = input('Enter third number: ')

sum_negative_number = first_number.count('-')
sum_positive_number = 3 - sum_negative_number

print(f"Number of positive numbers: {sum_positive_number} \nNumber of negative numbers: {sum_negative_number}")
