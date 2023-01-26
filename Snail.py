def snail(original):
    rez = []
    rotated = original
    while len(rotated) > 0:
        for i in range(len(rotated[0])):
            rez.append(rotated[0][i])
        rotated.pop(0)
        rotated = list(map(list, reversed(list(zip(*rotated)))))
    return rez




array = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]