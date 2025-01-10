class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}")

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

# Example usage
student = Student("Alice", 20, [85, 90, 78])
student.display_details()
print(f"Average Grade: {student.average_grade()}")