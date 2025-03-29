# write your solution here

text = input("Write text: ")

words = []

with open("wordlist.txt") as new_file:
    for line in new_file:
        words.append(line.strip())

desired_text = ""

for word in text.split(" "):
    if word.lower() in words:
        desired_text += word + " "
    else:
        desired_text += "*" + word + "*" + " "

print(desired_text)
