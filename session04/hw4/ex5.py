a = [4, 8, 1, 3, 2, 9, 5, 7, 6]
for j in range (len(a)):
    for i in range (len(a)-1):
        if a[i] > a[i+1]:
            x = a[i]
            a[i] = a[i+1]
            a[i+1] = x
print (a)