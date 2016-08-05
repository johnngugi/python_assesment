import string
import random


def main(size=10):
    user = raw_input("Do you want to your password to be: (A) Strong (B) Weak [A/B]?\n")

    if user == "A"or user == "a":
        lcase = string.ascii_lowercase[:26]
        ucase = string.ascii_uppercase[:26]
        numbers = string.digits
        symbols = random.choice('%&#$@')
        pwd = lcase + ucase + numbers + symbols
        return ''.join(random.choice(pwd) for p in range(size))

    elif user == "B"or user == "b":
        pwd = ('password', '2016', 'user')
        return random.choice(pwd)
    else:
        return 'Wrong Entry, Retry'


if __name__ == "__main__":
    print main()
