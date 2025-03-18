# Write your solution here

def most_common_character(string: str) -> str:
    uniq_str_list = []
    for char in string:
        if char not in uniq_str_list:
            uniq_str_list.append(char)
    occurrences = []
    for char in uniq_str_list:
        occurrences.append(string.count(char))
    return uniq_str_list[occurrences.index(max(occurrences))]

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
