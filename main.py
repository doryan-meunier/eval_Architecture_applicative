class Subject:
    def __init__(self, name):
        self.name = name


class Grade:
    def __init__(self, subject, value):
        self.subject = subject
        self.value = value


class Student:
    def __init__(self, name, grade_math, grade_english, grade_science):
        self.name = name
        self.grade_math = grade_math
        self.grade_english = grade_english
        self.grade_science = grade_science


class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)


school_class = SchoolClass()
school_class.add_student(Student('J', 10, 12, 13))
school_class.add_student(Student('A', 8, 2, 17))
school_class.add_student(Student('V', 9, 14, 14))