# Write your solution here

limit = int(input("Upper limit: "))

i = 0
while (2 ** i) <= limit:
  print(2 ** i)
  i += 1
