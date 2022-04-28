def digital_root(n):
    '''
    Given n, take the sum of the digits of n.
    If that value has more than one digit, continue reducing in this way
    until a single-digit number is produced. The input will be a non-negative integer.
    '''
    sum = 0
    for i in str(n):
        sum = sum + int(i)
    if sum // 10 != 0:
        sum = digital_root(sum)

    print('sum = ', sum)
    return sum



digital_root(16) #, 7)
digital_root(942) #, 6)
digital_root(132189) #, 6)
digital_root(493193) #, 2)