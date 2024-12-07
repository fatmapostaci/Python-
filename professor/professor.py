import random
def get_level():
    while True:
        try:
            level = int(input("Level:"))
            if level == 1 or level == 2 or level == 3:
                return level
        except:
            pass

def get_sum():
    while True:
        try:
            sum = int(input())
            return sum
        except:
            pass

def generate_integer(level):
        num1 = random.randint(1, level*10)
        num2 = random.randint(1, level*10)
        print(f"{num1} + {num2} = " , end = "")
        for i in range(10):
            sum = get_sum()
            if sum == num1+num2:
                return 1
            else:
                print("EEE")
                print(f"{num1} + {num2} = " , end = "")

            if i==2:
                print(f"{num1+num2}" , end = "\n")
                return 0

def main():
    true_check = 0
    level = get_level()
    for i in range(10):
        true_check += generate_integer(level)

    print("Score: ", true_check)


if __name__ == "__main__":
    main()

