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


class Admin(User):
    def __init__(self, first_name, last_name):
        # Initiate Parent Class
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


class Privileges:
    def __init__(self, privileges=['can delete post', 'can ban user', 'can add post']):
        self.privileges = privileges

    def add_priviliges(self, new_privilige, password):
        if password == '123' and new_privilige != '':
            self.privileges.append(new_privilige)
        else:
            print(f'Password or Privilige not added')

    def show_privileges(self):
        print(f'Admin has the following privileges: {self.privileges}')


my_admin = Admin("Hernan", "Di Tano")
my_admin.privileges.show_privileges()
my_admin.privileges.add_priviliges("can modify users", "1")
my_admin.privileges.show_privileges()
