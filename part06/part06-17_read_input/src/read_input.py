# Write your solution here

def read_input(prompt, a, b):
    while True:
        try:
            number = int(input(f"{prompt}: "))
            if number >= a and number <= b:
                return number
        except ValueError:
            pass
        print(f"You must type in an integer between {a} and {b}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
