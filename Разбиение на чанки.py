def chunked(stroka, n):
    a = stroka.split()
    new_stroka = []
    row = []
    for i in range(len(a)):
        row.append(a[i])
        if len(row) == n:
            new_stroka.append(row.copy())
            row.clear()
    print(new_stroka)


s = input()
n = int(input())
chunked(s, n)