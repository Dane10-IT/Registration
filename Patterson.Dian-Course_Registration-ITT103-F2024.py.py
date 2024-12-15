
#registration menu
class RegistrationMethod:
    def __init__(self):
        self.students={}
        self.courses = {}

#new course added to the registry
    def add_course(self, course_id,name,fee):
        course=Course(course_id,name,fee)
        self.courses[course_id]=course
        print(f"Course{course.name} added to the registry.")

#add new student to the registry
    def register_student(self,student_id,name,email,balance):
        student=Student(student_id,name,email,balance)
        self.students[student_id]=student
        print(f"Student {name} registered successfully.")

#student_name=(input(print("Please enter your name:")))
#student_id=(input(print("Please enter your student_id:")))

#to enroll students into a course
    def enroll_in_course(self,student_id,course_id):
        student=self.students.get(student_id)
        course=self.courses.get(course_id)
        if student and course:
            student.enroll(course)
        else:
            print(f"Invalid student ID{student_id} or course ID {course_id}")

#calaculating students balance
    def calculate_payment(self,student_id):
        student=self.students.get(student_id)
        if  not student:
           print(f"Student with ID {student_id} not found.")
           return
        balance=student.balance
        if balance > 0:
            min_payment=0.4 * balance #must be 40% of course fee
            print(f"Student {student.name} is required to pay {min_payment}.")
            payment = float(input("Enter payment amount:"))
            if payment >= min_payment:
                student.balance-=payment
                print(f"Payment was successful. Remaining balance:{student.balance}.")
            else:
              print(f"Payment was insufficient. Minimum 40% is required.")
        else:
             print(f"Student {student.name} has no outstanding balance.")

#To check balance for students
    def check_student_balance(self,student_id):
           student=self.students.get(student_id),
           if student:
              print(f"Student {student.name}'s current balance is: {student.balance}.")
           else:
               print(f"Student with ID {student_id} not found.")

#method to show a list of all the available course
    def show_courses(self):
        if not self.courses:
            print("No courses available at this time.")
        else:
           for course in self.courses.values():
            print(f"Course Name ={course.name} ,Course ID={course.id}, Fee={course.fee}")

    def show_register_student(self):
         if not self.students:
            print("No student registered.")
         else:
             for student in self.students.values():
              print(f"Student ID ={student.id} Name={student.name} Email={student.email}")

#method to show all the courses listed
    def show_students_in_course(self,course_id):
        course=self.courses.get (course_id)
        if not course:
            print(f"No course found with ID {course_id}.")
            return
        enrolled_students= [student for student in self.students.values() if course in student.courses]
        if not enrolled_students:
            print(f"No students are enrolled in course {course.name}.")
        else:
            for student in enrolled_students:
             print(f"Student ID: {student.id}, Name: {student.name}, Email: {student.email}.")

def main():
    reg_system = RegistrationMethod()

    # Loop to show menu and handle user input
    while True:
        print("\nMenu, Course Registry")
        print("1. Register a student.")
        print("2. Add a course.")
        print("3. Show courses.")
        print("4. Enroll students in courses.")
        print("5. Show registered students.")
        print("6. Show students in course.")
        print("7. Calculate Payment.")
        print("8. Check student's balance.")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            email = input("Enter Student Email: ")
            balance = float(input("Enter Student Balance: "))
            reg_system.register_student(student_id, name, email, balance)

        elif choice == '2':
            course_id = input("Enter Course ID: ")
            name = input("Enter Course Name: ")
            fee = float(input("Enter Course Fee: "))
            reg_system.add_course(course_id, name, fee)

        elif choice == '3':
            reg_system.show_courses()

        elif choice == '4':
            student_id = input("Enter Student ID: ")
            course_id = input("Enter Course ID: ")
            reg_system.enroll_in_course(student_id, course_id)

        elif choice == '5':
            reg_system.show_register_student()

        elif choice == '6':
            course_id = input("Enter Course ID: ")
            reg_system.show_students_in_course(course_id)

        elif choice == '7':
            student_id = input("Enter Student ID: ")
            reg_system.calculate_payment(student_id)

        elif choice == '8':
            student_id = input("Enter Student ID: ")
            reg_system.check_student_balance(student_id)

        elif choice == '9':
            print("Goodbye")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__": main()