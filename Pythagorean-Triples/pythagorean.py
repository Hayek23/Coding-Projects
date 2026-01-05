

def equate():
    Condition = True
    while(Condition):
        start  = input("Would you like to find out if a triangle is a pythagorean triple? (Y/N) ")
        if start == "y" or start == "Y":
            a = input("Please enter side a: ")
            b = input("Please enter side b: ")
            c = int(input("Please enter side c: ")) ** 2

            ab = int(a) ** 2 + int(b) ** 2

            if ab == c:
                print(str(ab) + " is equal to " + str(c))
                print("That is a pythagorean triple!")
                input("Please press enter")
            else:
                print(str(ab) + " is not equal to " + str(c))
                print("That is not a pythagorean triple!")
                input("Please press enter")

        elif start == "n" or start == "N":
            Condition = False
        else:
            start = input("Please enter Y/N")

equate()