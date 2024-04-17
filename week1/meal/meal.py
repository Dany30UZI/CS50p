def main():
    c = input("What time is it? ")
    c = convert(c)

    if 7<=c<=8:
        print('breakfast time')
    elif 12<=c<=13:
        print('lunch time')
    elif 18<=c<=19:
        print('breakfast time')


def convert(time):
    first, last = time.split(":")
    z = float(first) + (float(last)/60)
    return(z)


if __name__ == "__main__":
    main()
