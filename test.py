class User():
    def __init__(self, user_name, email, password):
        self.user_name = user_name
        self.email = email
        self.password = password

    def email_verification(self):
        if '@' in self.email:
            return True
        else:
            return False


    def user_verification(self):
        if len(self.user_name) < 8:
            return False
        else:
            return True

    def pass_int(self):
        try:
            if int(self.password):
                return False
            else:
                return True
        except ValueError:
            return True


#Создание объекта user c тремя параметрами которые мы передали в конструктор
user = User('sergeieeee','qaaz@mail.com','123654')
print(user.email_verification())
print(user.user_verification())
print(user.pass_int())
user_2 = User('Alex', 'qaaz486mail.ru', '486aa52')
print(user_2.email_verification())
print(user_2.user_verification())
print(user_2.pass_int())