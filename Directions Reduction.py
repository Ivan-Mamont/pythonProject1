def dirReduc(arr):


    i = 0
    while i < len(arr)-1:
        print(i)
        if len(arr) < 2:
            return arr

        elif arr[i] == "NORTH" and arr[i+1] == "SOUTH" or arr[i] == "SOUTH" and arr[i+1] == "NORTH" or arr[i] == "EAST" and arr[i+1] == "WEST" or arr[i] == "WEST" and arr[i+1] == "EAST":
            arr.pop(i)
            arr.pop(i)
            i = -1
        i += 1
    return arr








a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
dirReduc(a)#, ['WEST'])
u = ["NORTH", "WEST", "SOUTH", "EAST"]
dirReduc(u)#, ["NORTH", "WEST", "SOUTH", "EAST"])