# Вывести четные числа от 2 до N по 5 в строку

n = int(input())

# Вариант 1
number = [i for i in range(2, n + 1) if not i % 2]
for i in range(0, len(number), 5):
    print(*number[i:i + 5])


# Вариант 2
i = 0
for i in range(len(number)):
    if i % 5:
        print(number[i], end=' ')
    else:
        print(number[i])
