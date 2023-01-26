n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int, (input().split()))))

res = [[0]*n for _ in range(n)]


for i in range(n):
    for j in range(n):
        res[j][n-i-1] = mat[i][j]

for row in res:
    print(*row)
