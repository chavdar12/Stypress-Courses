class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{type(self).__name__}({self.name}, {self.age})"


class Teacher(SchoolMember):
    def __init__(self, name, age, salary, courses=None):
        super().__init__(name, age)
        self.salary = salary
        self.courses = courses or []


class Student(SchoolMember):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.courses = {}  # course -> {"year": int, "grades": [..]}

    def enroll(self, course, year):
        self.courses[course] = {"year": year, "grades": []}

    def add_grade(self, course, grade):
        self.courses[course]["grades"].append(grade)


teacher = Teacher("Ivan", 45, 2500, ["Python"])
student = Student("Maria", 20)
student.enroll("Python", 2022)
student.add_grade("Python", 6)
assert student.courses == {"Python": {"year": 2022, "grades": [6]}}
assert isinstance(teacher, SchoolMember) and teacher.courses == ["Python"]

if __name__ == "__main__":
    print(teacher, teacher.salary, teacher.courses)
    print(student, student.courses)
