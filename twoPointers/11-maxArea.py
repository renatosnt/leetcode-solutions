def maxArea(self, height: List[int]) -> int:
    # a maior area será dada pelas duas barras que estão
    # mais longe e que são maiores

    l, r = 0, len(height) - 1
    ans = -1

    while l <= r:

        area = min(height[l], height[r]) * (r - l)
        ans = max(ans, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return ans