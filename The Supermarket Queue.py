def queue_time(customers, n):
    '''
    write a function to calculate the total time required for all the customers to check out!
    input
    customers: an array of positive integers representing the queue. Each integer represents a customer,
    and its value is the amount of time they require to check out.
    n: a positive integer, the number of checkout tills.
    '''
    s = []
    if len(customers) == 0: return 0
    if len(customers) == 1: return customers[0]
    if len(customers) < int(n): return max(customers)
    for i in range(n):
        s.append(customers[i])
        s = sorted(s)
    for z in range(n, len(customers)):
        s[0] += customers[z]
        s = sorted(s)
    resalt = s[n-1]
    print(resalt)
    return resalt












queue_time([], 1) #, 0, "wrong answer for case with an empty queue")
queue_time([5], 1) #, 5, "wrong answer for a single person in the queue")
queue_time([2], 5) #, 2, "wrong answer for a single person in the queue")
queue_time([1, 2, 3, 4, 5], 1) #, 15, "wrong answer for a single till")
queue_time([1, 2, 3, 4, 5], 100) #, 5, "wrong answer for a case with a large number of tills")
queue_time([2, 2, 3, 3, 4, 4], 2) #, 9, "wrong answer for a case with two tills")
