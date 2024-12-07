def main():
    x = int(input("what is x? "))
    if is_even3(x):
        print("this is an even number")
    else:
        print("this is an odd number")


def is_even3(n):
    return (n % 2 == 0)

def is_even2(n):
    return True if n % 2 == 0 else False

def is_even(n):
   if n % 2 == 0:
       return True
   else :
       return False

main()