vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

c = input("Input: ")
d =""
count = 0

for i in range(0, len(c)):
    for j in range(0, len(vowels)):
        count += 1
        if c[i] == vowels[j]:
            count = 0
            break
        elif count == len(vowels) and c[i] != vowels[j]:
            d = d + c[i]
            count = 0


print(d)
