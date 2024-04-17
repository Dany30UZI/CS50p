c = input("File name: ")
c = c.lower()
c = c.strip()
first, last = c.split(".")

match last:
    case "gif":
          print("image/gif")
    case "jpg":
          print("image/jpeg")
    case "jpeg":
          print("image/jpeg ")
    case "png":
          print("image/png")
    case "pdf":
          print("application/pdf")
    case "txt":
          print("text/plain")
    case "zip":
          print("application/zip")
    case "bin":
          print("application/octet-stream")
    case _:
          print("application/octet-stream")

