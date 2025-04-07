class bird():
    def __init__(self):
        print("Bird is ready")
    def swim(self):
        print("swim faster")
    def say(self):
        print("Hi")
    def whoisthis(self):
        ("I am bird")

class penguine(bird):
    def __init__(self):
        super().__init__()
        print("Penguine is ready")
    def run(self):
        print("Run faster")
    def whoisthis(self):
        print("I am penguine")

peggy = penguine()
peggy.swim()
peggy.run()
peggy.whoisthis()