def sort_students(students):
    students.sort(key=lambda student: student.cgpa, reverse=True)
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number  
        self.cgpa = cgpa

# Create a list of student objects
students = [
    Student("Bhavani", "A001", 3.8),
    Student("Preethi", "A002", 3.5),
    Student("Yuvasri", "A003", 3.9),
]

# Sort the list of students based on CGPA
sort_students(students)

# Print the sorted list
for student in students:
    print(student.name, student.roll_number, student.cgpa)