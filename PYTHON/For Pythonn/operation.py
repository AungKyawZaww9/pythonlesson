# Operation
# n = 1
# n %= 3
# print(n)
#
# x = 3
# y = 2
# print(x+y)
# print(x*y)
# print(x%y)
# print(x/y)

# --------------------------

# type Cast

# n = input("Enter name: ")
#
# c = int(n)
#
# add = c + 12
#
# print(add)
# print(type(add))
# print(type(c))

# --------------------------------

# condition

# i = 0
# if i == 0:
#     print("It is Zero")
#
# elif i == 1:
#     print("It is One")
#
# else:
#     print("Nothing")
#
# print("End Program")

# --------------------------------

# for loop

# name = ["Aung", "Kyaw ", "Zaww"]
# # for i in ["Aung", "Kyaw ", "Zaww"]: #^^^^^
# for i in name:
#     print(i)
# print("Done")

# for z in range(1, 11, 1):
#     print(z)
# print("Done range")

# --------------------------------

# while loop

# n = 5
# while n > 0:
#     print(n, "Hello")
#     n -= 1
# print("While Done")
# print(n)

# --------------------------------


# Compare Largest Number

# n = [1000, 900, 800, 700, 600, 500, 400, 2000]
#
# maxnum = n[0]
#
# for i in n:
#     if i > maxnum:
#         maxnum = i
#     print("Current Number: ", i, "Largest Number: ", maxnum)
# print("Max is ", maxnum)

# --------------------------------

# Compare Samllest Number

# Compare Smallest Number

# minnum = None
# for i in [1000, 900, 800, 700, 600, 500, 400, 2000]:
#     if minnum is None: # is not also has
#         minnum = i
#
#     elif i < minnum:
#         minnum = i
#     print("Current Number: ", i,"Minnum: ", minnum)
#
# print("Min is ", minnum)

# --------------------------------

# String

# name = "Aung Kyaw"
#
# print(name[0])
# print(name[0:4])
# print(name[0:3])
# print(name.lower())
# print(name.upper())
#
# print("It is index : ", name.find('n'))

# find = name.find('A')
# print("It is : ",find)

# --------------------------------


# Function

# def add(a, b):
#     return a*b
#
# g = input("y or n")
# if(g =='y'):
#     a = input("Enter a number1: ")
#     num1 = int(a)
#
#     b = input("Enter a number2: ")
#     num2 = int(b)
#
#
#
# print("Total result", add(num1, num2))

# --------------------------------


# default argument

# def area(length=1, width=2):
#     return length * width
#
#
# print("First result Area :", area())
# print("Second result Area :", area(4))
# print("Third result Area : ", area(4, 3))
#
# # STAR NAME
# def names(*name):
#     for i in name:
#         print(i)
#
# names("aung", "kyaw", "zaww", 33, 33, 54.4)


# GLOBAL AND LOCAL

# x = 10
#
# def num(): #local
#     x = 20
#     x += 1
#     print(x)
#
# def num1(): #global
#     global x
#     x += 1
#     print(x)
#
# num() #for local
# num1() #for global

# --------------------------------


# TRY EXCEPT

# name = "aung kyaw zaww"
#
# try:
#     name1 = int(name)
#
# except:
#     name1 = -1
#     print(name1)

# --------------------------------


# WHILE LOOP
n = input("Enter Number: ")
change = int(n)

# change = 0
while (change < 10):
    print(change, "Hello")
    change += 1

# --------------------------------
















