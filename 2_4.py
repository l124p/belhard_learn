# Список из n 2 в степени n
n = int(input("Введите степень: "))
number = [2 ** i for i in range(1, n + 1)]
print(*number)
