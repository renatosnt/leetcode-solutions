def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1

    while l <= r:
        soma = numbers[l] + numbers[r]

        # se passsa do target, movimenta o da direita
        # se é menor que o target, movimenta o da esquerda
        if soma > target:
            r -= 1
        elif soma < target:
            l += 1
        elif soma == target:
            return [l + 1, r + 1]
        