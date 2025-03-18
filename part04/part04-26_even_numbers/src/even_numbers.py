# Write your solution here

def even_numbers(integers: list) -> list:
    new_list = []
    for integer in integers:
        if integer % 2 == 0:
            new_list.append(integer)
    return new_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
