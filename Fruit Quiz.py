import random
class FruitQuiz:
    def __init__(self):
        self.fruits = {"apple" : "red",
                        "orange" : "orange",
                        "watermelon" : "green",
                        "banana" : "yellow"}
    def quiz(self):
        while True:
            fruit, colour = random.choice(list(self.fruits.items()))
            print("What is the colour of {}".format(fruit))
            user_answer = input()
            if(user_answer.lower() == colour):
                print("Correct answer!")
            else:
                print("Wrong answer!")
            option = int(input("Enter 0 if you want to play again, otherwise enter 1:\n"))
            if (option):
                break
print("WELCOME TO THE FRUIT QUIZ")
fq = FruitQuiz()
fq.quiz()