# access private


class Human:

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # age: private attribute

    def print_info(self):
        print(self.name, self.__age)


tom = Human('Tom', 18)
tom.print_info()
print(tom.name)
print(tom.age)  # AttributeError: 'Human' object has no attribute 'age'

