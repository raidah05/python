class myclass:
    __privatevar =27

    def privatemeth(self):
        print("I am inside myclass ")
    def hello(self):
        print("private variable is", myclass.__privatevar)

foo = myclass()
foo.hello()
foo.privatemeth()