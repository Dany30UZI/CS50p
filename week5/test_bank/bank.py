def main():
    c = input("Greeting: ")
    c = value(c)
    print(c)


def value(greeting):
    greeting = greeting.strip()
    if greeting == "hello" or greeting.startswith("hello") or greeting.startswith("Hello") or greeting == "Hello":
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
