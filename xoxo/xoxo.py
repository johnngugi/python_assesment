# Using Python, have the function xoxo(str) take the str parameter
# being passed and return the string true if there is an equal number of x's and o's,
# because you cannot receive an uneven number of hugs and kisses :-)
# otherwise return the string false. Only these two letters will be entered in the string,
# no punctuation or numbers.
# For example: if str is "xooxxxxooxo" then the output should return false because there are 6 x's and 5 o's.


def Xoxo(word):
    # code goes here
    x = word.count('x')
    o = word.count('o')

    if x == o:
        return True
    else:
        return False

# keep the function call
print Xoxo("have fun..xoxo")
