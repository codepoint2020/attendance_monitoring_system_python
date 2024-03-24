from prettytable import PrettyTable



daily_records = []
record_day = True
day_number = 1


while record_day:
    table = PrettyTable()
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

    
    
    daily_records.append(student_record)

    next_day = input("Record for the next day? y/n: ")
    if next_day == 'n' or next_day == 'q':
        record_day = False  # Exit the loop to stop recording for more days
    

for day_records in daily_records:
    table = PrettyTable(["Name of Student", "Attendance Status", "Punctuality"])
    
    for record in day_records:
        table.add_row([record['name'], record['isPresent'], record['isLate']])
    
    print(f"Day {day_number}")
    print(table)
    print("\n")
    day_number += 1

