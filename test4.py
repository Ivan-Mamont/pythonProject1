n = 3
# table = [[(int(i * n + i / n + j) % (n * n) + 1) for j in range(n * n)] for i in range(n * n)]
table = []
str = []
for i in range(n * n):
    for j in range(n * n):
        str.append(int(i * n + i / n + j) % (n * n) + 1)
        print(int(i * n + i / n + j) % (n * n))
    table.append([str])
print(table)

