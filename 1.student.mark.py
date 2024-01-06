def input_students():
    while True:
        try:
            num_students = int(input("Please enter the number of students in the class: "))
            if num_students < 0:
                print("Number of students cannot be negative. Please try again.")
            else:
                return num_students
        except ValueError:
            print("Invalid input. Please enter a number.")

def input_student_info(num_students):
    students = []
    for i in range(num_students):
        student = {}
        student['id'] = input("Enter student's ID: ")
        student['name'] = input("Enter student's name: ")
        student['dob'] = input("Enter student's date of birth (format: dd-mm-yyyy): ")
        students.append(student)
    return students
def input_courses():
    while True:
        try:
            num_courses = int(input("Please enter the number of courses: "))
            if num_courses < 0:
                print("Number of courses cannot be negative. Please try again.")
            else:
                return num_courses
        except ValueError:
            print("Invalid input. Please enter a number.")

def input_course_info(num_courses):
    courses = []
    for i in range(num_courses):
        course = {}
        course['id'] = input("Enter course's ID: ")
        course['name'] = input("Enter course's name: ")
        courses.append(course)
    return courses
def input_marks(courses, students):
    course_id = input("Enter the ID of the course you want to input marks for: ")
    for course in courses:
        if course['id'] == course_id:
            for student in students:
                print(f"Enter the marks for student {student['name']} (ID: {student['id']}) in course {course['name']} (ID: {course['id']}):")
                marks = input()
                if 'marks' not in student:
                    student['marks'] = {}
                student['marks'][course['id']] = marks

num_students = input_students()
students = input_student_info(num_students)
num_courses = input_courses()
courses = input_course_info(num_courses)
input_marks(courses, students)

def list_courses(courses):
    print("List of courses:")
    for course in courses:
        print(f"Course ID: {course['id']}, Name: {course['name']}")

def list_students(students):
    print("List of students:")
    for student in students:
        print(f"Student ID: {student['id']}, Name: {student['name']}, Date of Birth: {student['dob']}")

def show_student_marks(course_id, courses, students):
    print(f"Marks for course ID: {course_id}")
    for course in courses:
        if course['id'] == course_id:
            for student in students:
                if course_id in student['marks']:
                    print(f"Student ID: {student['id']}, Name: {student['name']}, Marks: {student['marks'][course_id]}")


list_courses(courses)
list_students(students)
course_id = input("Enter the ID of the course you want to see marks for: ")
show_student_marks(course_id, courses, students)
def main():
    students = []
    courses = []

    while True:
        print("""
    0. Exit
    1. Input students
    2. Input student info
    3. Input courses
    4. Input course info
    5. Input marks
    """)
        option = int(input("Your choice: "))
        if option == 0:
            break
        elif option == 1:
            num_students = input_students()
        elif option == 2:
            students = input_student_info(num_students)
        elif option == 3:
            num_courses = input_courses()
        elif option == 4:
            courses = input_course_info(num_courses)
        elif option == 5:
            input_marks(courses, students)
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
