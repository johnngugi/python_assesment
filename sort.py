def sorted(words):
    mylist=words.split(",")
    mylist.sort()
    print mylist
    return mylist
sorted("without,hello,bag,world")