def valid_solution(board):
    if proverka_strok(board) == False or proverka_strok(list(map(list, zip(*board[::-1])))) == False or proverka_3x3(list(map(list, zip(*board[0:3][::-1])))) == False or proverka_3x3(list(map(list, zip(*board[3:6][::-1])))) == False or proverka_3x3(list(map(list, zip(*board[6:9][::-1])))) == False:
        return False
    else: return True


def proverka_strok(massiv):
    for i in massiv:
        if sum(i) != 45:

            return False

def proverka_3x3(massiv):
    sum1, sum2, sum3 = 0, 0, 0
    for i in range(9):
        if i <3:
            sum1 += sum(massiv[i])
        elif 2<i<6:
            sum2 += sum(massiv[i])
        elif 5<i:
            sum3 += sum(massiv[i])
    if sum1 != 45 or  sum2 != 45 or sum3 != 45:

        return False


# valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
#                                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
#                                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
#                                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
#                                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
#                                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
#                                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
#                                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
#                                    [3, 4, 5, 2, 8, 6, 1, 7, 9]])#, True);

valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                   [6, 7, 2, 1, 9, 0, 3, 4, 9],
                                   [1, 0, 0, 3, 4, 2, 5, 6, 0],
                                   [8, 5, 9, 7, 6, 1, 0, 2, 0],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 0, 1, 5, 3, 7, 2, 1, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 0, 0, 4, 8, 1, 1, 7, 9]])#, False);
#
# valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8]
#                                       , [4, 9, 8, 2, 6, 1, 3, 7, 5]
#                                       , [7, 5, 6, 3, 8, 4, 2, 1, 9]
#                                       , [6, 4, 3, 1, 5, 8, 7, 9, 2]
#                                       , [5, 2, 1, 7, 9, 3, 8, 4, 6]
#                                       , [9, 8, 7, 4, 2, 6, 5, 3, 1]
#                                       , [2, 1, 4, 9, 3, 5, 6, 8, 7]
#                                       , [3, 6, 5, 8, 1, 7, 9, 2, 4]
#                                       , [8, 7, 9, 6, 4, 2, 1, 5, 3]])#, True);
#
# valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8]
#                                       , [4, 9, 8, 2, 6, 1, 3, 7, 5]
#                                       , [7, 5, 6, 3, 8, 4, 2, 1, 9]
#                                       , [6, 4, 3, 1, 5, 8, 7, 9, 2]
#                                       , [5, 2, 1, 7, 9, 3, 8, 4, 6]
#                                       , [9, 8, 7, 4, 2, 6, 5, 3, 1]
#                                       , [2, 1, 4, 9, 3, 5, 6, 8, 7]
#                                       , [3, 6, 5, 8, 1, 7, 9, 2, 4]
#                                       , [8, 7, 9, 6, 4, 2, 1, 3, 5]])#, False);
#
# valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8]
#                                       , [4, 9, 8, 2, 6, 0, 3, 7, 5]
#                                       , [7, 0, 6, 3, 8, 0, 2, 1, 9]
#                                       , [6, 4, 3, 1, 5, 0, 7, 9, 2]
#                                       , [5, 2, 1, 7, 9, 0, 8, 4, 6]
#                                       , [9, 8, 0, 4, 2, 6, 5, 3, 1]
#                                       , [2, 1, 4, 9, 3, 5, 6, 8, 7]
#                                       , [3, 6, 0, 8, 1, 7, 9, 2, 4]
#                                       , [8, 7, 0, 6, 4, 2, 1, 3, 5]])#, False);
#
# valid_solution([[1, 2, 3, 4, 5, 6, 7, 8, 9]
#                                       , [2, 3, 4, 5, 6, 7, 8, 9, 1]
#                                       , [3, 4, 5, 6, 7, 8, 9, 1, 2]
#                                       , [4, 5, 6, 7, 8, 9, 1, 2, 3]
#                                       , [5, 6, 7, 8, 9, 1, 2, 3, 4]
#                                       , [6, 7, 8, 9, 1, 2, 3, 4, 5]
#                                       , [7, 8, 9, 1, 2, 3, 4, 5, 6]
#                                       , [8, 9, 1, 2, 3, 4, 5, 6, 7]
#                                       , [9, 1, 2, 3, 4, 5, 6, 7, 8]])#, False);