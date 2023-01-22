class Solution:
    def findMin(self, nums: List[int]) -> int:
        # queremos encontrar o menor elemento de um array
        # ordenado em O(log n). Se é em O(log n), vamos precisar
        # usar busca binária. Seria trivial, se o array não fosse rotacionado.
        # Logo, se transformarmos um array rotacionado em um não rotacionado,
        # o problema está resolvido.
        minElement = float("inf")

        # relembrando a busca binária
        l, r = 0, len(nums) - 1

        while l <= r:
          mid = l + (r - l) / 2
          if nums[mid] < target:
            #segunda metade
            l = mid + 1
          elif nums[mid] > target:
            # primeira metade
            r = mid - 1
          else:
            # encontramos

        # minElement = min(minElement, temp)
        return minElement 