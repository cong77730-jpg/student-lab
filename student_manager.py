class Student:
    def __init__(self, student_id, name, age, gpa):
        if not (0 <= gpa <= 10):
            raise ValueError("GPA phải từ 0 đến 10")
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gpa = gpa

    def __str__(self):
        return f"ID: {self.student_id} | Tên: {self.name} | Tuổi: {self.age} | GPA: {self.gpa}"


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if self.find_by_id(student.student_id):
            raise ValueError(f"ID {student.student_id} đã tồn tại!")
        self.students.append(student)

    def get_all(self):
        return self.students

    def find_by_id(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None