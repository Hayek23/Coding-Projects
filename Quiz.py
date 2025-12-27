quiz = [
    ("What is our anniversary?", "December 30th"),
    ("What is the name of my first dog?", "Sadie"),
    ("What city is this show based in?", "Philadelphia")
]
score = 0
for number, (question, answer) in enumerate(quiz, start=1):
    response = input(f"{number}. {question}")
    if response == answer:
        score += 1
        print("Correct!")
    else:
        print("wrong :(")

if score == 3:
    print(score, "Points. Good Job!")
else:
    print("only", score, "points. I guess you dont love me :(")