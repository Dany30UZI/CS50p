d = 50
print(f"Amount Due: {d}")

while d > 0:
    c = input("Insert Coin: ")
    c = int(c)

    match c:
      case 25:
          d = d - c
          if d == 0 or d < 0:
              print(f"Change Owed: {d}")
          else:
              print(f"Amount Due: {d}")
      case 10:
          d = d - c
          if d == 0 or d < 0:
              print(f"Change Owed: {d}")
          else:
              print(f"Amount Due: {d}")
      case 5:
          d = d - c
          if d == 0 or d < 0:
              print(f"Change Owed: {d}")
          else:
              print(f"Amount Due: {d}")
      case _:
            print(f"Amount Due: {d}")



