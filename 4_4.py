class Category:
    list_categories: list  # Состоящий из dict{name: str, is_published: bool}
    list_categories = [{'name': 'A', 'is_published': True}, {'name': 'B', 'is_published': False}]

    @classmethod
    def add(cls, category):
        for i in cls.list_categories:
            if category.get('name') == i.get('name'):
                raise ValueError('category is not unique')
        cls.list_categories.append(category)
        return cls.list_categories.index(category)

    @classmethod
    def get(cls, index_category):
        try:
            return cls.list_categories[index_category]
        except IndexError:
            print('invalid index')
    @classmethod
    def delete(cls, index_category):
        try:
            del cls.list_categories[index_category]
        except IndexError:
            pass

    @classmethod
    def update(cls, index, value):
        flag = False
        if index in range(len(cls.list_categories)):
            for i in cls.list_categories:
                if i.get('name') == value.get('name'):
                    raise ValueError('category is not unique')
            else:
                cls.list_categories[index] = value
                flag = True
        if not flag:
            return cls.add(value)\

    @classmethod
    def make_published(cls, index_category):
        try:
            cls.list_categories[index_category]['is_published'] = True
        except IndexError:
            print('invalid index')

    @classmethod
    def make_unpublished(cls, index_category):
        try:
            cls.list_categories[index_category]['is_published'] = False
        except IndexError:
            print('invalid index')


print('\n------Get------')
print("Категория на позиции 1: ", Category.get(1))
print("Категория на позиции 3: ", Category.get(3))
print('\n------Add------')
print(Category.add({'name': 'E', 'is_published': True}))
print(Category.list_categories)
print('\n------Delete------')
print(Category.delete(3))
print(Category.list_categories)
print('\n------Update------')
print(Category.update(1, {'name': 'D', 'is_published': False}))
print(Category.list_categories)
print('\n------Update------')
Category.make_published(1)
Category.make_unpublished(0)
print(Category.list_categories)
