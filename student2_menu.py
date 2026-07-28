from student1_logic import create_student_record, show_record
from student3_storage import load_students, save_students, add_student_to_file, update_student_in_file, delete_student_from_file, search_student_in_file


def input_marks():
    marks = []
    for i in range(1, 4):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks should be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
    return marks


def add_student():
    roll_no = input("Enter Roll No: ")
    name = input("Enter Student Name: ")
    marks = input_marks()

    student = create_student_record(roll_no, name, marks)
    add_student_to_file(student)
    print("Student record added successfully.")


def view_all_students():
    students = load_students()
    if not students:
        print("No records found.")
        return

    for student in students:
        show_record(student)


def search_student():
    roll_no = input("Enter Roll No to search: ")
    student = search_student_in_file(roll_no)
    if student:
        show_record(student)
    else:
        print("Student not found.")


def update_student():
    roll_no = input("Enter Roll No to update: ")
    students = load_students()
    found = False

    for student in students:
        if student["roll_no"] == roll_no:
            print("Enter new details:")
            name = input("Enter Student Name: ")
            marks = input_marks()
            new_student = create_student_record(roll_no, name, marks)

            student["name"] = new_student["name"]
            student["marks"] = new_student["marks"]
            student["total"] = new_student["total"]
            student["percentage"] = new_student["percentage"]
            student["grade"] = new_student["grade"]
            student["result"] = new_student["result"]
            found = True
            break

    if found:
        save_students(students)
        print("Student record updated successfully.")
    else:
        print("Student not found.")


def delete_student():
    roll_no = input("Enter Roll No to delete: ")
    students = load_students()
    new_students = [student for student in students if student["roll_no"] != roll_no]

    if len(new_students) == len(students):
        print("Student not found.")
    else:
        save_students(new_students)
        print("Student record deleted successfully.")


def main():
    while True:
        print("\n===== Student Course Performance Manager =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()