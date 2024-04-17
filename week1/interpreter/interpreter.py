c = input("Expression: ")

first, sign, last = c.split(" ")

first = int(first)
last = int(last)

match sign:
      case "+":
          print(float(first + last))
      case "-":
          print(float(first - last))
      case "/":
          print(float(first / last))
      case "*":
          print(float(first * last))
