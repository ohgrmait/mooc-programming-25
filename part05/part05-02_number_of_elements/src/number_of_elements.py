# Write your solution here

def count_matching_elements(my_matrix: list, element: int) -> int:
    count = 0
    for row in my_matrix:
        for e in row:
            if e == element:
                count += 1
    return count

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))
