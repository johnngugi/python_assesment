def swapie(sentence):
    store = list(sentence)

    for i in range(len(sentence)):
        store[i] = store[i].upper()

    word = ''.join(store)
    return word


print (swapie("Hello world Practice makes perfect"))
