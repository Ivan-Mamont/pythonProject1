def move_zeros(array):
    """
    Write an algorithm that takes an array and moves all of the zeros to the end,
    preserving the order of the other elements.
    """
    new_array = []
    not_zero = 0
    for i in array:
        if i != 0:
            new_array.append(i)
            not_zero += 1
    for q in range(not_zero, len(array)):
        new_array.append(0)
    print(new_array)
    return new_array



move_zeros(
        [1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
      #,[1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
move_zeros(
        [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])
      #,[9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
move_zeros([0, 0]) #, [0, 0])
move_zeros([0]) #, [0])
move_zeros([]) #, [])