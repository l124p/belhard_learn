from csv import DictWriter
from hw_6_3 import *


def export_csv(obj):
    data = []
    res = obj.select()
    for row in res:
        data.append(row.dict())
    with open('output_' + obj.__tablename__ + '.csv', 'w', encoding='utf-8') as file:
        row = DictWriter(file, fieldnames=obj.__table__.columns.keys())
        row.writeheader()
        row.writerows(data)


export_csv(Users)
export_csv(Categories)
export_csv(Products)
