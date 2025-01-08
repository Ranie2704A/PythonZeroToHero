class Student:
    def __init__(self, name, age, course, score):
        self.name = name
        self.age = age
        self.course = course
        self.score = score

    def __str__(self):
        return f'{self.name}, {self.age}, {self.course}, {self.score}'


    def is_approved(self):
        if self.score >= 5:
            return True
        else:
            return False