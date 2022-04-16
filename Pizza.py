#Родительский класс Item для проверки не пустого значения
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

#Родительский класс Number для проверки положителных чисел
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
 #Класс Product для продуктов
class Product(Item):

    def __init__(self, title, calorific, cost):
        super().__init__(title)
       #присваеваем класс Number каллорийности и цене для проверки значений 
        if Number(calorific) and Number(cost):
            self.calorific = calorific
            self.cost = cost
        else:
            raise ValueError
              
    # получаем каллорийность продукта определенного веса     
    def get_calorific(self, weight):
        # Обращаемся к атрибутам экземпляра класса через self.
        return weight * self.calorific / 100    

     # получаем стоимость продукта определенного веса   
    def get_cost(self, weight):
        # Обращаемся к атрибутам экземпляра класса через self.
        return weight * self.cost / 100  

# Класс Ingredient для ингредиентов
class Ingredient():
    def __init__(self, product, weight):
        self.product = product
        # присваеваем класс Number каллорийности и цене для проверки значений
        if Number(weight):
            self.weight = weight
        else:
            raise ValueError

 # получаем каллорийность ингредиента  
    def get_calorific(self):
        return self.product.get_calorific(self.weight)

# получаем стоимость интгредиента  
    def get_cost(self):
        return self.product.get_cost(self.weight)

#Класс Pizza для объединения ингредиентов
class Pizza(Item):
    def __init__(self, title, ingredients):
        super().__init__(title)
        self.ingredients=ingredients

# получаем каллорийность пиццы  
    def get_calorific(self):
        total_calorific = 0
        for ingredient in self.ingredients:
            total_calorific += ingredient.get_calorific()
        return total_calorific

# получаем стоимость пиццы
    def get_cost(self):
        total_cost = 0
        for ingredient in self.ingredients:
            total_cost += ingredient.get_cost()
        return total_cost

# получаем суммарную информацию о пицце
    def get_pizza(self):
        pizza = f'{self.title} ({self.get_calorific()} kkal) - {self.get_cost()} руб'
        return pizza

# возвращаем ответ
    def __str__(self):
        return self.get_pizza()

        
# # Создаем продукты с указанием названия, калорийности продукта и его себестоимости
# dough_product = Product('Тесто', 0, 20)
# tomato_product = Product('Помидор', 100, 50)
# cheese_product = Product('Сыр', 100, 120)
# peper_product = Product('Перец', 20, 5)

# # Из продуктов создаем ингредиенты. Для каждого ингредиента указываем продукт, 
# # из которого он состоит и вес продукта
# dough_ingredient = Ingredient(dough_product, 200)
# tomato_ingredient = Ingredient(tomato_product, 100)
# cheese_ingredient = Ingredient(cheese_product, 100)
# peper_ingredient = Ingredient(peper_product, 10)

# # Из ингредиентов создаем пиццу
# pizza_margarita = Pizza('Маргарита', [dough_ingredient, tomato_ingredient, cheese_ingredient, peper_ingredient])

# # Выводим экземпляр пиццы
# print(pizza_margarita)
