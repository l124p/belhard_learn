# Вывести четные числа от 2 до N по 5 в строку

n = int(input())
number = [i for i in range(2, n + 1) if not i % 2]

# Вариант 1
print("Вариант 1")
for i in range(0, len(number), 5):
    print(*number[i:i + 5])

# Вариант 2
print("Вариант 2")
i = 0
for i in range(len(number)):
    if (i + 1) % 5:
        print(number[i], end=' ')
    else:
        print(number[i])

# Вариант 3
print("\nВариант 3")
i = 0
j = 1
for i in range(2, (n + 1), 2):
    if j % 5:
        print(i, end=' ')
    else:
        print(i)
    j += 1
