# Write your solution here

word = input("Please type in a word: ")
char = input("Please type in a character: ")

while True:
  index = word.find(char)
  if index == -1 or len(word) < index + 3:
    break
  print(word[index: index + 3])
  word = word[index + 1:]
