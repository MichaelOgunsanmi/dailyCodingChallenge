# Source: 2020 Goldman Sachs Engineering Code test

# Level: Medium

# Date: 17th July, 2019

def play(inputArray):
    optimalArray = []
    rows = len(inputArray)
    columns = len(inputArray[0])

    for column in range(columns):
        for row in range(rows):
            if row == 0:
                maxValue = float('-inf')

            if inputArray[row][column] > maxValue:
                maxValue = inputArray[row][column]

        optimalArray.append(maxValue)

    optimalArray.sort(reverse=True)

    jerryScore = 0
    tomScore = 0

    for index, value in enumerate(optimalArray):
        if index % 2 == 0:
            jerryScore += value
        else:
            tomScore += value

    return jerryScore - tomScore


print(play([[3, 7, 5, 3, 4, 5],
      [4, 5, 2, 6, 4, 5],
      [7, 4, 9, 7, 8, 3]]))

# find the optimal score from picking a value from each column
# ans = 3

