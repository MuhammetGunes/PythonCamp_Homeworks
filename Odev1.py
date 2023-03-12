Names = ["Lorem", "Ipsum", "asds"]

def addStudent():
    fName_lName = input("Please enter name and surname for add action:")
    Names.append(fName_lName)


def addStudents():
    list1 = []
    while True:
        fNames_lNames = input("Please enter name and surname for add action:")
        list1.append(fNames_lNames)
        t_f = input("Do you want to add more student? (yes/no)")
        if t_f == "no":
            break
    Names.extend(list1)


def deleteStudent():
    deletedName = input("Please enter name for delete action:")
    i=0
    while i<len(Names):
        if Names[i] == deletedName:
            Names.remove(deletedName)
        i = i+1


def deleteStudents():
    list1 = []
    while True:
        deletedName = input("Please enter name and surname for delete action:")
        Names.remove(deletedName)
        t_f = input("Do you want to delete more student? (yes/no)")
        if t_f == "no":
            break

def showStudent():
    for i in range(len(Names)):
        print(Names[i])



def learnStudentNumber():
    fName_lName = input("Please enter student name and surname for learning the student number:")
    for i in range(len(Names)):
        if Names[i] == fName_lName:
            print(f"Student number is {i}")

# addStudent()
# addStudents()
# deleteStudent()
# deleteStudents()
# showStudent()
# learnStudentNumber()
print(Names)


