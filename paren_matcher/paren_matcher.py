# Write a function that return whether or not the input string has balanced parentheses
# Balanced:
#   '((()))'
#   '(()())'
# Not balanced:
#   '((()'
#   '())('

def counter(word):
    a = word.count('(')
    b = word.count(')')
    if a == b:
        return 'Balanced'
    else:
        return 'Not Balanced'

print counter(' ((())) ')
print counter(' ())( ')
