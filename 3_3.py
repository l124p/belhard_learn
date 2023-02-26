# Сдвигаем список на n элементов
def fun(lst_number, n):
    for i in range(n):
        lst_number.insert(0, lst.pop())
    return lst


lst = list(map(int, input('Введите список чисел: ').split()))
n = int(input('Введите число сдвига: '))
print(fun(lst, n))
