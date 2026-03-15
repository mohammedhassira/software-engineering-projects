# Simple Student Management System

students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        students[name] = grade

    elif choice == "2":
        for name, grade in students.items():
            print(name, ":", grade)

    elif choice == "3":
        break

    else:
        print("Invalid choice")
