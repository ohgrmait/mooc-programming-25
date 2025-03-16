# Write your solution here

word = input("Word: ")

stars = "*" * 30
spaces = " " * ((30 - 2 - len(word)) // 2)

print(stars)
if len(word) % 2 == 0:
  print("*" + spaces + word + spaces + "*")
else:
  print("*" + spaces + word + spaces + " " + "*")
print(stars)
