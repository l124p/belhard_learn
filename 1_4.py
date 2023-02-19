# Подсчёт положительных и отрицательных чисел.

first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))
third_num = int(input('Enter third number: '))

col_pos_number = ((first_num * first_num)**(1/2) + first_num) / (first_num*2) + \
                      ((second_num * second_num) ** (1/2) + second_num) / (second_num*2) + \
                      ((third_num * third_num) ** (1/2) + third_num) / (third_num*2)
col_neg_number = 3 - col_pos_number

print(f"Number of positive numbers: {round(col_pos_number)} \nNumber of negative numbers: {round(col_neg_number)}")
