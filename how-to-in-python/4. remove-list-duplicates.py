list = ["hi", "hello", "hey", "helloooo", "hi", "oo", "hey"]

def noDupes():
    new_list = []
    for item in list:
        if item not in new_list:
            new_list.append(item)
    print(new_list)
noDupes()