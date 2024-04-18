def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
        if len(s) > 1 and len(s) < 7:
            return True

main()
