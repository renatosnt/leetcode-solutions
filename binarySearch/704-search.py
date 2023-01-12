def search(self, nums: List[int], target: int) -> int:
  l, r = 0, len(nums) - 1

  while l <= r:

      m = l + ((r - l) // 2)
      if nums[m] > target:
          #primeira metade
          r = m - 1
      elif nums[m] < target:
          # segunda metade
          l = m + 1
      else:
          return m
  return -1