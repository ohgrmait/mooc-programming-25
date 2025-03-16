# Write your solution here

string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

index = string.find(substring, string.find(substring) + len(substring))
if index != -1:
  print(f"The second occurrence of the substring is at index {index}.")
else:
  print(f"The substring does not occur twice in the string.")
