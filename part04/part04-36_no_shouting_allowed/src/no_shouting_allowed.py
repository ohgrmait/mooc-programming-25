# Write your solution here

def no_shouting(strings: list) -> list:
    new_list = []
    for string in strings:
        if string.isupper():
            continue
        new_list.append(string)
    return new_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
