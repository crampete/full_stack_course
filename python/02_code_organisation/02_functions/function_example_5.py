from pprint import pprint

def collect_student_details():
    student_name = input("Please enter the student's name.\n")
    student_age = input("Please enter the student's age.\n")

    return {'name': student_name, "age": student_age}



student_details = []

while 1:
    y_or_n = input("Do you want to enter any more student names?\n Please input y or n.")

    if y_or_n == 'y':
        details = collect_student_details()
        student_details.append(details)
    elif y_or_n == 'n':
        break
    else:
        print("Invalid. Please enter y or n only.")


print("The final student details are as follows.")
pprint(student_details)
