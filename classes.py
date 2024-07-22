class Cookie:  # this is here the class is created
    def __init__(self, color):  # the constructor
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


coockie1 = Cookie('red')  # the object of the class is created here
coockie2 = Cookie('green')

print('Color of cookie 1 is', coockie1.get_color())
print('Color of cookie 2 is', coockie2.get_color())

coockie1.set_color('yellow')  # the method of the class is used

print('Color of cookie 1 is', coockie1.get_color())
print('Color of cookie 2 is', coockie2.get_color())
