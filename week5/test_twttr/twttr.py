def main():
    c = input("Input: ")
    c = shorten(c)
    print(c)


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    d =""
    count = 0

    for i in range(0, len(word)):
        for j in range(0, len(vowels)):
            count += 1
            if word[i] == vowels[j]:
                count = 0
                break
            elif count == len(vowels) and word[i] != vowels[j]:
                d = d + word[i]
                count = 0
    return d

if __name__ == "__main__":
    main()
