import random

def game():
    number = (random.randint(1,100))
    answer = (int(input("Pick a number between 1 and 100: ")))
    print ("you chose:", answer)
    if number == answer:
        print("YOU WIN!")
    else:
        print("WRONG! THE ANSWER WAS", number, "TRY AGAIN!")
        game()

game()