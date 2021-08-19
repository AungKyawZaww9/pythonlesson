def add(Paper1, Paper2, Paper3, Paper4, Economics, Law):
    return Paper1 + Paper2 + Paper3 + Paper4 + Economics + Law

year = input("Enter Year: ")
if year == "Third year":
    name = input("Enter student name: ")
    RolL_Number = input("Enter student roll number(1IR - ): ")
    Paper1 = input("Enter the result mark of Myanmar: ")
    a = int(Paper1)
    Paper2 = input("Enter the result mark of English: ")
    b = int(Paper2)
    Paper3 = input("Enter the result mark of Paper 1: ")
    c = int(Paper3)
    Paper4 = input("Enter the result mark of Paper 2: ")
    d = int(Paper4)
    Economics = input("Enter the result mark of Economics 3: ")
    e = int(Economics)
    Law = input("Enter the result mark of Law: ")
    f = int(Law)

    add = a + b + c + d + e + f
    print("\n\n\nStudent Name : ", name)
    print("Roll_Number :3IR-", RolL_Number)
    print("Total mark are : ", add)

    do = add / 5
    if 81 <= do <= 100:
        print("Your Grade is : A+")
    elif 71 <= do <= 80:
        print("Your Grade is : A")
    elif 51 <= do <= 70:
        print("Your Grade is : B")
    elif 41 <= do <= 50:
        print("Your Grade is : C")
    elif 35 <= do <= 40:
        print("Your Grade is : F")
    elif 0 <= do <= 25:
        print("Your exam is fall")
    else:
        print("Wrong Grade")
