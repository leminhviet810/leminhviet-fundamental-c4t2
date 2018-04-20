# row = int(input("row"))
# col = int(input("col"))
# f = []
# for i in range (row):
#     l = []
#     for j in range (col):
#         l.append(i*j)
#     f.append(l)
# print (f)

# a = sorted(x for x in input("chu j do").split(","))
# for x in a:
#     print(x, end=",")

#cachs 2
# a = input("st").split(",")
# for j in range (len(a)):
#     for i in range (len(a)-1):
#         if a[i] > a[i+1]:
#             x = a[i]
#             a[i] = a[i+1]
#             a[i+1] = x
# for x in a:
#     print(x, end = ",")
# print("\b")

#######################

# s = "abcsd"
# x = s.upper()
# print(x)

###################


# a = [tuple(x.split(",")) for x in input("Input: ").split(";")]
# for j in range (100):
#     for i in range (len(a)-1):
#         if a[i] > a[i+1]:
#             x = a[i]
# #             a[i] = a[i+1]
# #             a[i+1] = x

# for x in range (len(a)-1):
#     if a[x][0] == a[x+1][0] :
#         for y in range(len(a)):
#             for z in range(len(a) - 1):
#                 if a[z][1] > a[z + 1][1]:
#                     x = a[z][1]
#                     a[z][1] = a[z + 1][1]
#                     a[z + 1][1] = x
#
# for x in range (len(a)-1):
#     if a[x][1] == a[x + 1][1]:
#         for y in range(len(a)):
#             for z in range(len(a) - 1):
#                 if a[z][2] > a[i + 1][2]:
#                     x = a[i][2]
#                     a[i][2] = a[i + 2][2]
#                     a[i + 2][2] = x

# print(a)


####################

# def fibonanci(x):
#     if x <=1:
#         return x
#     else:
#         return fibonanci(x-1)+fibonanci(x-2)
#
# for i in range (10):
#     print(fibonanci(i), end=",")


# cách 2 (trẩu)
# a = b = c = 1
# n = int(input("Input: "))
# for i in range(n-2):
#     b = c
#     c = a + b
#     a = b
# print(c)

############################
# for x in ("i", "you"):
# #     for y in ("play", "verb"):
# #         for z in ("hockey", "football"):
# #             print (x,y,z)


# a = [12,24,35,24,88,120,155,120,88,120,155]
# i = j =0
#
# while i <= len(a)-2:
#     i+=1
#     while j <= len(a)-2:
#         j+=1
#         if a[j] == a[i]:
#             del a[i]
#     else:
#         continue
# print(a)

# x,y = 0,1
# x,y = y,x+y
# print (y)