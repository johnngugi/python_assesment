# Write a function that return whether or not the input string has balanced parantheses
# Balanced:
#   '((()))'
#   '(()())'
# Not balanced:
#   '((()'
#   '())('


def paren_matcher(parens):
    opening = 0
    closing = 0

    for x in range(len(parens)):
        if parens[x] == '(':
            opening += 1
        elif parens[x] == ')':
            closing += 1

    if opening == closing:
        print "Balanced"
    else:
        print "Not Balanced"

paren_matcher("(((())))")


