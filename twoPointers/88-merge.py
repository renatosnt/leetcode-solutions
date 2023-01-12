def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    first = m - 1
    second = n - 1

    for i in reversed(range(m+n)):
        print(i)
    
        if first >= 0 and second >= 0 and nums1[first] >= nums2[second]:
            nums1[i] = nums1[first]
            first -= 1
        elif second >= 0:
            nums1[i] = nums2[second]
            second -= 1
        