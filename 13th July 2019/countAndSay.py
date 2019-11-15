def countAndSay(n: int) -> str:
    if n == 1:
        return "1"

    i = 0
    prev = "1"
    while i <= n-1:
        i += 1
        output = ""
        j = 0
        count = 0
        while j < len(prev):
            if j == len(prev) - 1:
                num = prev[j]
                count += 1

            if j+1 != len(prev) and prev[j] == prev[j+1]:
                count += 1
                num = prev[j]
                j += 1
                continue
            else:
                num = prev[j]
                count = 1
            k = 0
            while k < count:
                k += 1
                print(output)
                output = output.join(["1"])
            print(output,55,num)
            output = output.join(["1"])
            print('get here')
            print(output)
            count = 0
            j += 1
        prev = output
        # print(prev)
        # print(output)

    return output

countAndSay(4)


