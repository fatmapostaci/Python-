fruits = {
    "Apple" : "130",
    "Avocado" : "50",
    "Banana" : "110",
    "Cantaloupe" : "50",
    "Kiwifruit" : "90",
    "Pear" : "100",
    "Sweet Cherries" : "100",
    "Grapefruit" : "60",
    "Grapes" : "90"
    }

str = input("Item: ").title()

for s in fruits:
    if s == str:
        print("Calories: ", fruits[s])

