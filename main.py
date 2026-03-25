class Subject:
    def __init__(self, name):
        self.name = name


class Grade:
    def __init__(self, subject, value):
        self.subject = subject
        self.value = value


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades