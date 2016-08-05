import string
import random


def password(size=8):
    letters_lower = string.ascii_lowercase[:26]
    letters_upper = string.ascii_uppercase[:25]
    numbers = str(random.randint(0, 9))
    symbols = random.choice('!@#$%^')
    sequence = letters_upper + letters_lower + numbers + symbols
    return ''.join(random.choice(sequence) for x in range(size))

if __name__ == '__main__':
    password()

print password()
