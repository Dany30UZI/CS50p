le = []
v = "Adieu, adieu, to"

try:
    while True:
        c = input("Name: ")
        if c == "":
            break
        le.append(c)


    last_product = le[-1]

    if len(le) > 2:
        for i in le[:-1]:
                v += " " + i + ","
                print(f"{v} and {last_product}")
    else:
        print(f"{v} {last_product}")



except EOFError:
    last_product = le[-1]
    if len(le) > 1:
        for i in le[:-1]:
                v += " " + i + ","
                print(f"{v} and {last_product}")
    else:
        print(f"{v} {last_product}")






