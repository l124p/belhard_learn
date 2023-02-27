class Category:
    categories = ['A', 'B', 'C', 'CE', 'D', 'DE']

    @classmethod
    def add(cls, names_category):
        if names_category not in cls.categories:
            cls.categories.append(names_category)
            return cls.categories.index(names_category)
        else:
            raise ValueError('category is not uniqui')

    @classmethod
    def get(cls, index_category):
        return cls.categories[index_category]

    @classmethod
    def delete(cls, index_category):
        try:
            del cls.categories[index_category]
            # cls.categories.remove(index_category)
        except IndexError:
            pass

    @classmethod
    def update(cls, i, value):
        if i in range(len(cls.categories)):
            if value not in cls.categories:
                cls.categories[i] = value.title()
            else:
                raise ValueError('category is not unique')
        else:
            return cls.add(value)

    def __iter__(self):
       return self
    def __next__(self):
        self.i += 1
        if self.i in range(len(self.categories)):
            return self.categories[self.i]
        else:
            self.i = -1
            raise StopIteration


print(Category.get(0))
print(Category.add('AC'))
print(Category.get(6))
print(Category.delete(6))
Category.update(6, 'AC')
Category.update(5, 'AC')
print(Category.get(6))
print(Category.get(5))
