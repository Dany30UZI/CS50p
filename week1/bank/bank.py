c = input("Greeting: ")
c = c.strip()
if c == "Hello" or c.startswith("Hello"):
    print("$0")
elif c.startswith("H"):
    print("$20")
else:
    print("$100")
