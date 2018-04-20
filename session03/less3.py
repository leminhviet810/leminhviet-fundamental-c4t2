# for i in range (2000,3201):
#     if i%5 == 0:
#         continue
#     if i%7 == 0:
#         print (i, end=", ")

# def giaithua(x):
#     if x  <2 :
#         return 1
#     else:
#         return giaithua(x-1)*x
#
# print(giaithua(8))

# def binhphuong(x):
# #     return x**2
# #
# # for i in range (1,9):
# #     y = i
# #     print(y,":", binhphuong(y), end=" , ")

# for x in range (1,35):
#         for y in range (1,35):
#             if x + y == 35 and 2*x +4*y == 94:
#                 print(x)
#                 print(y)

     #      # #     y = 35 - x
# #     if 2*x + 4*y == 94:
# #         print ("ga co" ,x)
# #         print ("tho co",y)

# def f(x):
#     if x ==0:
#         return 1
#     else:
#         return f(x-1)+100
#
# print(f(5))

########## lệnh x = ord()
########### lệnh để check về bảng mã sci

# x= 10
# while x :##đến khi x = 0 thì false -> thoát vòng lặp
#     x = x - 1
#     if x%2 != 0:
#         continue
#     print (x)

    ##while: chủ yếu là phép toán so sánh = == >= <=


# y**2= <-> y = y**2
# y//2= <-> y = y//2

# dictionary
# lop_code4teen = {"tenlop": "c4t", "siso": (15,29) }
# # #
# # # print(lop_code4teen)
# # #
# # # print(lop_code4teen.keys())
# # # print(lop_code4teen.values())
# # #
# # # lop_code4teen["tenlop"] = "hello"
# # # print(lop_code4teen)

# baif 3
# dict = {}
# for i in range (1,9):
#     dict[i] = i**2
# print (dict)

# a =(1,2,3)
# b =(1,2)
# print(hex(id(a)))
# a = a+b #tuple là duy nhất. đây là 2 mảng a khác nhau
# print (a)
# print(hex(id(a)))
# print("array")
# c =[1,2,3]
# print(hex(id(c)))
# c.append([1,2]) # đã tạo ra 1 c mới hoàn toàn
# print(c)
# print(hex(id(c)))

### buổi sau là class
# sum = 0
# n = int(input("nhập n"))
# for x in range (1,n+1):
#     sum = sum + x/(x+1)
# print (sum)

# i = int(input("Input number of rows: "))
# j = int(input("Input number of columns: "))
# array = [[0 for col in range(j)] for row in range(i)]
#
# for row in range(i):
#     for col in range(j):
#         array[row][col]= row*col
#
# print(array)




