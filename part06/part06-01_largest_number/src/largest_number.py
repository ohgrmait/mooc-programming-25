# write your solution here

def largest() -> int:
    numbers = []
    with open("numbers.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            numbers.append(int(line))
    return max(numbers)
