bottles = 99
def on_the_wall(bottles):
    for bottles in range(99, -1, -1):
        if bottles == 99:
            print(str(bottles) + " bottles of beer on the wall!")
        elif bottles > 1 and bottles < 99:
            print("take one down, pass it around, " + str(bottles) + " bottles of beer on the wall")
        elif bottles == 1:
            print("take one down, pass it around, " + str(bottles) + " last bottle of beer on the wall")
        else:
            print("song over go away")
            return
        
on_the_wall(bottles)