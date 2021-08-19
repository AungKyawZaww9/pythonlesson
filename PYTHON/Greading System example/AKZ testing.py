
'''while True:

    year = input("\nEnter Year :")

    if year == "First year":
        name = input("Enter student name: ")
        RolL_Number = input("Enter student roll number(1IR - ): ")
        myanmar = input("Enter the result mark of Myanmar: ")
        english = input("Enter the result mark of English: ")
        Paper1 = input("Enter the result mark of Paper 1: ")
        Paper2 = input("Enter the result mark of Paper 2: ")
        A_M = input("Enter the result mark of A.M: ")
        History = input("Enter the result mark of History: ")
        Geography = input("Enter the result mark of Geography: ")

    if year == "Second year":
        name = input("Enter student name: ")
        RolL_Number = input("Enter student roll number(2IR - ): ")
        myanmar = input("Enter the result mark of Myanmar: ")
        english = input("Enter the result mark of English: ")
        Paper1 = input("Enter the result mark of Paper 1: ")
        Paper2 = input("Enter the result mark of Paper 2: ")
        A_M = input("Enter the result mark of A.M: ")
        History = input("Enter the result mark of History: ")
        Geography = input("Enter the result mark of Geography: ")

    if year == "Third year":
        name = input("Enter student name: ")
        RolL_Number = input("Enter student roll number(3IR - ) :")
        Paper1 = input("Enter the result mark of Paper 1: ")
        Paper2 = input("Enter the result mark of Paper 2: ")
        Paper3 = input("Enter the result mark of Paper 3: ")
        Economics = input("Enter the result mark of Paper Economics: ")
        Law = input("Enter the result mark of Paper Law: ")

    if year == "Fourth year":
        name = input("Enter student name: ")
        RolL_Number = input("Enter student roll number(4IR - ): ")
        Paper1 = input("Enter the result mark of Paper 1: ")
        Paper2 = input("Enter the result mark of Paper 2: ")
        Paper3 = input("Enter the result mark of Paper 3: ")
        Economics = input("Enter the result mark of Paper Economics: ")
        Law = input("Enter the result mark of Paper Law: ")

    elif year == "Y":
        continue
    elif year == "N":
        exit()
    else:
        print("\n\nSomething wrong.. Please again")'''

def grades(*name):
    for i in name:
        print(i)
grades("Aung kyaw zaww")


