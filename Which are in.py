def in_array(array1, array2):
    r = []
    duplicates = []
    stroka = ''.join(array2)
    for i in array1:
        if i in stroka:
            if i not in r:
                r.append(i)
    r.sort()

    return r


a1 = ["live", "arp", "strong", "stron"]
a2 = ["lively", "alive", "harp", "alive", "aliveds", "sharp", "armstrong"]
# r = ['arp', 'live', 'strong']
print(in_array(a1, a2))


a1 = ["arp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#r = ['arp']
print(in_array(a1, a2))