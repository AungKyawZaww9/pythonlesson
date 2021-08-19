min = 0

for  i in [999,8,77,990393,5940049,454,33]:

    if min is not None:
        min = i
    elif i < min:
        min = i

    print("current number",i,"min",min)
print("min is",min)

max = None
for i in [4005, 300, 209, 606, 4006]:
    if max is None:
        max = i
    elif i > max:
        max = i
    print("First number is ",i,"Max number is",max)
print("Max",max)