class computer:
    def __init__(self):
        self.__maxprice = 1000
    
    def sell(self):
        print('selling price is : {}'.format(self.__maxprice))
    def setmaxprice(self , price):
        self.__maxprice = price

c = computer()
c.sell()

c.__maxprice = 1500
c.sell()

c.setmaxprice(2000)
c.sell()
       