def count_bits(n):
    '''
    function that takes an integer as input, and returns the number of bits that are
    equal to one in the binary representation of that number.
    '''

    n = bin(n)
    sum = 0
    for digit in n:
        if digit == '1':
            sum += 1
    print(sum)
    return sum


count_bits(0) #, 0)
count_bits(4) #, 1)
count_bits(7) #, 3)
count_bits(9) #, 2)
count_bits(10) #, 2)