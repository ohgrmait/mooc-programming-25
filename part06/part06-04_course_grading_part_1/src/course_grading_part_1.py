# write your solution here

if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

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

for id, name in names.items():
    exercise_total = 0
    for exercise in exercises[id]:
        exercise_total += int(exercise)
    print(f"{name} {exercise_total}")
