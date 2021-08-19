name = "\n\n\t\t\t\t\t\t\t\t\tGrading System for Dagon University"
print(name.upper())
name1 = "\t\t\t\t\t\t\t\t\tInternational Relations Department"
print(name1.upper())
try:
    while True:

        def add(myanmar, english, paper1, paper2, A_M, History, Geography):
            return myanmar + english + paper1 + paper2 + A_M + History + Geography


        print("\n\n\n-----------------------------------------------")
        print("Put 'N' if you wannna exit")
        print("-----------------------------------------------")
        year = input("\nEnter year: ")

        if year == "First year":
            name = input("Enter student name: ")
            RolL_Number = input("Enter student roll number(1IR - ): ")

            myanmar = input("Enter the result mark of Myanmar: ")
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

            add = a + b + c + d + e + f + g
            print("\n\n\nStudent Name : ", name)
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
                print("Your Grade is : F")
            elif 0 <= do <= 50:
                print("Your Grade is : G")
                print("Your exam is fall")
            else:
                print("Wrong Grade")

        if year == "Second year":
            name = input("Enter student name: ")
            RolL_Number = input("Enter student roll number(2IR - ): ")

            myanmar = input("Enter the result mark of Myanmar: ")
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

            add = a + b + c + d + e + f + g
            print("\n\n\nStudent Name : ", name)
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
                print("Your Grade is : F")
            elif 0 <= do <= 50:
                print("Your Grade is : G")
                print("Your exam is fall")
            else:
                print("Wrong Grade")


        def add(Paper1, Paper2, Paper3, Paper4, Economics, Law):
            return Paper1 + Paper2 + Paper3 + Paper4 + Economics + Law


        if year == "Third year":
            name = input("Enter student name: ")
            RolL_Number = input("Enter student roll number(3IR - ): ")
            Paper1 = input("Enter the result mark of Myanmar: ")
            a = int(Paper1)
            Paper2 = input("Enter the result mark of English: ")
            b = int(Paper2)
            Paper3 = input("Enter the result mark of Paper 1: ")
            c = int(Paper3)
            Paper4 = input("Enter the result mark of Paper 2: ")
            d = int(Paper4)
            Economics = input("Enter the result mark of Economics: ")
            e = int(Economics)
            Law = input("Enter the result mark of Law: ")
            f = int(Law)

            add = a + b + c + d + e + f
            print("\n\n\nStudent Name : ", name)
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
                print("Your Grade is : F")
            elif 0 <= do <= 45:
                print("Your Grade is : G")
                print("Your exam is fall")
            else:
                print("Wrong Grade")

        if year == "Fourth year":
            name = input("Enter student name: ")
            RolL_Number = input("Enter student roll number(4IR - ): ")
            Paper1 = input("Enter the result mark of Myanmar: ")
            a = int(Paper1)
            Paper2 = input("Enter the result mark of English: ")
            b = int(Paper2)
            Paper3 = input("Enter the result mark of Paper 1: ")
            c = int(Paper3)
            Paper4 = input("Enter the result mark of Paper 2: ")
            d = int(Paper4)
            Economics = input("Enter the result mark of Economics: ")
            e = int(Economics)
            Law = input("Enter the result mark of Law: ")
            f = int(Law)

            add = a + b + c + d + e + f
            print("\n\n\nStudent Name : ", name)
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
                print("Your Grade is : F")
            elif 0 <= do <= 45:
                print("Your Grade is : G")
                print("Your exam is fall")
            else:
                print("Wrong Grade")


        elif year == "N":
            print("\n\n\t\t\t\t\t\t\t\t\t<<<<Thank you>>>>")
            exit()
        else:
            print("<<<Please write the beginning of the words of year>>>")


except:
    print("....")