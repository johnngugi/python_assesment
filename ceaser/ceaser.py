# Using the Python,
# have the function CaesarCipher(str, num) take the str parameter and perform a Caesar Cipher num on it using the num parameter as the numing number.
# A Caesar Cipher works by numing all letters in the string N places down in the alphabetical order (in this case N will be num).
# Punctuation, spaces, and capitalization should remain intact.

# For example if the string is "Caesar Cipher" and num is 2 the output should be "Ecguct Ekrjgt".

# more on cipher visit http://practicalcryptography.com/ciphers/caesar-cipher/
# happy coding :-)


def CaesarCipher(string, num):
    # Your code goes here
    lists = list(string)
    empty = []
    number = 0
    for x in range(len(lists)):
        number = ord(string[x]) + num
        if number == 32:
            continue
        else:
            lists[x] = chr(number)
            empty.append(lists[x])

    sentence = ''.join(empty)
    print empty
    print sentence

CaesarCipher("john ngugi", 7)






# print "Cipertext:", CaesarCipher("A Crazy fool Z", 1)
