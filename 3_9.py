# Вывести имена у кого email отсутствует или не заполнен или ''

def get_name_clients(clients):
    clients_no_email = []
    for i in clients.values():
        if i.get('email') is None or i.get('email') == '':
            clients_no_email.append(i.get('name'))
    return clients_no_email


clients = {'1': {'name': 'Ivan', 'surname': 'Ivanov', 'phone': '269-44-88', 'email': 'ivan@iv.com'},
           '2': {'name': 'Petr', 'surname': 'Petrov', 'phone': '289-44-88', 'email': ''},
           '3': {'name': 'Zina', 'surname': 'Ivanova', 'phone': None, 'email': None},
           '4': {'name': 'Petr', 'surname': 'Petrov', 'phone': '269-44-88', 'email': 'petr@iv.com'},
           '5': {'name': 'Vova', 'surname': 'Vetrov', 'phone': '269-44-88'},
           '6': {'name': 'Mila', 'surname': 'Vetrova', 'phone': '269-44-88', 'email': 'mila@iv.com'}
           }
print(*get_name_clients(clients))
