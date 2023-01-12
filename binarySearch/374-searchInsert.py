def searchInsert(self, nums: List[int], target: int) -> int:
  # binary search, mas onde eu colocaria o target se ele não existir?
  # o ponteiro r jamais ficará menor que zero
  # o ponteiro l, pode passar do tamanho do array
  # isso sugere que o ponteiro l indica a posição que o target estaria
  # mas por quê?
  l, r = 0, len(nums) - 1

  while l <= r:
      m = l + ((r - l) // 2)

      if nums[m] > target:
          r = m - 1
      elif nums[m] < target:
          l = m + 1
      else:
          return m
  print(l, r)
  return l