a = 10

def num():
    a = 20
    a += 1
    print(a)

def num1():
    global a
    a += 2
    print(a)

print(a)
num()
num1()



