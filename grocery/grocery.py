
def main():

    grocery_dict = {}
    while True:
        try:
            item=get_item()
            if item  in grocery_dict:
                grocery_dict[item] += 1
            else:
                grocery_dict[item] = 1

        except (EOFError , KeyboardInterrupt):
            for item in sorted(grocery_dict):
                print(grocery_dict.get(item),item)
            break

def get_item():
    try:
        item = input().upper()
    except ValueError:
        pass
    return item



main()