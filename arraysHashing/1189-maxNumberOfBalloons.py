def maxNumberOfBalloons(self, text: str) -> int:
    balloon = Counter("balloon")
    textMap = Counter(text)
    print(balloon)
    print(textMap)
    ans = float('inf')
    for c in balloon:
        if c in text:
            ans = min(ans, textMap[c] // balloon[c])
        else:
            return 0
    return ans