fruit = [
    {"name": "apple", "cal": "130"},
    {"name": "avocado", "cal": "50"},
    {"name": "sweet cherries", "cal": "100"},
    {"name": "kiwifruit", "cal": "90"},
    {"name": "pear", "cal": "100"},
]

c = input("Item: ")
c = c.lower()

for i in fruit:
    if c == i["name"]:
        print(f"Calories: {i["cal"]}")

