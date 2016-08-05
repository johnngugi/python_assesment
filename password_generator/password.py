def password(size=10):

    user = raw_input("Choose the strength of your password: a) Strong    b) Weak: ")

    if user == "A" or user == 'a':
        letters_lower = string.ascii_lowercase[:26]
        letters_upper = string.ascii_uppercase[:25]
        numbers = str(random.randint(0, 9))
        symbols = random.choice('!@#$%^')
        sequence = letters_upper + letters_lower + numbers + symbols
        return ''.join(random.choice(sequence) for x in range(size))
    elif user == "B" or user == 'b':
        pass1 = ("password", "2016", "new")
        return random.choice(pass1)
    else:
        return "Not a valid choice"

if __name__ == '__main__':
    print password()
