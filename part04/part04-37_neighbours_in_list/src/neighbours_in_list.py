# Write your solution here

def longest_series_of_neighbours(numbers: list) -> int:
    longest = 1
    neighbours = 1
    for i in range(len(numbers)-1):
        if abs(numbers[i] - numbers[i+1]) == 1:
            neighbours += 1
        else:
            neighbours = 1
        longest = max(neighbours, longest)
    return longest

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
