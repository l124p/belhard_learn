# перевод числа из десятичной в двоичную систему исчисления и обратно
def convert_number_binary(i):
    num_to_two = ''
    while i > 0:
        num_to_two += str(i % 2)
        i = i // 2
    num_to_two = num_to_two[::-1]
    return num_to_two


def convert_number_decimal(num):
    num_decimal = 0
    num = num[::-1]
    for i in range(len(num)):
        num_decimal += int(num[i]) * 2 ** i
    return num_decimal


number_decimal = int(input('Введите десятичное число: '))
number_binary = convert_number_binary(number_decimal)
print("Число в двоичном представлении: ", number_binary)

print("Число переводённое обратно в десятичное представление: ", convert_number_decimal(number_binary))
