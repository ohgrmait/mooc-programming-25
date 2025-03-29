# Write your solution here

def add():
    entry = input("Dairy entry: ")
    with open("diary.txt", "a") as file:
        file.write(entry + "\n")
    print("Diary saved")

def read():
    print("Entries:")
    with open("diary.txt") as file:
        for row in file:
            print(row.strip())

def main():
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        function = int(input("Function: "))
        if function == 1:
            add()
            print()
        elif function == 2:
            read()
        elif function == 0:
            print("Bye now!")
            break

main()
