from abc import ABC , abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I have venom")

class monkey(Animal):
    def move(self):
        print("I can jump")

r = Human()
r.move()

a = Snake()
a.move()

m = monkey()
m.move()