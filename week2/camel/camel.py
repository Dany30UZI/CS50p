c = input("camelCase: ")
d = ""
cont = ""

for i in range(0, len(c)):
    if c[i].islower():
        d = d + c[i]
    elif c[i].isupper():
        cont = c[i].lower()
        d = d + f"_{cont}"


print(d)
