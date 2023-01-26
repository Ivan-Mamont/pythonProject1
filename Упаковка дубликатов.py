stroka = input()
a = stroka.split()
new_stroka = []
new_stroka.append([a[0]])
prom = []
for i in range(1, len(a)):

    if a[i] == a[i-1]:
        new_stroka[-1].append(a[i])
    else:
        new_stroka.append([a[i]])
print(new_stroka)
