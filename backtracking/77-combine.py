class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(combination, start):
            if len(combination) >= k:
                ans.append(combination.copy())
                return
            
            for i in range(start, n + 1):
                combination.append(i)
                backtrack(combination, i + 1)
                combination.pop()

        backtrack([], 1)
        return ans

            