class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def backtrack(permutation, i):
            if len(permutation) == len(nums):
                ans.append(permutation.copy())
                return
            for val in nums:
                if val not in permutation:
                    permutation.append(val)
                    backtrack(permutation, i + 1)
                    permutation.pop()

        backtrack([], 0)
        return ans