# Write your solution here

def palindromes(string: str) -> bool:
    i = 0
    while i < len(string) // 2:
        if string[i] != string[-i-1]:
            return False
        i += 1
    return True

while True:
    word = input("Please type in a palindrome: ")
    if palindromes(word):
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
