class INDIA():
    def capital(self):
        print("Delhi is the capital of India")
    def language(self):
        print("Hindi is the most spoken language in india")
    def typr(self):
        print("India is a developing country")
    
class USA():
    def capital(self):
        print("Washington, D.C is the capital of USA")
    def language(self):
        print("ENGLISH is the most spoken language in USA")
    def typr(self):
        print("USA is a developed ountry")

a = INDIA()
b = USA()

for country in (a,b):
    country.capital()
    country.language()
    country.typr()
