class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+' ( '+self.meaning+' ) '
flash = []
print("Welcome to flashcard!")
while True:
    word = input("Enter the word you want to add to the flashcard :")
    meaning = input("Also enter the meaning of that word :")
    flash.append(Flashcard(word, meaning))
    option = int(input("Enter 0 if you wnat to add another flashcard otherwise enter 1 :"))
    if (option):
        break
print("\nYour Flashcards :")
for i in flash:
    print(">", i)