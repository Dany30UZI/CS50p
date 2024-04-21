def main():
    s = get_int()
    print(f"{s}%")


def get_int():
        while True:
            try:
                c = input("Fraction: ")
                x, y = c.split("/")
                x = int(x)
                y = int(y)
                if x < y and y < 5 and x < 5:
                    d = int(round((x / y) * 100))
                    return d
                elif x == y:
                     print("F")
                elif x > y:
                    pass
                else:
                     print("E")
            except ValueError:
                pass

main()
