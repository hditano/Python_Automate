import os
from datetime import datetime

my_data = {"Hernan": 22, "Sebastian": 33}
my_string = 'Hernancito'
USER = os.getlogin()
TIME = datetime.now().strftime("%H:%M:%S")

def InitApp():
    print(f'Time: {TIME}'.ljust(0) + 'User: {USER}'.rjust(60))
    print('*** Welcome to All Around CLI ***'.center(75))
    print('***  Please choose an option  ***'.center(75))
    print(os.getlogin())
    print(my_string.ljust(30), end=' ')

class Init():
    def __init__(self) -> None:
        pass



if __name__ == "__main__":
    InitApp()
