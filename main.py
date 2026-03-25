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


class StudentWithHistory(Student):
    def __init__(self, student, grade_history):
        super().__init__(student.name, student.grade_math, student.grade_english, student.grade_science)
        self.grade_history = grade_history


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


class StudentIterator2(Iterator):
    def __init__(self, students):
        self._students = sorted(students, key=lambda s: s.grade_english, reverse=True)
        self._index = 0

    def __next__(self):
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student


class StudentIterator3(Iterator):
    def __init__(self, students):
        self._students = sorted(students, key=lambda s: s.grade_science, reverse=True)
        self._index = 0

    def __next__(self):
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student


class StudentIterator4(Iterator):
    def __init__(self, students):
        self._students = sorted(students, key=lambda s: s.grade_history, reverse=True)
        self._index = 0

    def __next__(self):
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student


class SchoolClass(Iterable):
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


class SchoolClassWithHistory(SchoolClass):
    def __init__(self, school_class):
        super().__init__()
        self.students = school_class.students

    def get_iterator_4(self):
        return StudentIterator4(self.students)


school_class = SchoolClass()
school_class.add_student(StudentWithHistory(Student('J', 10, 12, 13), 15))
school_class.add_student(StudentWithHistory(Student('A', 8, 2, 17), 11))
school_class.add_student(StudentWithHistory(Student('V', 9, 14, 14), 7))

for student in school_class:
    print(student.name, student.grade_math)

for student in StudentIterator2(school_class.students):
    print(student.name, student.grade_english)

for student in StudentIterator3(school_class.students):
    print(student.name, student.grade_science)

school_class_with_history = SchoolClassWithHistory(school_class)
for student in school_class_with_history.get_iterator_4():
    print(student.name, student.grade_history)