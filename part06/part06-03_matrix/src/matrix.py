# write your solution here

def matrix_sum() -> int:
    with open("matrix.txt") as file:
        grand_total = 0
        for line in file:
            total = 0
            line = line.replace("\n", "")
            parts = line.split(",")
            for part in parts:
                total += int(part)
            grand_total += total
    return grand_total

def matrix_max() -> int:
    with open("matrix.txt") as file:
        all_numbers = []
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(",")
            for part in parts:
                all_numbers.append(int(part))
    return max(all_numbers)

def row_sums() -> list:
    with open("matrix.txt") as file:
        row_totals = []
        for line in file:
            total = 0
            line = line.replace("\n", "")
            parts = line.split(",")
            for part in parts:
                total += int(part)
            row_totals.append(total)
    return row_totals
