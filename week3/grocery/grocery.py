def main():
    shop = add()
    count_items(shop)


def add():
    try:
        shop = []
        while True:
            item = input().strip().upper()
            if not item:
                break
            shop.append(item)
        return shop
    except EOFError:
        return shop


def count_items(shop):
    counts = {}
    for item in shop:
        counts[item] = counts.get(item, 0) + 1

    for item, count in counts.items():
        print(f"{count} {item}")


main()
