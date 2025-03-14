# Write your solution here

first = input("1st letter: ")
second = input("2nd letter: ")
third = input("3rd letter: ")

middle = first

if first > second and first > third:
  if second > third:
    middle = second
  else:
    middle = third
elif second > third:
  if third > first:
    middle = third
  else:
    middle = first
else:
  if first > second:
    middle = first
  else:
    middle = second

print(f"The letter in the middle is {middle}")
