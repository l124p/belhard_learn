# Калькулятор

while True:
    first_num = int(input("Введите первое число: "))
    operator = input("Введите действие: ")
    two_num = int(input("Введите второе число: "))
    if operator == '+':
        rez = first_num + two_num
    elif operator == '-':
        rez = first_num - two_num
    elif operator == '*':
        rez = first_num * two_num
    elif operator == '/' and two_num == 0:
        print("Деление на ноль")
    elif operator == '/':
        rez = first_num / two_num
    else:
        print("некорректный оператор")
    print(f"{first_num} {operator} {two_num} = {rez} ")
    if not (input("Продолжить 'Y': ")) == "Y":
        break
