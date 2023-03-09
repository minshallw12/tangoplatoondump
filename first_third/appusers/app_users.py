import random

class User:
    how_many_admins = 0
    how_many_users = 0
    posts = []

    def __init__(self, name, email, username, password, admin=False):
        self.__name = name
        self.__email = email
        self.__username = username
        self.__password = password
        User.how_many_users += 1
        self.__account = User.how_many_users
        # account_number = []
        # for i in range(12):
        #     account_number.append(str(random.randint(0,9)))
        #self.__account = ''.join(account_number)
        User.post[name] = []
        self.__balance = 0
        self.admin_status = admin
        if self.admin_status == True:
            User.how_many_admins += 1
    # getters

    def make_post(self,post: str) -> None:
        User.posts[self.name].append({
            "user_post_count": self._post_count,
            "content": post,
            "gid": User.post_count     
        })
        User.post_count  = User.post_count + 1
        self._post_count = self._post_count + 1

    def get_name(self):
        return self.__name
    def get_email(self):
        return self.__email
    def get_username(self):
        return self.__username
    def get_password(self):
        return self.__password
    def get_account(self):
        return self.__account
    def get_balance(self):
        return self.__balance
    def get_admin_status(self):
        return self.admin_status        
    def get_profile(self):
        return f'Name: {self.get_name()}\nEmail: {self.get_email()}\nUsername: {self.get_username()}\nPassword: {self.get_password()}\nAccount: # {self.get_account()}\nBalance: $ {self.get_balance()}\nAdmin: {self.get_admin_status()}\n'
    
    def make_post(self, post):
        User.posts[self.name].append({
            'user_p'
        })

    # setters
    def set_email(self, new_email):
        self.__email = new_email
    def set_username(self, new_username):
        self.__username = new_username
    def set_password(self, new_password):
        self.__password = new_password
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance -= amount        
    def turn_on_admin_status(self):
        self.admin_status = True
    def turn_off_admin_status(self):
        self.admin_status = False


    #users
will = User('Will','minshalltech@gmail.com','minshallw12', '1234', True)
meghan = User("Meghan", 'meglights@gmail.com', 'meglights', 'abcde', True)
isaac = User("Isaac", 'isaac@gmail.com', 'eyesac01', 'bigbrown')
emilee = User("Emilee", 'emilee@gmail.com', 'blueeyes03', 'aweoifn52134')
aiden = User("Aiden", 'aiden@gmail.com', 'gummy_gator12', 'iLoveSnowboarding')
zaynab = User('Zaynab','zaynab@gmail.com','eazydozit', '8q7t34rfqe')
benjamin = User('Benjamin','benjamin@gmail.com','aloofBuddha', 'aopw4t5w')

print(aiden.get_profile())
print(zaynab.get_profile())
print(will.get_profile())
print(User.how_many_admins)
print(User.how_many_users)