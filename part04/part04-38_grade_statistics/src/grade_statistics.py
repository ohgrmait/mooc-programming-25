# Write your solution here

def get_grades(exam_points: list, exercise_points: list) -> list:
    grades = []
    total_points = []
    for i in range(len(exam_points)):
        total_points.append(exam_points[i] + exercise_points[i])
    for i in range(len(total_points)):
        if exam_points[i] < 10:
            grade = 0
        elif exam_points[i] >= 10:
            if total_points[i] < 15:
                grade = 0
            elif total_points[i] < 18:
                grade = 1
            elif total_points[i] < 21:
                grade = 2
            elif total_points[i] < 24:
                grade = 3
            elif total_points[i] < 28:
                grade = 4
            elif total_points[i] < 31:
                grade = 5
        grades.append(grade)
    return grades

def get_pass_percentage(exam_points: list, exercise_points: list) -> float:
    total_points = []
    for i in range(len(exam_points)):
        total_points.append(exam_points[i] + exercise_points[i])
    passed = 0
    for i in range(len(total_points)):
        if total_points[i] >= 15 and exam_points[i] >= 10:
            passed += 1
    return round((passed/len(total_points)) * 100, 1)

def get_points_average(exam_points: list, exercise_points: list) -> float:
    total_points = []
    for i in range(len(exam_points)):
        total_points.append(exam_points[i] + exercise_points[i])
    return sum(total_points) / len(total_points)

def get_exercise_points(exercises_completed: list) -> list:
    exercise_points = []
    for exercises in exercises_completed:
        exercise_points.append(exercises // 10)
    return exercise_points

def print_stars(grades: list, index: int) -> str:
    if grades.count(index) > 0:
        return "*" * grades.count(index)
    return ""

def main():
    exam_points = []
    exercises_completed = []
    while True:
        user_input = input("Exam points and exercises completed: ")
        if user_input == "":
            break
        exam_points.append(int(user_input.split()[0]))
        exercises_completed.append(int(user_input.split()[1]))
    exercise_points = get_exercise_points(exercises_completed)
    print("Statistics:")
    print(f"Points average: {get_points_average(exam_points, exercise_points)}")
    print(f"Pass percentage: {get_pass_percentage(exam_points, exercise_points)}")
    print("Grade distribution:")
    grades = get_grades(exam_points, exercise_points)
    i = 5
    while i >= 0:
        print(f"{i}: {print_stars(grades, i)}")
        i -= 1

main()
