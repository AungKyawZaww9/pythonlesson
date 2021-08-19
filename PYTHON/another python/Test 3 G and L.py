a = 55

def acount():
    a = 5
    a -= 1
    print(a)#4
def acount1():
    global a
    a -= 1
    print(a)#54
print(a)
acount()
acount1()
