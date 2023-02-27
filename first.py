#
# class Rectangle:
#
#    def __init__(self, x1, y1, x2, y2):
#         self.width = abs(x1 - x2)
#         self.height = abs(y1 - y2)
#
#
#     def perimetr(self):
#         return (self.width + self.height) * 2
#     def square(self):
#         return self.width * self.height
#
# ob = Rectangle(1, 1, 4, 4)
# print(ob.perimetr())
# print(ob.square())

class Category:
    categories = ['A', 'B', 'C', 'CE', 'D', 'DE']

    @classmethod
    def add(cls,names_category):
        if names_category not in cls.categories:
            cls.categories.append(names_category)
            return cls.categories.index(names_category)
        else:
            raise ValueError('category is not uniqui')

    @classmethod
    def get(cls,index_category):
        try:
            return cls.categories[index_category]
        except:
            raise IndexError('error index')

    @classmethod
    def delete(cls, index_category):
        try:
            cls.categories.remove(index_category)
        except:
            return None

    @classmethod
    def update(cls, index_category, names_category):
        if names_category not in cls.categories:
            cls.categories[index_category] = names_category
        elif:
            return cls.add(names_category)
        else:
            raise ValueError('category is not uniqui')


print(Category.get(1))
