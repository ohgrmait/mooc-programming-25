# Write your solution here

def add(phonebook: dict):
    name = input("name: ")
    number = input("number: ")
    if name not in phonebook:
        phonebook[name] = [number]
    else:
        phonebook[name].append(number)
    print("ok!")

def search(phonebook: dict):
    name = input("name: ")
    if name in phonebook:
        for number in phonebook[name]:
            print(number)
    else:
        print("no number")

def main():
    phonebook = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))
        if command == 1:
            search(phonebook)
        elif command == 2:
            add(phonebook)
        elif command == 3:
            print("quitting...")
            break

main()
