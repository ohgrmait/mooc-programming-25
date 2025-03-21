# Write your solution here

def avg_grade(students: dict, name: str) -> float:
    grade = 0
    for courses in students[name]:
        grade += courses[1]
    return grade / len(students[name])

def add_student(students: dict, name: str):
    students[name] = []

def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
    else:
        print(f"{name}:")
        if len(students[name]) == 0:
            print(" no completed courses")
        else:
            print(f" {len(students[name])} completed courses:")
            for courses in students[name]:
                print(f"  {courses[0]} {courses[1]}")
            print(f" average grade {avg_grade(students, name)}")

def add_course(students: dict, name: str, course: tuple):
    if course[1] > 0:
        if len(students[name]) == 0:
            students[name].append(course)
        else:
            course_found = False
            for i in range(len(students[name])):
                if students[name][i][0] == course[0]:
                    course_found = True
                    if students[name][i][1] < course[1]:
                        students[name][i] = course
                    break
            if not course_found:
                students[name].append(course)

def most_courses_completed(students: dict) -> tuple:
    most_completed = 0
    most_completed_student = ""
    for student in students:
        if len(students[student]) > most_completed:
            most_completed = len(students[student])
            most_completed_student = student
    return most_completed, most_completed_student

def best_average_grade(students: dict) -> float:
    best_grade = 0.0
    best_student = ""
    for student in students:
        grade = 0.0
        for courses in students[student]:
            grade += courses[1]
        grade /= len(students[student])
        if grade > best_grade:
            best_grade = grade
            best_student = student
    return best_grade, best_student

def summary(students: dict):
    print(f"students {len(students)}")
    print(f"most courses completed {most_courses_completed(students)[0]} {most_courses_completed(students)[1]}")
    print(f"best average grade {best_average_grade(students)[0]} {best_average_grade(students)[1]}")

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
