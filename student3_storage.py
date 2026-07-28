import csv
import os

FILE_NAME = "students.csv"


def ensure_file_exists():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["roll_no", "name", "marks", "total", "percentage", "grade", "result"])


def save_students(students):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["roll_no", "name", "marks", "total", "percentage", "grade", "result"])
        for student in students:
            writer.writerow([
                student["roll_no"],
                student["name"],
                "|".join(map(str, student["marks"])),
                student["total"],
                student["percentage"],
                student["grade"],
                student["result"]
            ])


def load_students():
    ensure_file_exists()
    students = []

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({
                "roll_no": row["roll_no"],
                "name": row["name"],
                "marks": list(map(float, row["marks"].split("|"))) if row["marks"] else [],
                "total": float(row["total"]),
                "percentage": float(row["percentage"]),
                "grade": row["grade"],
                "result": row["result"]
            })

    return students


def add_student_to_file(student):
    students = load_students()
    students.append(student)
    save_students(students)


def search_student_in_file(roll_no):
    students = load_students()
    for student in students:
        if student["roll_no"] == roll_no:
            return student
    return None


def update_student_in_file(updated_student):
    students = load_students()
    for i, student in enumerate(students):
        if student["roll_no"] == updated_student["roll_no"]:
            students[i] = updated_student
            save_students(students)
            return True
    return False


def delete_student_from_file(roll_no):
    students = load_students()
    new_students = [student for student in students if student["roll_no"] != roll_no]

    if len(new_students) == len(students):
        return False

    save_students(new_students)
    return True