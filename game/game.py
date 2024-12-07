import random
while True:
    try:
        n = int(input("Level: "))
        if n>0:
            break
    except (ValueError,NameError):
        pass

number = int(random.randrange(1,n,1))
while True:

    try:
        guess = int(input("Guess: "))
        if guess>0:

            if guess > number:
                print("Too large!")
            elif guess < number:
                print("Too small!")
            else:
                print("Just right!")
                break

    except (ValueError,NameError):
        pass



