class Item:
   
    def __init__(self, title):
        if Item.check_title(title):
            self.__title = title
        else:
            raise ValueError
    
    @staticmethod
    def check_title(title):
        return title is not ''

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        if Item.check_title(title):
            self.__title = title
        else:
            raise ValueError   


instance = Item('gbr')

# На этой строке получаем ошибку, потому что сработала проверка в сеттере
instance.title = input()


# Создаем продукты с указанием названия, калорийности продукта и его себестоимости
dough_product = Product('Тесто', 200, 20)
tomato_product = Product('Помидор', 100, 50)
cheese_product = Product('Сыр', 100, 120)

# Из продуктов создаем ингредиенты. Для каждого ингредиента указываем продукт, 
# из которого он состоит и вес продукта
dough_ingredient = Ingredient(dough_product, 100)
tomato_ingredient = Ingredient(tomato_product, 100)
cheese_ingredient = Ingredient(cheese_product, 100)

# Из ингредиентов создаем пиццу
pizza_margarita = Pizza('Маргарита', [dough_ingredient, tomato_ingredient, cheese_ingredient])

# Выводим экземпляр пиццы
print(pizza_margarita)