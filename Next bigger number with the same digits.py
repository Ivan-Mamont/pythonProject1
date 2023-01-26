def next_bigger(n):
    chislo = list(map(int, list(str(n))))
    chislo1 = []
    print(chislo)
    min = chislo[-1]
    n = len(chislo)

    # while min < chislo[n-2]:
    #     n -= 1
    #     print(n)
    # chislo1 = chislo[:n-1]
    # chislo1.append(chislo[n])
    # chislo1.append(chislo[n-1])
    # print(chislo1)


    for i in range(len(chislo)-2,-1,-1):
        if chislo[i] < min
        print(chislo[i])



# next_bigger(12)#, 21)
# next_bigger(21)#, -1)
next_bigger(2017)#, 2071)
# next_bigger(414)#, 441)
# next_bigger(144)#, 414