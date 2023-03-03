import itertools

def get_pins(observed):
    cifry = {0:[0, 8], 1:[1,2,4], 2:[1,2,3,5], 3:[2,3,6], 4:[1,4,5,7], 5:[2,4,5,6,8], 6:[3,5,6,9], 7:[4,7,8], 8:[5,7,8,9], 9:[6,8,9]}

    result = []
    result1 = []
    rez = []
    for i in range(len(observed)):
        result.append(cifry[int(observed[i])])

    for q in range(len(result)):
        print('q=', q)
        for w in range(len(result[q])):
            print(w)
            print(result[q][w]+result[q+1][w+1])

            #print(result[q][w])



    print(result)

   # print(list(itertools.product(result)))

    #for j in result:
       # result1.append(cifry[j])
       # print(result1)
   # print(list(itertools.product(result1)))

   # print(result1)






#get_pins('8')
get_pins('12') #["11", "22", "44", "12", "21", "14", "41", "24", "42"]