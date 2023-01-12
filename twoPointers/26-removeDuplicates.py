def removeDuplicates(self, nums: List[int]) -> int:
    left = 1
    last = nums[0]

    for i in range(1, len(nums)):
        if nums[i] != last:
            nums[left] = nums[i]
            last = nums[i]
            left += 1
    return left