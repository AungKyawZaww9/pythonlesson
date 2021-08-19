'''def result(positive= 3, negative= 4):
    return positive *  negative
print("Print 1:",result())#12
print("Print 2:",result(10))#40
print("Print 3:",result(3,3))#9'''


def shop(*item):
    for i in item:
        print(i)
shop('pencilrulereraser')

print("pencil ruler eraser")