# Source: 2020 Goldman Sachs Engineering Code test

# Level: Medium

# Date: 17th July 2019

def rotateTheString(originalString, direction, amount):
    stringLength = len(originalString)

    for index, value in enumerate(amount):
        if direction[index] == 1:
            rotationPoint = value % stringLength
        else:
            rotationPoint = stringLength % value
        originalString = originalString[-rotationPoint:] + originalString[:len(originalString) - rotationPoint]
    return originalString


print(rotateTheString('hurart', [0, 1], [4, 1]))
# 0 is left rotation, 1 is right rotation and direction[i] * amount [i] is number of ith iteration
# ans = arthur
