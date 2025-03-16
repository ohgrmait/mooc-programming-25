# Write your solution here

limit = int(input("Limit: "))

i = 1
total = 0
sentence = "The consecutive sum:"

while total < limit:
  total += i
  if total >= limit:
    sentence += f" {i}"
  else:
    sentence += f" {i} +"
  i += 1

sentence += f" = {total}"
print(sentence)
