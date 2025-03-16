# Write your solution here

def squared(string, size):
  new_string = string * (size * size)
  i = 0
  while i < size:
    print(new_string[:size])
    new_string = new_string[size:]
    i += 1

if __name__ == "__main__":
  squared("ab", 3)
  print()
  squared("aybabtu", 5)
