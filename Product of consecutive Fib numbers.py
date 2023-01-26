def productFib(prod):
    f1 = 0
    f2 = 1
    list = []
    while f1 * f2 <= prod:
        if f1 * f2 == prod:
            list.append(f1)
            list.append(f2)
            list.append('True')
            print('qqq',list)
            return list
        f1, f2 = f2, f1+f2
    list.append(f2)
    list.append(f1+f2)
    list.append('Falshe')
    print(list)
    return list


productFib(4895)#, [55, 89, True])
productFib(5895)#, [89, 144, False])