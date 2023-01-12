def majorityElement(self, nums: List[int]) -> int:
    majoritySize = math.floor(len(nums) / 2)
    count = {}

    for num in nums:
        count[num] = 0
    
    for num in nums:
        count[num] += 1
    
    max = -1
    majority = -1
    for c in count:
        if count[c] > max and count[c] > majoritySize:
            max = count[c]
            majority = c
    return majority
