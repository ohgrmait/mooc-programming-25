# Write your solution here

def print_sudoku(sudoku: list):
    for i in range(len(sudoku)):
        if i % 3 == 0:
            print()
        for j in range(len(sudoku[i])):
            if j != 0 and j % 3 == 0:
                print(" ", end="")
            if sudoku[i][j] > 0:
                print(f"{sudoku[i][j]} ", end="")
            else:
                print(f"_ ", end="")
        print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) -> list:
    sudoku_copy = []
    for i in range(len(sudoku)):
        sudoku_copy_row = []
        for j in range(len(sudoku[i])):
            sudoku_copy_row.append(sudoku[i][j])
        sudoku_copy.append(sudoku_copy_row)
    sudoku_copy[row_no][column_no] = number
    return sudoku_copy

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
