import inflect

p = inflect.engine()

name = []
while True:

    try:
        name.append(input().title())
    except EOFError:
        mylist = p.join(name)
        print("Adieu, adieu, to" , mylist)
        break
