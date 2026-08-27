import unittest
from student_manager import Student, StudentManager

class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.manager = StudentManager()

    def test_add_student_success(self):
        s = Student("SV01", "An", 20, 8.5)
        self.manager.add_student(s)
        self.assertEqual(len(self.manager.get_all()), 1)

    def test_invalid_gpa(self):
        with self.assertRaises(ValueError):
            Student("SV02", "Binh", 20, 11.0)

    def test_duplicate_id(self):
        s1 = Student("SV01", "An", 20, 8.5)
        s2 = Student("SV01", "Binh", 21, 7.0)
        self.manager.add_student(s1)
        with self.assertRaises(ValueError):
            self.manager.add_student(s2)

if __name__ == "__main__":
    unittest.main()