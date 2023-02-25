# Развернуть список
def fun_reverse(reverse_lst):
    for i in range(len(reverse_lst)-1):
        reverse_lst.insert(i, reverse_lst.pop())
    return reverse_lst

#lst = [1, 2, 4, 6, 7, 9, 3]
list_numbers = list(map(int, input('Введите список чисел: ').split()))
list_numbers = fun_reverse(list_numbers)
print(list_numbers)
