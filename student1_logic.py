def calculate_total(marks):
    return sum(marks)


def calculate_percentage(marks):
    total = calculate_total(marks)
    return total / len(marks)


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "F"


def calculate_result(percentage):
    if percentage >= 35:
        return "Pass"
    else:
        return "Fail"


def create_student_record(roll_no, name, marks):
    total = calculate_total(marks)
    percentage = calculate_percentage(marks)
    grade = calculate_grade(percentage)
    result = calculate_result(percentage)

    return {
        "roll_no": roll_no,
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "result": result
    }


def show_record(student):
    print("\n----- Student Record -----")
    print("Roll No:", student["roll_no"])
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    print("Total:", student["total"])
    print("Percentage:", round(student["percentage"], 2))
    print("Grade:", student["grade"])
    print("Result:", student["result"])
    print("--------------------------\n")