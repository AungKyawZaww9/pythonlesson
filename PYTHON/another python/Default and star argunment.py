def area(length=1, width= 2):
    return length * width
print("Area 1 =",area())
print("Area 2 =",area(10))
print("Area 3 =",area(2,3))

def names(*name):
    for i in name:
        print(i)
names("Aung","kyaw","zaww")