str = input("camelCase: ")

print("snake_case: ", end="")

for i in range(len(str)):
    if str[i].isupper() ==  True:

        print( "_"+str[i].lower(), end="")
    else:
        print( str[i] , end="")

print("\n")
cd