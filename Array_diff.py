
def array_diff(a, b):
    '''
    It should remove all values from list a, which are present in list b keeping their order.
    '''

    for bi in b:
        i = 0
        while i < len(a):
            if a[i] == bi:
                a.remove(a[i])
                i -= 1
            i += 1

    return a


array_diff([1, 2], [1]) #, [2], "a was [1,2], b was [1], expected [2]")
array_diff([1, 2, 2], [1]) #, [2, 2], "a was [1,2,2], b was [1], expected [2,2]")
array_diff([1, 2, 2], [2]) #, [1], "a was [1,2,2], b was [2], expected [1]")
array_diff([1, 2, 2], []) #, [1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]")
array_diff([], [1, 2]), [] #, "a was [], b was [1,2], expected []")
array_diff([1, 2, 3], [1, 2]) #, [3], "a was [1,2,3], b was [1, 2], expected [3]")