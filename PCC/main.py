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
        self.number_served = 0

    def describe_restaurant(self):
        print(f'{self.name} | {self.cuisine_type} | Served: {self.number_served}')

    def set_number_served(self, total_served):
        self.number_served = total_served
        print(f'Current plates served: {self.number_served}')

    def increment_number_served(self, new_served):
        if self.number_served > new_served:
            print('Try again')
        else:
            self.number_served += new_served
            print(f'Total plates served is: {self.number_served}')





my_restaurant = Restaurant("Luna y Misterio", "Parrilla")
my_restaurant.set_number_served(10)
my_restaurant.increment_number_served(30)
my_restaurant1 = Restaurant("El Loco", "Pasta")
my_restaurant2 = Restaurant("Saraza", "Chocha")
my_restaurant.describe_restaurant()
my_restaurant1.describe_restaurant()
my_restaurant2.describe_restaurant()


class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} | Login Attempts: {self.login_attempts}')

    def greet_user(self):
        print(f'Hello {self.first_name}!!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


my_user = User("Hernan", "Di Tano")
my_user.describe_user()
my_user.greet_user()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.describe_user()
my_user.reset_login_attempts()
my_user.describe_user()