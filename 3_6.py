# Сортировка списка: вначале чётные затем нечетные

def my_sort(lst_numbers):
    new_list = sorted(list(filter(lambda x: (not x % 2), lst_numbers)))
    new_list.extend(sorted(list(filter(lambda x: (x % 2), lst_numbers))))
    return new_list


list_numbers = list(map(int, input().split()))
list_numbers = my_sort(list_numbers)
print(list_numbers)
