class Solution:
    def findMin(self, nums: List[int]) -> int:
        # queremos encontrar o menor elemento de um array
        # ordenado em O(log n). Se é em O(log n), vamos precisar
        # usar busca binária. Seria trivial, se o array não fosse rotacionado.
        # Logo, se transformarmos um array rotacionado em um não rotacionado,
        # o problema está resolvido.
        minElement = float("inf")

        minElement = min(minElement, temp)
        return minElement 