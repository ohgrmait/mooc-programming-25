# Write your solution here

def shortest(strings: list) -> str:
    shortest = strings[0]
    for string in strings:
        if len(string) < len(shortest):
            shortest = string
    return shortest

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)
