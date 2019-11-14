def isIsomorphic(s: str, t: str) -> bool:
    sHashMap, tHashMap = {}, {}

    for index in range(len(s)):
        sHashMap[s[index]] = sHashMap.get(s[index], 0) + 1
        tHashMap[t[index]] = tHashMap.get(t[index], 0) + 1

    sVal = ""
    for i in sHashMap.values():
        print(i)
        sVal = sVal.join(str(i))
    print(sVal)





isIsomorphic("ab", "aa")
