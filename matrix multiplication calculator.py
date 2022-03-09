a = [[1,2,3],
    [4,5,6],
    [7,8,9]]
b = [[1,2,3],
    [4,5,6],
    [7,8,9]]
c = []
for _ in range(3):
    c.append([])
print(c)
for i in range(len(a)):
    for k in range(len(a)):
        sum = 0
        for j in range(len(b[0])):
            sum += a[i][j]*b[j][k]
        c[i].append(sum)
print(c)
