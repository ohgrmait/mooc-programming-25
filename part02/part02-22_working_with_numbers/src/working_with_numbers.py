# Write your solution here

print("Please type in integer numbers. Type in 0 to finish.")

count = 0
total = 0
positives = 0

while True:
  number = int(input("Number: "))
  if number == 0:
    break
  if number > 0:
    positives += 1
  count += 1
  total += number

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {total}")
print(f"The mean of the numbers is {total / count}")
print(f"Positive numbers {positives}")
print(f"Negative numbers {count - positives}")
