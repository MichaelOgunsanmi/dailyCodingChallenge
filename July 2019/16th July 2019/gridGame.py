# Source: 2020 Goldman Sachs Engineering Code test

# Level: Medium

# Date: 16th July 2019

# Complete the 'gridGame' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY grid
#  2. INTEGER k
#  3. STRING_ARRAY rules


def gridGame(grid, k, rules):
    indexes = {}
    for index, rule in enumerate(rules):
        if rule == 'alive':
            indexes[index] = 1

    rows = len(grid)
    columns = len(grid[0])

    updatedBoard = [[0] * columns for i in range(rows)]

    for step in range(k):
        for row in range(rows):
            for column in range(columns):
                count = 0
                if row - 1 >= 0:
                    if grid[row - 1][column] == 1:
                        count += 1
                    if column - 1 >= 0 and grid[row - 1][column - 1] == 1:
                        count += 1
                    if column + 1 < columns and grid[row - 1][column + 1] == 1:
                        count += 1

                if row + 1 < rows:
                    if grid[row + 1][column] == 1:
                        count += 1
                    if column - 1 >= 0 and grid[row + 1][column - 1] == 1:
                        count += 1
                    if column + 1 < columns and grid[row + 1][column + 1] == 1:
                        count += 1

                if column + 1 < columns and grid[row][column + 1] == 1:
                    count += 1

                if column - 1 >= 0 and grid[row][column - 1] == 1:
                    count += 1
                updatedBoard[row][column] = count
                count = 0

        for row in range(rows):
            for column in range(columns):
                if updatedBoard[row][column] in indexes:
                    updatedBoard[row][column] = 1
                else:
                    updatedBoard[row][column] = 0
        grid = updatedBoard
        updatedBoard = [[0] * columns for i in range(rows)]

    return grid


ans = gridGame([[0, 1, 1, 0], [1, 1, 0, 0]], 2,
               ['dead', 'dead', 'dead', 'alive', 'dead', 'alive', 'dead', 'dead', 'dead'])
print(ans)  # [[0, 1, 1, 0], [1, 1, 0, 0]]
