class Student:
<<<<<<< HEAD
    def __init__(self, student_id, name, age, gpa):
=======
    """Lớp đại diện cho đối tượng Sinh viên."""
    def __init__(self, student_id: str, name: str, age: int, gpa: float):
>>>>>>> 3996c7a980b93254f92ce6692bc2f733086e46aa
        if not (0 <= gpa <= 10):
            raise ValueError("GPA phải từ 0 đến 10")
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gpa = gpa

<<<<<<< HEAD
    def __str__(self):
=======
    def __str__(self) -> str:
>>>>>>> 3996c7a980b93254f92ce6692bc2f733086e46aa
        return f"ID: {self.student_id} | Tên: {self.name} | Tuổi: {self.age} | GPA: {self.gpa}"


class StudentManager:
<<<<<<< HEAD
    def __init__(self):
        self.students = []

    def add_student(self, student):
=======
    """Lớp quản lý danh sách sinh viên."""
    def __init__(self):
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
>>>>>>> 3996c7a980b93254f92ce6692bc2f733086e46aa
        if self.find_by_id(student.student_id):
            raise ValueError(f"ID {student.student_id} đã tồn tại!")
        self.students.append(student)

<<<<<<< HEAD
    def get_all(self):
        return self.students

    def find_by_id(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None
=======
    def get_all(self) -> list[Student]:
        return self.students

    def find_by_id(self, student_id: str) -> Student | None:
        return next((s for s in self.students if s.student_id == student_id), None)
>>>>>>> 3996c7a980b93254f92ce6692bc2f733086e46aa
    def update_gpa(self, student_id: str, new_gpa: float) -> bool:
     student = self.find_by_id(student_id)
     if student and 0 <= new_gpa <= 10:
         student.gpa = new_gpa
         return True
     return False