import string
import random


def main(size=10):
    lcase = string.ascii_lowercase[:26]
    ucase = string.ascii_uppercase[:26]
    numbers = string.digits
    symbols = random.choice('%&#$@')
    pwd = lcase + ucase + numbers + symbols

    return ''.join(random.choice(pwd) for i in range(size))

if __name__ == "__main__":
    main()
print main()