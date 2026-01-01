import random

answer_list = ["It is certain", "It is decidedly so", "Without a doubt", "Yes - definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Don't count on it", "My reply is no", "My sources say no", "Outlook no so good", "Very doubtful", "Ask again later", "Reply hazy, try again", "Better not tell you now", "Cannot Predict now", "Concentrate and ask again"]
answer = random.choice(answer_list)

def magic(answer):
    Condition = True
    while(Condition):
        print("Hello, would you like to ask a question? (Y/N)")
        prompt = input()
        while prompt != 'y' and prompt != 'Y' and prompt != 'n' and prompt != 'N':
            print("Please enter Y/N")
            prompt = input()
        if prompt == 'y' or prompt =='Y':
            print("Please enter your question:")
            print("----------------------------")
            question = input("Question: ")
            print(answer)
            while question == "":
                print("Once again, please enter your question:")
                question = input()
            print("---------------------------")
            input("Please press enter.")
        elif prompt == "n" or prompt == "N":
            print("Goodbye!")
            Condition = False 

magic(answer)