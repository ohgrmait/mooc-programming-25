# tee ratkaisu tänne

if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points = "exam_points1.csv"

names = {}

with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        names[parts[0]] = f"{parts[1]} {parts[2].strip()}"

exercises = {}

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        total = []
        for part in parts[1:]:
            total.append(part.strip())
        exercises[parts[0]] = total

points = {}

with open(exam_points) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        points[parts[0]] = parts[1:]

print(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}")

for id, name in names.items():
    exam_total = 0
    for point in points[id]:
        exam_total += int(point)
    exercise_total = 0
    for exercise in exercises[id]:
        exercise_total += int(exercise)
    exercise_points = int(exercise_total / 40 * 100) // 10
    if exam_total + (exercise_points) < 15:
        grade = 0
    elif exam_total + (exercise_points) < 18:
        grade = 1
    elif exam_total + (exercise_points) < 21:
        grade = 2
    elif exam_total + (exercise_points) < 24:
        grade = 3
    elif exam_total + (exercise_points) < 28:
        grade = 4
    else:
        grade = 5
    print(f"{name:30}{exercise_total:<10}{exercise_points:<10}{exam_total:<10}{exam_total+exercise_points:<10}{grade:<10}")
