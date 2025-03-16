# Write your solution here

number = int(input("Please type in a number: "))

i = 0
while i < number // 2:
  print(i + 1)
  print(number - i)
  i += 1
if number % 2 != 0:
  print(i + 1)
