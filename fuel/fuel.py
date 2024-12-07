def try_func():
    while True:
        try:
            str = input("Fraction: " ).split('/')
            division = (int(str[0])/int(str[1]))

            if(division>1):
                raise ValueError()
            else:
                return round(division,2)

        except ValueError:
            pass

        except ZeroDivisionError:
            pass



def main():

    division = int(try_func()*100)

    if(division>=99):
        print("F", end='')
    elif(division<=1):
        print("E", end='')
    else:
        print(division, end = "%")




main()

