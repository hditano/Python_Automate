import os
from datetime import datetime
from MyData import * 

USER = os.getlogin()
TIME = datetime.now().strftime("%H:%M:%S")

def InitApp():
    print(f'Time: {TIME}'.ljust(0) + f'User: {USER}'.rjust(60))
    print('*** Welcome to All Around CLI ***'.center(75))
    print('***  Please choose an option  ***'.center(75))
    print('*** --------------------------***'.center(75))
    print('*** 1- DONT USE               ***'.center(75))
    print('*** 2- View Users Profile     ***'.center(75))
    print('*** 3- Add Data               ***'.center(75))
    print('*** 4- Check Database         ***'.center(75))
    print('*** 5- Create Table           ***'.center(75))
    print('***  -- Choose an Option --   ***'.center(75))
    my_input = input()
    
    # Primordial para que el context manager funcione correctamente
    with MyData():
    
        match my_input:
            case '1':
                p1 = MyData()
                p1.create_connection()
            case '2':
                os.system('cls')
                p2 = MyData()
                p2.users_profile()
            case '3':
                p3 = MyData()
                p3.insert_data()
            case '4':
                p4 = MyData()
                p4.fetch_data()
            case '5':
                p5 = MyData()
                p5.create_table() 


if __name__ == "__main__":
    InitApp()
