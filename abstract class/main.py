from abc import ABC , abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("passed value:",x)
    @abstractmethod
    def task(self):
        print("I am from absclass")

class task_Class(Absclass):
    def task(self):
        print("I am from task_class")

obj = task_Class()
obj.print(100)
obj.task()


