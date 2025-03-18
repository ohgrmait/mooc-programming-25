# Write your solution here

def all_the_longest(strings: list) -> list:
    len_of_longest = len(strings[0])
    for string in strings:
        if len(string) > len_of_longest:
            len_of_longest = len(string)
    new_list = []
    for string in strings:
        if len(string) == len_of_longest:
            new_list.append(string)
    return new_list

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']
