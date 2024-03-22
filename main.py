studentList = []

keepEncoding = 'y'
topStudent = ""
highestGrade = 0

def addStudent(name, grade):
    newStudent = {
        "name" : name,
        "grade" : grade
    }
    studentList.append(newStudent)

#populate
# addStudent("John", 88)
# addStudent("Mary", 76)
# addStudent("Jenny", 50)

while keepEncoding == 'y':
    new_name = input("Enter a name: ")
    new_grade = int(input("Enter grade:"))
    addStudent(new_name , new_grade)
    
    keepEncoding = input("Continue? 'y/n': ")


for student in studentList:
    if student["grade"] > highestGrade:
        highestGrade = student["grade"]
        topStudent = student["name"]

print(f"{topStudent} is the top student in class with a grade of {highestGrade}")







