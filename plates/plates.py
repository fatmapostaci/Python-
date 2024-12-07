def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

i=0

def is_valid(s):
    k=0
    x=len(s)
    lastchar=s[x-1]

    if s.find('0')>0:
        k=s.find('0')

    if s[0]=='0' or 2>x or x>6 or s.isdigit():
        return bool(0)

    elif s.isalnum()==False:
        return bool(0)

    elif s.isalpha():
        return bool(1)

    elif lastchar.isalpha():
        return bool(0)

    elif  s[k-1].isalpha():
        return bool(0)


    else:
        return bool(1)


main()

