sample = [(1, 2, 40), (0, 15, 60), (10, 80, 0)]
output = []
for i in sample:
    x = [j for j in i ]
    x[2] = 100
    output.append(tuple(x))
print(output)
