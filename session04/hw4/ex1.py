def accept_login(x,y,z):
    if x.get(y) == z:
        return "successful"
    else:
        return "false"

users = {"user1":"password1","user2":"password2","user3":"password3"}
a = accept_login(users, input("tên"),input("mk"))
print (a)