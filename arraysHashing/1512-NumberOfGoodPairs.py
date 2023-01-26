class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        valToIndex = defaultdict(list)
        total = 0
        # solução O(n) de tempo e O(n) de espaço
        for i in range(len(nums)):
            valToIndex[nums[i]].append(i)
        
        for key, val in valToIndex.items():
            total += (len(val) - 1) * len(val) / 2
        return int(total)