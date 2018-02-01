class User:

    def __init__(self, name, age, address1, tel, address2=None):
        self.name = name
        self.age = age
        self.address1 = address1
        self.address2 = address2
        self.tel = tel

    def to_string(self):

        user_str = 'Name: {name}, age: {age}, address1: {address1}, tel: {tel}'.format(name=self.name, age=self.age, address1=self.address1, tel=self.tel)

        return user_str

    def __str__(self):
        user_str = 'Name: {name}, age: {age}, address1: {address1}, tel: {tel}'.format(name=self.name, age=self.age, address1=self.address1, tel=self.tel)

        return user_str


if __name__ == '__main__':
    bjorn = User('Bjorn', 27, address1='Cesta 5a', tel='04624136517383')
    frida = User('Frida', 22, address1='Ulica 7', tel='12345678')
    hans = User('Hans', 33, address1='Ulica 123', tel='1234', address2='Nadomestna ulica 10')
    users = [bjorn, frida, hans]

    for user in users:
        print user
    # print bjorn.name
    # print bjorn.age
    # print bjorn.address1
    # print bjorn.tel
    # print bjorn.to_string()
    # print bjorn
