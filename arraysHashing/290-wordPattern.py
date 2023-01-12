def wordPattern(self, pattern: str, s: str) -> bool:
    mapCW = {}
    mapWC = {}
    words = s.split()
    print(words)
    if len(pattern) != len(words):
        return False
    for c, word in zip(pattern, words):
        print(c, word)

        if (c in mapCW and mapCW[c] != word )or \
            (word in mapWC and mapWC[word] != c):
            return False

        mapCW[c] = word
        mapWC[word] = c
    print(mapCW, mapWC)
    return True