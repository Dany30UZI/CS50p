def main():
    tac = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    comp(tac)

def comp(s):
    c = 0.0
    while True:
        try:
            item = input("Item: ")
            if item == "":
                break

            item = item.lower()
            res = " " in item
            if res == True:
                first, last = item.split(" ")
                first = first.capitalize()
                last = last.capitalize()
                item = first + " " + last
            else:
                item = item.lower()
                item = item.capitalize()


            for i in s:
                if item == i:
                    c += s[i]
                    print("Total: " + "$" +"%.2f" % c)

        except EOFError:
            break


main()
