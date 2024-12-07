str=input("Input: ")
for s in str:
    if (s=='a' or s=='A' or
        s=='e' or s=='E' or
        s=='ı' or s=='I' or
        s=='i' or s=='İ' or
        s=='o' or s=='O' or
        s=='ö' or s=='Ö' or
        s=='u' or s=='U' or
        s=='ü' or s=='Ü' ):
        str=str.replace(s,'')

print("Output: ",str)
