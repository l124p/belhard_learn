# Вывод n чисел кратных m и больше k

n = int(input("Введите количество цифр: "))
m = int(input("Введите кратную цифр: "))
k = int(input("Введите число больше какого выводить: "))
count = 0
while n > count:
    k += 1
    if not k % m:
        print(k)
        count += 1
