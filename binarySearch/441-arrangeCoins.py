def arrangeCoins(self, n: int) -> int:
  l, r = 1, n

  while l <= r:
      m = l + (r - l) // 2
      # a soma nos diz se conseguimos usar todas as n moedas
      soma = (1 + m) * (m / 2)

      if soma > n:
          r = m - 1
      elif soma < n:
          l = m + 1
      else:
          # conseguimos usar todas as moedas
          return m
  # se não conseguimos usar todas as moedas, temos uma linha a menos
  return l - 1