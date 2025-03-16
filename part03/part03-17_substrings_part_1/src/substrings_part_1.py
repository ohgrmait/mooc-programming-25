# Write your solution here

string = input("Please type in a string: ")

index = 0
while index < len(string):
  print(string[0: index + 1])
  index += 1
