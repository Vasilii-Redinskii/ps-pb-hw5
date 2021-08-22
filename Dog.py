class Animal:
    def __init__(self):
        print('Это животное (' + self.__class__.__name__ + ')')
        super().__init__()


class NotBird:
    def __init__(self):
        print('Это не птица (' + self.__class__.__name__ + ')')


class Dog(Animal, NotBird):
    def __init__(self):
        super().__init__()
        print('У собаки 4 лапы (' + self.__class__.__name__ + ')')


dog_instance = Dog()