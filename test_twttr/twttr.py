def main():

    print("Output: ", shorten(input("Input: ")))

def shorten(word):
    str = word.upper()
    for s in str:
        if ( s=='A' or s=='E' or s=='I'or s=='O' or s=='U' ):
            str=str.replace(s,'')

    return str


if __name__ == "__main__":
    main()
