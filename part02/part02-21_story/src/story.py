# Write your solution here

curr_word = ""
prev_word = ""
sentence = ""

while True:
  curr_word = input("Please type in a word: ")
  if curr_word == "end" or curr_word == prev_word:
    break
  prev_word = curr_word
  sentence += curr_word + " "

print(sentence)
