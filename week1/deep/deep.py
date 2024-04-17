c = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
c = c.lower().strip
if c == "42" or c == "forty-two" or c == "forty two":
    print("Yes")
else:
    print("No")
