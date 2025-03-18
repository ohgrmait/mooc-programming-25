# Write your solution here

def length_of_longest(strings: list) -> int:
    longest = strings[0]
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return len(longest)

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(my_list)
    print(result)
