def sorting(words):
    new_list = words.split(",")
    new_list.sort()
    print new_list
    return new_list

sorting("john, alice, george, gladys")
