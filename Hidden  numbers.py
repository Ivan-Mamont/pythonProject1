
def cubic(q):
    summa = 0
    for w in q:
        summa += int(w)**3
    return summa


def is_sum_of_cubes(s):
    s = s + '  '
    sum_n = 0
    i = 0
    h = []
    count = 0
    while i <= len(s)-3:
        if s[i].isdigit() and s[i+1].isdigit() and s[i+2].isdigit():
            t = cubic(s[i:i+3])
            if str(t) == int(s[i:i+3]):
                count += 1
                h.append(str(t))
                sum_n += t
            i += 3

        elif s[i].isdigit() and s[i+1].isdigit():
            t = cubic(s[i:i+2])
            if str(t) == int(s[i:i+2]):
                count += 1
                h.append(str(t))
                sum_n += t
            i += 2

        elif s[i].isdigit():
            t = cubic(s[i])
            if str(t) == s[i]:
                count += 1
                h.append(str(t))
                sum_n += t
            i += 1

        else:
            i += 1


    h.append(str(sum_n))
    h.append('Lucky')

    if count > 0:
        return ' '.join(h)
    return "Unlucky"


ddd = is_sum_of_cubes("l125ab o 10 01 10" )
print(ddd)
