import random


def main():
    v = get_level()
    c = 0
    score = 10
    incorect = 0
    while c < 10:
        x = generate_integer(v)
        y = generate_integer(v)
        try:
            res = x + y
            gue = int(input(f"{x} + {y} = "))
            if res == gue:
                c += 1
            else:
                score -= 1
                while(incorect < 2):
                    print("EEE")
                    gue = int(input(f"{x} + {y} = "))
                    if gue == res:
                        break
                    else:
                        incorect += 1
                if incorect == 2:
                    print("EEE")
                    print(f"{x} + {y} = {res}")

        except ValueError:
            pass

    print(f"Score: {score}")

def get_level():
    c = 0
    while c == 0:
        try:
            level = int(input("Level: "))
            if int(level) > 0 and int(level) < 4:
                c = -1
        except ValueError:
            c = 0
            pass
    return level



def generate_integer(level):
    if level == 1:
        gen = random.randint(0, 9)
        return gen
    elif level == 2:
        gen = random.randint(10, 99)
        return gen
    elif level == 3:
        gen = random.randint(100, 999)
        return gen


if __name__ == "__main__":
    main()
