FILE_NAME = "students.txt"

def add_student():
    id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Course: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{id},{name},{age},{course}\n")

    print("✅ Student added successfully!\n")


def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()
            if not students:
                print("No student records found.\n")
                return
            print("\nID | Name | Age | Course")
            print("-" * 30)
            for student in students:
                print(student.replace(",", " | ").strip())
            print()
    except FileNotFoundError:
        print("No student records found.\n")


def search_student():
    search_id = input("Enter Student ID to search: ")
    found = False

    with open(FILE_NAME, "r") as file:
        for student in file:
            if student.startswith(search_id + ","):
                print("🎯 Student Found:")
                print(student.replace(",", " | "))
                found = True
                break

    if not found:
        print("❌ Student not found.\n")


def update_student():
    search_id = input("Enter Student ID to update: ")
    updated = False
    students = []

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    with open(FILE_NAME, "w") as file:
        for student in students:
            if student.startswith(search_id + ","):
                name = input("Enter New Name: ")
                age = input("Enter New Age: ")
                course = input("Enter New Course: ")
                file.write(f"{search_id},{name},{age},{course}\n")
                updated = True
            else:
                file.write(student)

    if updated:
        print("✅ Student updated successfully!\n")
    else:
        print("❌ Student not found.\n")


def delete_student():
    search_id = input("Enter Student ID to delete: ")
    deleted = False
    students = []

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    with open(FILE_NAME, "w") as file:
        for student in students:
            if student.startswith(search_id + ","):
                deleted = True
            else:
                file.write(student)

    if deleted:
        print("🗑 Student deleted successfully!\n")
    else:
        print("❌ Student not found.\n")


def main():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")


main()
