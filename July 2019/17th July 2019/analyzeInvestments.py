# Source: 2020 Goldman Sachs Engineering Code test

# Level: Medium

# Date: 17th July 2019

def analyzeInvestments(stringInput):  # O(n^2)
    hashMap = {}
    count = 0
    for index, value in enumerate(stringInput):
        if index + 3 > len(stringInput):
            break
        hashMap[value] = index
        for index2, otherValues in enumerate(stringInput[index + 1:]):
            if otherValues in hashMap:
                continue
            hashMap[otherValues] = index2 + index + 1
            if 'A' in hashMap and 'B' in hashMap and 'C' in hashMap:
                count += len(stringInput) - max(hashMap['A'], hashMap['B'], hashMap['C'])
                break

        hashMap = {}

    return count


def analyzeInvestments2(stringInput):  # O(n)
    count = 0
    companiesIndexes = [[], [], [], []]
    for index, value in enumerate(stringInput):
        if value == 'A':
            companiesIndexes[0].append(index)
        elif value == 'B':
            companiesIndexes[1].append(index)
        elif value == 'C':
            companiesIndexes[2].append(index)
        else:
            companiesIndexes[3].append(index)

    while True:
        if len(companiesIndexes[0]) == 0 or len(companiesIndexes[1]) == 0 or len(companiesIndexes[2]) == 0:
            return count

        minIndexA = companiesIndexes[0][0]
        minIndexB = companiesIndexes[1][0]
        minIndexC = companiesIndexes[2][0]
        minIndexOthers = float('inf')
        if len(companiesIndexes[3]) != 0:
            minIndexOthers = companiesIndexes[3][0]
            minVal = min(minIndexA, minIndexB, minIndexC, minIndexOthers)
        else:
            minVal = min(minIndexA, minIndexB, minIndexC)

        if minVal == minIndexOthers:
            count += 1
        else:
            count += len(stringInput) - max(minIndexA, minIndexB, minIndexC)

        if minVal == minIndexA:
            companiesIndexes[0].pop(0)
        if minVal == minIndexB:
            companiesIndexes[1].pop(0)
        if minVal == minIndexC:
            companiesIndexes[2].pop(0)
        if minIndexOthers and minVal == minIndexOthers:
            companiesIndexes[3].pop(0)


print(analyzeInvestments('ABCCBA'), analyzeInvestments2('ABCCBA'))
