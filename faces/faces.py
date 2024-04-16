def main():
    c = input()
    first, last = c.split(" ")
    conv = convert(last)
    print(first + " " + conv)


def convert(s):
    s = s.replace(":)","🙂")
    s = s.replace(":(","🙁")
    return s

main()
