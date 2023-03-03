def pascal(n):
    """
    На вход программе подается число n.
    Программу возвращает указанную строку треугольника Паскаля в виде списка
        """
    a = []
    for i in range(n):
        row = [1] * (i+1)
        for j in range(i+1):
            if j != 0 and j != i:
                row[j] = a[i-1][j-1] + a[i-1][j]
        a.append(row)
    for z in a:
        for x in z:
            print(x, end =' ')

        print()


pascal(4)