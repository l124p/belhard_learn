from csv import DictReader
from hw_6_3 import *


def import_csv(obj, file):
    if obj == Users:
        with open(file, 'r', encoding='utf-8') as file:
            reader = DictReader(file, delimiter=',')
            for row in reader:
                try:
                    valid = UserAdd(**row)
                    obj = Users(
                        name=valid.name,
                        email=valid.email
                    )
                    obj.save()
                except ValidationError as e:
                    print(e, row)
                obj.save()
    elif obj == Categories:
        with open(file, 'r', encoding='utf-8') as file:
            reader = DictReader(file, delimiter=',')
            for row in reader:
                try:
                    valid = CategoryAdd(**row)
                    obj = Categories(
                        name=valid.name
                    )
                    obj.save()
                except ValidationError as e:
                    print(e, row)
    elif obj == Products:
        with open(file, 'r', encoding='utf-8') as file:
            reader = DictReader(file, delimiter=',')
            for row in reader:
                try:
                    valid = ProductAdd(**row)
                    obj = Products(
                        title=valid.title,
                        description=valid.description
                    )
                    obj.save()
                except ValidationError as e:
                    print(e, row)

#import_csv(Users, 'user.csv')
#import_csv(Categories, 'cat.csv')
#import_csv(Products, 'output_products.csv')
