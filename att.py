student_record = []
temp_list = []
teacher_name = ""

def addStudent(name):
    newStudent = {
        "name" : name,
        "isPresent" : "yes"
    }
    student_record.append(newStudent)


# def addAbsent(name):
#     newStudent = {
#         "name" : name,
#         "isPresent" : "no"
#     }
#     absent_list.append(newStudent)


teacher_name = input("Enter your name: ")
print(f"Hi {teacher_name}!")
student_data = input("Enter your list of students separated by comma: ")
student_list = student_data.split(", ")


for student in student_list:
    addStudent(student)


ifAnyoneAbsent = input("Any absent y/n: ")


if (ifAnyoneAbsent == 'y'):

    user_input = input("Enter names of absent students separated by commas: ")
    temp_list = user_input.split(", ")

    for student in student_record:
        if student["name"] in temp_list:
            student["isPresent"] = "no"
            print("=====================================")
            print(f"Marked {student['name']} as absent")
            print("=====================================\n")

for student in student_record:
    print(f"Name: {student['name']} is_present: {student['isPresent']}")


