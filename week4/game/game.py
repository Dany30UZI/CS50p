import random

v = 0
c = 0
while c == 0:
    try:
        level = input("Level: ")
        if int(level) > 0:
            c = -1
    except ValueError:
        c = 0
        pass


number = random.randint(1, 100)


while v == 0:
    try:
        z = int(input("Guess: "))
        if z > 0 and z > number:
            print("Too large!")
        elif z > 0 and z < number:
            print("Too small!")
        elif z > 0 and z == number:
            print("Just right!")
            v = -1
    except ValueError:
        v = 0
        pass

