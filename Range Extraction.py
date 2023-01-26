def solution(args):
    rez = ''
    i = 0
    j = 0
    while i < (len(args)-1):
        rez += str(args[i]) + ','
        if args[i]+1 == args[i+1]:
            while i < (len(args)-1) and args[i]+1 == args[i+1]:
                j += 1
                i += 1
            if j == 1:
                rez += str(args[i]) + ','
            else:
                rez = rez[0:-1]
                rez += '-' + str(args[i]) + ','
        i += 1
        j = 0
    if i != len(args):
        rez += str(args[-1]) + ','
    return rez[:-1]





solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
                       # '-6,-3-1,3-5,7-11,14,15,17-20')
solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20, 25])
                        # , '-3--1,2,10,15,16,18-20')