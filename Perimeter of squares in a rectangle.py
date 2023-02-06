def fib(n):
    fibo = []
    a, b = 1, 1
    fibo.append(a)
    for i in range(n):
        a, b = b, a+b
        fibo.append(a)
    return fibo

def perimeter(n):
    fibo = sum(fib(n))*4
    print(fibo)
    return fibo


#perimeter(5)#, 80)
#perimeter(7)#, 216)
perimeter(20)#, 114624)
#perimeter(30)#, 14098308)
#perimeter(100)#, 6002082144827584333104)
#perimeter(500)#, 2362425027542282167538999091770205712168371625660854753765546783141099308400948230006358531927265833165504)