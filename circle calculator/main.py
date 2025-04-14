class circle:
    def __init__(self):
        self.r = int(input("Enter the radius: "))
    def calculate(self):
        area = 3.1416*(self.r**2)
        print("The area is {}".format(area))
        parameter = 2*3.1416*self.r
        print("The parameter is {}".format(parameter))

obj = circle()
obj.calculate()
        