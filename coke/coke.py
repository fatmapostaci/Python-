target=50
coin=0
amount=0
print("Amount due: ", target)

for i in range(100):
    coin= int(input("insert a coin: "))
    if coin != 10 and coin != 5 and coin != 25:
        print("unaccepted coin:  ")
    else:
        amount = amount+coin
        if(amount >= target):
            print("Change Owed " ,  amount - target)
            amount=0
            break
        else:
            print("Amount due: " , target-amount )

