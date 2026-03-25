from collections.abc import Iterable, Iterator

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

class StudentIterator(Iterator):
    def __init__(self, students):
        self._students = sorted(students, key=lambda s: s.grade_math, reverse=True)
        self._index = 0

    def __next__(self):
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student
    
class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __iter__(self):
        return StudentIterator(self.students)
    
    def rank_matter_1(self):
        sorted_students = sorted(self.students, key=lambda s: s.grade_math, reverse=True)
        for student in sorted_students:
            print(student.name, student.grade_math)
    
    def rank_matter_2(self):
        sorted_students = sorted(self.students, key=lambda s: s.grade_english, reverse=True)
        for student in sorted_students:
            print(student.name, student.grade_english)

    def rank_matter_3(self):
        sorted_students = sorted(self.students, key=lambda s: s.grade_science, reverse=True)
        for student in sorted_students:
            print(student.name, student.grade_science)


school_class = SchoolClass()
school_class.add_student(Student('J', 10, 12, 13))
school_class.add_student(Student('A', 8, 2, 17))
school_class.add_student(Student('V', 9, 14, 14))

school_class.rank_matter_1()
school_class.rank_matter_2()
school_class.rank_matter_3()

for student in school_class:
    print(student.name, student.grade_math)