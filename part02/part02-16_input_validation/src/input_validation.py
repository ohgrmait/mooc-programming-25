# Write your solution here

from math import sqrt

while True:
  number = int(input("Please type in a number: "))
  if number == 0:
    break
  elif number < 0:
    print("Invalid number")
  else:
    print(sqrt(number))
print("Exiting...")
