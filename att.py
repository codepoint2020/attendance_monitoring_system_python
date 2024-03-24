from prettytable import PrettyTable
table = PrettyTable()

table.align = "l"

student_record = []
temp_list = []
teacher_name = ""

attendance_percentage = ""
late_percentage = ""

def addStudent(name):
    newStudent = {
        "name" : name,
        "isPresent" : "present",
        "isLate": ""
    }
    student_record.append(newStudent)


teacher_name = input("Enter your name: ")
print(f"Hi {teacher_name}!")
student_data = input("Enter your list of students separated by comma: ")
student_list = student_data.split(", ")


for student in student_list:
    addStudent(student)


#IF THERE IS/are AN ABSENT/ABSENCES
ifAnyoneAbsent = input("Any absent y/n: ")


while (ifAnyoneAbsent != 'y' and ifAnyoneAbsent != 'n' and ifAnyoneAbsent !='q'):

    print("ERROR: Invalid input, please enter 'y' or 'n' if you need to quit the program press 'q'")
    ifAnyoneAbsent = input("Any absent? y/n: ")


    if(ifAnyoneAbsent == 'q'):
        break


if (ifAnyoneAbsent == 'y'):
    user_input = ""
    user_input = input("Enter names of absent students separated by commas: ")
    temp_list = user_input.split(", ")

    for student in student_record:
        if student["name"] in temp_list:
            student["isPresent"] = "absent"
           

elif (ifAnyoneAbsent == "n"):

    attendance_percentage = "100%"


#if there is/are late/lates
ifAnyoneLate = input("Any late y/n: ")


while (ifAnyoneLate != 'y' and ifAnyoneLate != 'n' and ifAnyoneLate !='q'):

    print("ERROR: Invalid input, please enter 'y' or 'n' if you need to quit the program press 'q'")
    ifAnyoneLate = input("Any late(s)? y/n: ")


    if(ifAnyoneLate == 'q'):
        break


if (ifAnyoneLate == 'y'):
    user_input = ""
    temp_list = []
    user_input = input("Enter name(s) of students to be marked as late: ")
    temp_list = user_input.split(", ")

    for student in student_record:
        if student["name"] in temp_list:
            student["isLate"] = "late"
           

elif (ifAnyoneLate == "n"):

    late_percentage = "0%"

       

#Preparing for report generation
names_students = []
attendance_status = []
late_status = []

for student in student_record:
    names_students.append(student['name'])
    attendance_status.append(student['isPresent'])
    late_status.append(student['isLate'])


# print(record_result) - Print Report
table.add_column("Name of Student", names_students)
table.add_column("Attendance Status", attendance_status)
table.add_column("Punctuality", late_status)
print(table)


