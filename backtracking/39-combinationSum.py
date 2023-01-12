class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(comb, i, total):
                if total > target or i == len(candidates):
                    return

                if total == target:
                    ans.append(comb.copy())
                    return
                
                
                comb.append(candidates[i])
                backtrack(comb, i, total+candidates[i])
                comb.pop()
                backtrack(comb, i + 1, total)

                    
        backtrack([], 0, 0)
        return ans
