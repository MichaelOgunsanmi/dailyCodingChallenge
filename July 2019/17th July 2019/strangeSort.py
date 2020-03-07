# Source: 2020 Goldman Sachs Engineering Code test

# Level: Medium

# Date: 17th July 2019, 2019

def ans(mappings, nums):
    hashMap = {}
    sortedArray = []

    for index, value in enumerate(mappings):
        hashMap[value] = index

    for index, num in enumerate(nums):
        newNum = ''
        for element in num:
            newNum += str(hashMap[int(element)])
        sortedArray.append([int(newNum), index, num])

    sortedArray.sort()
    output = []
    for values in sortedArray:
        output.append(values[2])

    return output


print(ans([2, 1, 4, 8, 6, 3, 0, 9, 7, 5], ['12', '02', '4', '023', '65', '83', '224', '50']))
# sort in ascending order after mapping ['4', '224', '12', '83', '65', '02', '50', '023']
