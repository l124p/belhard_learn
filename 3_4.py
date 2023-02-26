# Фильтруем список оставляя только строки

def filter_lst(new_lst):
    new_list = list(filter(lambda x: isinstance(x, str), new_lst))
    return new_list


lst = ['123123', 3, [2, 4], ['5', '6'], (9, 2, 1), {3, 4}, '2', '44']
lst = filter_lst(lst)
print(lst)
