name = "\n\n\t\t\t\t\t\t\t\t\tGrading System for Dagon University"
print(name.upper())
name1 = "\t\t\t\t\t\t\t\t\t International Relations Department"
print(name1.upper())
print("\t\t\t\t\t\t\t\t\t   ACADEMIC RECORDS OF YEAR END")

while True:


    def add(myanmar, english, paper1, paper2, A_M, History, Geography):
        return myanmar + english + paper1 + paper2 + A_M + History + Geography
    print("\n-----------------------------------------------")
    print("Put 'N' if you wannna exit")
    print("-----------------------------------------------")
    year = input("\n\nEnter year: ")

    if year == "First year":
        name = input("Enter student name: ")
        father_name = input("Enter father name: ")
        sex = input("Sex(Male or female): ")
        RolL_Number = input("Enter student roll number(1IR - ): ")
        print("\t--------------------")

        myanmar = input("\nEnter the result mark of Myanmar: ")
        a = int(myanmar)
        english = input("Enter the result mark of English: ")
        b = int(english)
        paper1 = input("Enter the result mark of Paper 1: ")
        c = int(paper1)
        paper2 = input("Enter the result mark of Paper 2: ")
        d = int(paper2)
        A_M = input("Enter the result mark of A.M: ")
        e = int(A_M)
        History = input("Enter the result mark of History: ")
        f = int(History)
        Geography = input("Enter the result mark of Geography: ")
        g = int(Geography)
        print("\t--------------------")

        add = a + b + c + d + e + f + g
        print("\n\n\nStudent Name : ", name)
        print("Father Name: ", father_name)
        print("Sex: ", sex)
        print("Roll_Number :1IR-", RolL_Number)
        print("Total mark are : ", add)

        do = add / 5
        if 115 <= do <= 150:
            print("Your Grade is : A+")
        elif 95 <= do <= 110:
            print("Your Grade is : A")
        elif 85 <= do <= 94:
            print("Your Grade is : B")
        elif 65 <= do <= 84:
            print("Your Grade is : C")
        elif 51 <= do <= 64:
            print("Your Grade is : D")
        elif 0 <= do <= 50:
            print("Your Grade is : E")
            print("Your exam is fall")
        else:
            print("Wrong Grade")
        print("\nA+ = Credit\t\t\t\tA = Qualified\t\t\t\tB = Passed\t\t\t\tC = passed\t\t\t\tD/E = Moderation or Fall")
        print("\t\t\t\t---------------------------------------------------------------------------------------------------")

    if year == "Second year":
        name = input("Enter student name: ")
        father_name = input("Enter father name: ")
        sex = input("Sex(Male or female): ")
        RolL_Number = input("Enter student roll number(2IR - ): ")
        print("\t--------------------")

        myanmar = input("\nEnter the result mark of Myanmar: ")
        a = int(myanmar)
        english = input("Enter the result mark of English: ")
        b = int(english)
        paper1 = input("Enter the result mark of Paper 1: ")
        c = int(paper1)
        paper2 = input("Enter the result mark of Paper 2: ")
        d = int(paper2)
        A_M = input("Enter the result mark of A.M: ")
        e = int(A_M)
        History = input("Enter the result mark of History: ")
        f = int(History)
        Geography = input("Enter the result mark of Geography: ")
        g = int(Geography)
        print("\t--------------------")

        add = a + b + c + d + e + f + g
        print("\n\n\nStudent Name : ", name)
        print("Father Name: ", father_name)
        print("Sex: ", sex)
        print("Roll_Number :2IR-", RolL_Number)
        print("Total mark are : ", add)
        do = add / 5
        if 115 <= do <= 150:
            print("Your Grade is : A+")
        elif 95 <= do <= 110:
            print("Your Grade is : A")
        elif 85 <= do <= 94:
            print("Your Grade is : B")
        elif 65 <= do <= 84:
            print("Your Grade is : C")
        elif 51 <= do <= 64:
            print("Your Grade is : D")
        elif 0 <= do <= 50:
            print("Your Grade is : E")
            print("Your exam is fall")
        else:
            print("Wrong Grade")
        print("\nA+ = Credit\t\t\t\tA = Qualified\t\t\t\tB = Passed\t\t\t\tC = passed\t\t\t\tD/E = Moderation or Fall")
        print("\t\t\t\t---------------------------------------------------------------------------------------------------")

    def add(Paper1, Paper2, Paper3, Paper4, Economics, Law):
        return Paper1 + Paper2 + Paper3 + Paper4 + Economics + Law


    if year == "Third year":
        name = input("Enter student name: ")
        father_name = input("Enter father name: ")
        sex = input("Sex(Male or female): ")
        RolL_Number = input("Enter student roll number(3IR - ): ")
        print("\t--------------------")

        Paper1 = input("\nEnter the result mark of Paper 1: ")
        a = int(Paper1)
        Paper2 = input("Enter the result mark of Paper 2: ")
        b = int(Paper2)
        Paper3 = input("Enter the result mark of Paper 3: ")
        c = int(Paper3)
        Paper4 = input("Enter the result mark of Paper 4: ")
        d = int(Paper4)
        Economics = input("Enter the result mark of Economics: ")
        e = int(Economics)
        Law = input("Enter the result mark of Law: ")
        f = int(Law)
        print("\t--------------------")

        add = a + b + c + d + e + f
        print("\n\n\nStudent Name : ", name)
        print("Father Name: ", father_name)
        print("Sex: ", sex)
        print("Roll_Number :3IR-", RolL_Number)
        print("Total mark are : ", add)

        do = add / 5
        if 105 <= do <= 120:
            print("Your Grade is : A+")
        elif 90 <= do <= 104:
            print("Your Grade is : A")
        elif 76 <= do <= 89:
            print("Your Grade is : B")
        elif 61 <= do <= 75:
            print("Your Grade is : C")
        elif 46 <= do <= 60:
            print("Your Grade is : D")
        elif 0 <= do <= 45:
            print("Your Grade is : E")
            print("Your exam is fall")
        else:
            print("Wrong Grade")


        def grades(*name):
            for y in name:
                print(y)
        grades("\nA+ = Credit\t\t\t\tA = Qualified\t\t\t\tB = Passed\t\t\t\tC = passed\t\t\t\tD/E = Moderation or Fall")
        print("\t\t\t\t---------------------------------------------------------------------------------------------------")

    if year == "Fourth year":
        name = input("Enter student name: ")
        father_name = input("Enter father name: ")
        sex = input("Sex(Male or female): ")
        RolL_Number = input("Enter student roll number(4IR - ): ")
        print("\t--------------------")

        Paper1 = input("\nEnter the result mark of Paper1: ")
        a = int(Paper1)
        Paper2 = input("Enter the result mark of Paper2: ")
        b = int(Paper2)
        Paper3 = input("Enter the result mark of Paper 3: ")
        c = int(Paper3)
        Paper4 = input("Enter the result mark of Paper 4: ")
        d = int(Paper4)
        Economics = input("Enter the result mark of Economics: ")
        e = int(Economics)
        Law = input("Enter the result mark of Law: ")
        f = int(Law)
        print("\t--------------------")

        add = a + b + c + d + e + f
        print("\n\n\nStudent Name : ", name)
        print("Father Name: ", father_name)
        print("Sex: ", sex)
        print("Roll_Number :4IR-", RolL_Number)
        print("Total mark are : ", add)

        do = add / 5
        if 105 <= do <= 120:
            print("Your Grade is : A+")
        elif 90 <= do <= 104:
            print("Your Grade is : A")
        elif 76 <= do <= 89:
            print("Your Grade is : B")
        elif 61 <= do <= 75:
            print("Your Grade is : C")
        elif 46 <= do <= 60:
            print("Your Grade is : D")
        elif 0 <= do <= 45:
            print("Your Grade is : E")
            print("Your exam is fall")
        else:
            print("Wrong Grade")


        def grades(*name):
            for z in name:
                print(z)
        grades("\nA+ = Credit\t\t\t\tA = Qualified\t\t\t\tB = Passed\t\t\t\tC = passed\t\t\t\tD/E = Moderation or Fall")
        print("\t\t\t\t---------------------------------------------------------------------------------------------------")

    elif year == "N":
        print("\n\n\t\t\t\t\t\t\t\t\t\t\t<<<<Thank you>>>>")
        exit()
    else:
        print("\n<<<Please write BIG the beginning of the words of year>>>")


