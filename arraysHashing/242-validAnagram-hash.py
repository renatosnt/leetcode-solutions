def isAnagram(self, s: str, t: str) -> bool:
    # s and t are anagrams if and only if they have the same characters in the same amount
    if len(s) != len(t): return False

    countS = {}
    countT = {}

    for i in range(len(s)):
        #countS.get(s[i]) does the same as countS[s[i]], but it has a second paramter that returns a default value if the key doesn't exist
        countS[s[i]] = countS.get(s[i], 0) + 1
        countT[t[i]] = countT.get(t[i], 0) + 1
    return countS == countT