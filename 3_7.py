# Посчитать сумму соседей каждого элемента списка
def sum_item(list_numbers):
    list_summ = []
    for i in range(len(list_numbers)):
        if i == 0:
            list_summ.append(list_numbers[-1] + list_numbers[i+1])
        elif i == len(list_numbers)-1:
            list_summ.append(list_numbers[i-1]+list_numbers[0])
        else:
            list_summ.append(list_numbers[i-1] + list_numbers[i+1])
    return list_summ


#list_numbers = [1, 2, 3, 4, 5, 6, 7, 9]
list_numbers = list(map(int, input('Введите список чисел: ').split()))
print(sum_item(list_numbers))
