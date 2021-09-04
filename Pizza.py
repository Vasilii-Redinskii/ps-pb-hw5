class Item:
   
    def __init__(self, title):
        if Item.check_title(title):
            self.__title = title
        else:
            raise ValueError
    
    @staticmethod
    def check_title(title):
        if title:
            return True
        else:
            return False

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        if Item.check_title(title):
            self.__title = title
        else:
            raise ValueError   

class Number:
    def __init__(self, number):
        
        if Number.check_number(number):
            self.__number = number
        else:
            raise ValueError
    
    @staticmethod
    def check_number(number):
        return number > 0

    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, number):
        if Number.check_number(number):
            self.__number = number
        else:
            raise ValueError 
class Product(Item):

    def __init__(self, title, calorific, cost):
        super().__init__(title)
        if Number(calorific) and Number(cost):
            self.calorific = calorific
            self.cost = cost
        else:
            raise ValueError
              
        
    def get_calorific(self, weight):
        # Обращаемся к атрибутам экземпляра класса через self.
        return weight * self.calorific / 100    
    
    def get_cost(self, weight):
        # Обращаемся к атрибутам экземпляра класса через self.
        return weight * self.cost / 100  

class Ingredient():
    def __init__(self, product, weight):
        self.product = product
        if Number(weight):
            self.weight = weight
        else:
            raise ValueError

    def get_calorific(self):
        return self.product.get_calorific(self.weight)

    def get_cost_ingredient(self):
        return self.product.get_cost(self.weight)

class Pizza(Item):
    def __init__(self, title, ingredients):
        super().__init__(title)
        self.ingredients=ingredients

    def __str__(self):
        return self.title

        
# Создаем продукты с указанием названия, калорийности продукта и его себестоимости
dough_product = Product('Тесто', 200, 20)
tomato_product = Product('Помидор', 100, 50)
cheese_product = Product('Сыр', 100, 120)

# Из продуктов создаем ингредиенты. Для каждого ингредиента указываем продукт, 
# из которого он состоит и вес продукта
dough_ingredient = Ingredient(dough_product, 200)
tomato_ingredient = Ingredient(tomato_product, -100)
cheese_ingredient = Ingredient(cheese_product, 100)
print(tomato_ingredient.get_calorific())
# Из ингредиентов создаем пиццу
pizza_margarita = Pizza('Маргарита', [dough_ingredient, tomato_ingredient, cheese_ingredient])

# Выводим экземпляр пиццы
print(pizza_margarita)