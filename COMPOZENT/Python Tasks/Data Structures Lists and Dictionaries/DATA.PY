def student_data_crud():
    students = {}

    while True:
        action = input("Choose an action: [add, view, update, delete, exit]: ").lower()
        
        if action == 'add':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grades = list(map(float, input("Enter student grades separated by space: ").split()))
            students[name] = {'age': age, 'grades': grades}
        
        elif action == 'view':
            for name, info in students.items():
                print(f"Name: {name}, Age: {info['age']}, Grades: {info['grades']}")
        
        elif action == 'update':
            name = input("Enter the name of the student to update: ")
            if name in students:
                age = int(input("Enter new age: "))
                grades = list(map(float, input("Enter new grades separated by space: ").split()))
                students[name] = {'age': age, 'grades': grades}
            else:
                print("Student not found.")
        
        elif action == 'delete':
            name = input("Enter the name of the student to delete: ")
            if name in students:
                del students[name]
                print(f"Deleted student {name}.")
            else:
                print("Student not found.")
        
        elif action == 'exit':
            break
        
        else:
            print("Invalid action. Please try again.")

student_data_crud()