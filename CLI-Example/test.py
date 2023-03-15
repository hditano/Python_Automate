import os
from datetime import datetime

USER = os.getlogin()
TIME = datetime.now().strftime("%H:%M:%S")

ENTRIES = {
    "name": "Hernan",
    "data": {
            1: "Test1",
            2: "Test2",    
        }
    }

def InitApp():
    print(f'Time: {TIME}'.ljust(0) + f'User: {USER}'.rjust(60))
    print('*** Welcome to All Around CLI ***'.center(75))
    print('***  Please choose an option  ***'.center(75))
    print('*** --------------------------***'.center(75))
    print('*** 1- View Entries           ***'.center(75))
    print('*** 2- Add Entries            ***'.center(75))
    print(f'*** -- Choose an Option      ***'.center(75))
    my_input = input()

    if my_input == '1':
        print('You choose one')
        p1 = Init("Hernan")
        p1.view_entries()
    else:
        print('You choose two')



class Init():
    def __init__(self, user) -> None:
        self.user = user
        
    def add_entry(self) -> None:
        pass

    def view_entries(self) -> None:
        os.system('cls')
        print('*** Your entries are ***'.center(75))
        for k, v in ENTRIES.items():
            if v == self.user:
                for item in ENTRIES['data'].values():
                    print(item)
                
       
        
    
        
if __name__ == "__main__":
    InitApp()
