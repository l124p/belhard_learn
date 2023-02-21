# Словарь из n вложенных словарей с элементами name и email

n = int(input("number of elements: "))
dic_clients = {i: {'name': input("Enter name: "), 'email': input("Enter email: ")} for i in range(n)}
print(dic_clients)
