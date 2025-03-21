# Write your solution here

layers = int(input("Layers: "))

rows = layers*2 - 1
char = "A"

for i in range(rows):
    y = abs(layers-1-i)
    for j in range(rows):
        x = abs(layers-1-j)
        if x > y:
            print(chr(ord(char) + x), end="")
        else:
            print(chr(ord(char) + y), end="")
    print()
