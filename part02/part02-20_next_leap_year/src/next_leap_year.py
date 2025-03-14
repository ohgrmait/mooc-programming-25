# Write your solution here

year = int(input("Year: "))

next_leap_year = year
leap_year = False

while True:
  next_leap_year += 1

  if next_leap_year % 100 == 0:
    if next_leap_year % 400 == 0:
      leap_year = True
  elif next_leap_year % 4 == 0:
    leap_year = True
  
  if leap_year:
    break

print(f"The next leap year after {year} is {next_leap_year}")
