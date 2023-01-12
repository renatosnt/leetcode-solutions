def twoSum(self, nums: List[int], target: int) -> List[int]:
  map = {}

  for i, value in enumerate(nums):
      diff = target - value
      if diff in map:
          return [map[diff], i]
      map[value] = i 