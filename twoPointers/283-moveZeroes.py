def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # olhando o problema de outra perspectiva, basta
    # mover todos elementos diferentes de zero para o lado esquerdo
    left = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[left], nums[i] = nums[i], nums[left]
            left += 1