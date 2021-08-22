class AirBall:
    
    def __init__(self, title, price):
        self.title = title
        self.price = price
    
    def __str__(self):
        return self.title
    
    def __setattr__(self, name, value):
        if name == 'title' or name == 'price':
            self.__dict__[name] = value
        else:
            print('Нет такого атрибута')
            raise AttributeError


# Создаем экземпляр класса
instance = AirBall('Шар большой', 150)

# Создаем новый атрибут - цвет (color)
instance.color = 'красный'

# Выводим атрибут color
print(instance.color)