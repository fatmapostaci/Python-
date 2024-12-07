import emoji

try:
    prompt = input("Input: ")
    print("Output: ", emoji.emojize(prompt,language='alias'))
except:
    ValueError()