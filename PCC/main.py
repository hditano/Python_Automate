class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'My name is: {self.name}')

    def roll_over(self):
        print(f'{self.name} rolled over')


my_dog = Dog("Hernan", 6)
print(f'My dog name is: {my_dog.name}')
my_dog.sit()


class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.name} | {self.cuisine_type}')


my_restaurant = Restaurant("Luna y Misterio", "Parrilla")
my_restaurant1 = Restaurant("El Loco", "Pasta")
my_restaurant2 = Restaurant("Saraza", "Chocha")
my_restaurant.describe_restaurant()
my_restaurant1.describe_restaurant()
my_restaurant2.describe_restaurant()


class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f'{self.first_name} {self.last_name}')

    def greet_user(self):
        print(f'Hello {self.first_name}!!')


my_user = User("Hernan", "Di Tano")
my_user.describe_user()
my_user.greet_user()