## bai 1
# n=5
# for i in range(n):
#     for j in range(i):
#         print ('* ', end="")
#     print('')
#
# for i in (3,2,1):
#     for j in range(i):
#         print('* ', end="")
#     print('')

# #bài 2
# l = list(input("dãy cần xác định"))
# so_chan=[]
# so_le=[]
# for i in l:
#     if int(i)%2 == 0:
#         so_chan.append(i)
#     else:
#         so_le.append(i)
#
# print("số số chẵn:", len(so_chan))
# print("số số lẻ:", len(so_le))

##bài 3
# for i in range (1500,2701):
    # if i%7 == 0 and i%5==0:
    #     print (i)

##bài 4
# import random
# i = random.randint(1,10)
# x = int(input("đoán đi"))
# for y in range(10):
#     if x == i:
#         print("đoán đúng")
#         break
#     else:
#         x = int(input("đoán lại"))

##BAI5
# l = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
# {"class":'V', "section":'A'}]
# for item in l:
#    print ("Type of ",item, " is ", type(item))

##bài 6
# for i in range (7):
#     if i == 3 or i == 6:
#         continue
#     print (i)

##bài7
# def f(x):
#     if x <2:
#         return x
#     return f(x-2)+f(x-1)
#
# for i in range (50):
#     print(f(i), end=" ")


##bai 8
# for i in range (0,51):
#     if i == 0:
#         print("fizzbuzz")
#     elif i%15 == 0:
#         print("fizzbuzz")
#         continue
#     elif i%3 == 0:
#         print("fizz")
#     elif i%5 == 0:
#         print("buzz")
#     else:
#         print(i)

##bai 10
# a = int(input("a"))
# b = int(input("b"))
# c = int(input("c"))
# d = int(input("d"))
# e = int(input("e"))
# l = [a,b,c,d,e]
# for i in l:
#     if i > 999 and i%5 == 0:
#         print (i)

## bai 11
# s = input("Input a string")
# d = 0
# l = 0
# for i in s:
#     if i.isdigit():
#         d=d+1
#     elif i.isalpha():
#         l=l+1
#     else:
#         pass
# print("Letters", l)
# print("Digits", d)

# #bai 12: (bài này có gì đó vẫn sai khi e nhập số vào)
# def validate():
#     while True:
#         password = input("Enter a password: ")
#         if len(password) < 6 or len(password) > 16 :
#             print("Make sure your password is at lest 8 letters and at most 16 letters")
#         # elif not password.isdigit():
#         #     print("Make sure your password has a number in it")
#         elif not password.isupper():
#              print("Make sure your password has a upper in it")
#         elif not password.islower():
#             print("Make sure your password has a lower in it")
#         else:
#             print("Your password is fine")
#             break
#
# validate()


#bai 13
# n ='''      ***
#      *   *
#      *   *
#      *****
#      *   *
#      *   *
#      *   *'''
# print (n)

##bai 14
# for i in range(10):
#     for j in range(i):
#         print (i, end="")
#     print('')

