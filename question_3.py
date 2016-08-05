def binary(numbers):
    new_list = numbers.split(",")
    filter_list = []

    for x in range(len(new_list)):
        new_list[x] = int(new_list[x], 2)

        if new_list[x]%5 == 0:
            bin(new_list[x])
            new_list[x] = '{0:04b}'.format(new_list[x])
            filter_list.append(new_list[x])

    print filter_list

binary("0111, 1010")

