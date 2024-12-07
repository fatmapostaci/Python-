from pyfiglet import Figlet
import sys
import random

if len(sys.argv) == 1:
    arg = input("Input: " )
    figlet = Figlet()
    f = figlet.getFonts()
    figlet.setFont(font=random.choice(f))
    print("Output: \n", figlet.renderText(arg))


elif len(sys.argv) == 3:
    try:
        type = sys.argv[1]
        name = sys.argv[2]
        figlet = Figlet(font=name)
    except:
        sys.exit(1)


    if(type == '-f' or type == '--font' ):
        arg = input("Input: " )
        figlet.setFont()
        print("Output: \n", figlet.renderText(arg))
    else:
        sys.exit(1)

else:
    sys.exit(1)

