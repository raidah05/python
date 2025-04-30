class flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def str(self):
        return self.word+'("+self.meaning+")'
    
flash = []

while(True):
    word = input("Enter the word: ")
    meaning = input("Enter the meaning of the word:")

    flash.append(flashcard(word, meaning))
    option = int(input("Enter 0 if you want to add another flashcard and add 1 if you want to stop."))

    if(option):
        break

print("\nyour flashcard")
for i in flash:
    print("<",i)