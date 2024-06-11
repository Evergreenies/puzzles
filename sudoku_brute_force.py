"""
Sudoku Puzzle
"""


def is_valid_move(grid: list[list], row: int, column: int, number: int) -> bool:
    # check if number already exists in current row
    for index in range(9):
        if grid[row][index] == number:
            return False

    # check if number already exists in current column
    for index in range(9):
        if grid[index][column] == number:
            return False

    # check if current number already exists in current 3X3 matrix
    corner_row = row - row % 3
    corner_column = column - column % 3
    for _row in range(3):
        for _col in range(3):
            if grid[corner_row + _row][corner_column + _col] == number:
                return False

    return True


def solve(grid: list[list], row: int, column: int):
    if column == 9:
        if row == 8:
            return True

        row += 1
        column = 0

    if grid[row][column] > 0:
        return solve(grid, row, column + 1)

    for num in range(1, 10):
        if is_valid_move(grid, row, column, num):
            grid[row][column] = num

            if solve(grid, row, column + 1):
                return True

        grid[row][column] = 0

    return False


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0, 6, 8, 0],
        [0, 0, 0, 0, 7, 3, 0, 0, 9],
        [3, 0, 9, 0, 0, 0, 0, 4, 5],
        [4, 9, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 3, 0, 5, 0, 9, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 3, 6],
        [9, 6, 0, 0, 0, 0, 3, 0, 8],
        [7, 0, 0, 6, 8, 0, 0, 0, 0],
        [0, 2, 8, 0, 0, 0, 0, 0, 0],
    ]
    if solve(grid, 0, 0):
        row_count = 0
        for row in range(9):
            column_count = 0
            row_count += 1
            for column in range(9):
                column_count += 1
                print(grid[row][column], end=" ")

                if column_count == 3 and column < 8:
                    print(" | ", end="")
                    column_count = 0

            if row_count == 3 and row < 8:
                print()
                row_count = 0
                print("------   " * 3, end="")

            print()

    else:
        print("No solution for this Sudoku")
