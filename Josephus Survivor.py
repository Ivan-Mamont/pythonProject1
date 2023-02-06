def josephus(n,k):
    if n == 1:
        voin = 1
    elif n > 1:
        voin = 1 + (josephus(n-1,k) + k - 1) % n
    return voin

def josephus_survivor(n,k):
    import sys
    sys.setrecursionlimit(15000)
    givoi = josephus(n,k)
    print(givoi)
    return givoi



josephus_survivor(1201,1266)#, 4)
#josephus_survivor(11, 19)#, 10)
#josephus_survivor(1, 300)#, 1)
#josephus_survivor(14, 2)#, 13)
#josephus_survivor(100, 1)#, 100)