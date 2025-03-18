# Write your solution here

def distinct_numbers(integers: list) -> list:
    new_list = []
    for integer in sorted(integers):
        if integer in new_list:
            continue
        new_list.append(integer)
    return new_list

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]
