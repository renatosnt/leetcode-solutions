class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(subset, i):
            if i >= len(nums):
                ans.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(subset, i + 1)
            subset.pop()
            backtrack(subset, i + 1)
        
        backtrack([], 0)
        return ans