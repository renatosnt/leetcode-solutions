def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    ans = []
    for n in nums1:
        res = -1
        idx = nums2.index(n)
        for i in range(idx, len(nums2)):
            if nums2[i] > n:
                res = nums2[i]
                break

        
        ans.append(res)
    return ans