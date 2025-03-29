# Write your solution here

def search():
    search_term = input("Search term: ")
    with open("dictionary.txt")as file:
        for row in file:
            parts = row.split(":")
            if search_term in parts[0] or search_term in parts[1].strip():
                print(f"{parts[0]} - {parts[1].strip()}")

def add_word():
    finnish = input("The word in Finnish: ")
    english = input("The word in English: ")
    with open("dictionary.txt", "a") as file:
        file.write(f"{finnish}: {english}\n")
    print("Dictionary entry added")

def main():
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        function = int(input("Function: "))
        if function == 1:
            add_word()
        elif function == 2:
            search()
        elif function == 3:
            # open("dictionary.txt", "w").close()
            print("Bye!")
            break

main()
