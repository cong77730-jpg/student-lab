from student_manager import Student, StudentManager

def main():
    manager = StudentManager()

    while True:
        print("\n=== QUẢN LÝ SINH VIÊN ===")
        print("1. Thêm sinh viên")
        print("2. Xem danh sách sinh viên")
        print("3. Tìm sinh viên theo ID")
        print("0. Thoát")

        choice = input("Chọn chức năng (0-3): ").strip()

        if choice == "1":
            try:
                s_id = input("Nhập ID: ").strip()
                name = input("Nhập tên: ").strip()
                age = int(input("Nhập tuổi: "))
                gpa = float(input("Nhập GPA (0-10): "))

                student = Student(s_id, name, age, gpa)
                manager.add_student(student)
                print("-> Thêm sinh viên thành công!")
            except ValueError as e:
                print(f"-> Lỗi: {e}")

        elif choice == "2":
            students = manager.get_all()
            if not students:
                print("-> Danh sách sinh viên đang trống.")
            else:
                print("\nDanh sách sinh viên:")
                for s in students:
                    print(s)

        elif choice == "3":
            s_id = input("Nhập ID cần tìm: ").strip()
            student = manager.find_by_id(s_id)
            if student:
                print(f"-> Kết quả: {student}")
            else:
                print("-> Không tìm thấy sinh viên có ID này.")

        elif choice == "0":
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

if __name__ == "__main__":
    main()