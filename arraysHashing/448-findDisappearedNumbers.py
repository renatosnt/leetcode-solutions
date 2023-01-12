def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    ans = set()
    checkNums = set(nums)
    allNumbers = [*range(1, len(nums) + 1)]

    for n in allNumbers:
        if n not in checkNums:
            ans.add(n)
    return list(ans)