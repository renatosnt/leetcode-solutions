def maxProfit(self, prices: List[int]) -> int:
  left, right = 0, 1
  
  maxProf = 0
  
  while right < len(prices):
      if prices[left] > prices[right]:
          left = right
          right += 1
      else:
          maxProf = max(prices[right] - prices[left], maxProf)
          right += 1
  return maxProf