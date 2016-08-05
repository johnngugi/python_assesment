def bin2int(digits):
    numbers = []
    new_digits = digits.split(",")
    for i in range(len(new_digits)):
        x = new_digits[i]
        x = int(x, 2)
        if x % 5 == 0:
            bin(x)
            x = '{0:04b}'.format(x)
            numbers.append(x)
    print numbers
    return numbers
bin2int("0100,0011,1010,1001,1111")