
def zero(*args): return 0 if len(args) == 0 else args[0]
def one(*args): return 1 if len(args) == 0 else args[0]
def two(*args): return 2 if len(args) == 0 else args[0]
def three(*args): return 3 if len(args) == 0 else args[0]
def four(*args): return 4 if len(args) == 0 else args[0]
def five(*args): return 5 if len(args) == 0 else args[0]
def six(*args): return 6 if len(args) == 0 else args[0]
def seven(*args): return 7 if len(args) == 0 else args[0]
def eight(*args): return 8 if len(args) == 0 else args[0]
def nine(*args): return 9 if len(args) == 0 else args[0]

def plus(*args): return args[0]+args[1]

#def minus(): #your code here
#def times(): #your code here
#def divided_by(): #your code here


print(five())
print(five(1))
#seven(times(five()))#, 35)
print(four(plus(nine()))) #, 13)
#eight(minus(three()))#, 5)
#six(divided_by(two()))#, 3)