database = {}

def studentEntry():
    student = input("Enter the student name:\n")
    marks = int(input("Enter his marks:\n"))
    database[student]=marks

def maxGrade():
    maximum = 0
    student = ""
    for key in database:
        print(database[key])
        if(database[key]>maximum):
            maximum = database[key]
            print(maximum)
            student = key
            print(student)
    return maximum,student

def averageClass():
    sum = 0
    for key in database:
        sum = sum + database[key]
    return sum/5

def gradeSystem():
    for i in database:
        if(database[i]<30):
            print(f"{i} gets an F\n")
        elif(database[i]<50):
            print(f"{i} gets a D\n")
        elif(database[i]<60):
            print(f"{i} gets a C\n")
        elif(database[i]<70):
            print(f"{i} gets a B\n")
        elif(database[i]<80):
            print(f"{i} gets an A\n")
        else:
            print(f"{i} gets an O\n")

for i in range(0,5):
    studentEntry()

max_marks,student = maxGrade()
print(f"The highest marks scored is {max_marks} by {student}\n")

average = averageClass()
print(f"The total average of the class is {average}\n")

gradeSystem()
