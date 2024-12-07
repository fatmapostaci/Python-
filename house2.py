name = input("What is your name?  ")

match name:
    case "Harry" | "Harmonie" | "Ron":
        print("griffindor")
    case "draco":
        print("slytherin")
    case _:
        print("WHO?")
