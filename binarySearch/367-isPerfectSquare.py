
def isPerfectSquare(self, num: int) -> bool:
  l, r = 1, num

  while l <= r:
      mid = l + (r - l) // 2
      square = mid * mid

      if square > num:
          r = mid - 1
      elif square < num:
          l = mid + 1
      else:
          return True
  return False
