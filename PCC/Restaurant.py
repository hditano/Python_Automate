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


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        # Initiate parent class arguments
        super().__init__( name, cuisine_type)
        self.flavors = ['Crema del Cielo', 'Chocolate', 'Frutilla', 'Vainilla']

    def display_flavors(self):
        print(f'Flavors are {self.flavors}')


my_restaurant = IceCreamStand("Toledo", "De Todo")
my_restaurant.display_flavors()
