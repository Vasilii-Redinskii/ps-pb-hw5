class Person:
    def __init__(self, name, age):
        if Person.check_age(age):
            self.name = name
            self.__age = age
        else:
            raise ValueError
    
    @staticmethod
    def check_age(age):
        return age > 0

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if Person.check_age(age):
            self.__age = age
        else:
            raise ValueError   
    

instance = Person('Василий', 35)

# На этой строке получаем ошибку, потому что сработала проверка в сеттере
instance.age = -9
