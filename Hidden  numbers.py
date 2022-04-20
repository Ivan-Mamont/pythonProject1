
def cubic(q):
    summa = 0
    for w in q:
        summa += int(w)**3
    return summa

def is_sum_of_cubes(s):
    sum_n = 0
    i = 0
    h = []
    while i <= len(s)-2:
        if s[i].isdigit() and s[i+1].isdigit() and s[i+2].isdigit():
            t = cubic(s[i:i+3])
            if t == int(s[i:i+3]):
                sum_n += t
                h.append(t)
            i += 3
        else:
            i += 1
    print(h)
    if sum_n > 0:
        print('{0}, {1}, {2}'.format(h, sum_n, 'Lucky'))
    #  return "n0 n1 sum(n) Lucky"
    print("Unlucky")







is_sum_of_cubes("&z _upon 407298a --- ???ry, ww/100 I thought, 631str*ng and w===y -721&()") #, "407 407 Lucky")
# is_sum_of_cubes("No numbers!") #, "Unlucky")