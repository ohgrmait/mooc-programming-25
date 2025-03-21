# Write your solution here

phonebook = {}

def add(name: str, number: str):
    phonebook[name] = number
    print("ok!")

def search(name: str) -> str:
    if name in phonebook:
        return phonebook[name]
    return "no number"

def main():
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))
        if command == 1:
            name = input("name: ")
            print(search(name))
        elif command == 2:
            name = input("name: ")
            number = input("number: ")
            add(name, number)
        elif command == 3:
            print("quitting...")
            break

main()
