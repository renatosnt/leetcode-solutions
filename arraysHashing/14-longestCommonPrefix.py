def longestCommonPrefix(self, strs: List[str]) -> str:
  res = ""
  
  for i in range(len(strs[0])): # para cada caractere
      for s in strs: # para cada string
          if i == len(s) or s[i] != strs[0][i]:
              return res
      res += s[i]
  return res