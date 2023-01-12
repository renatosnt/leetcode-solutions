def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    if n == 0:
        return True

    if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
        return True

    if flowerbed[0] == 0 and flowerbed[1] == 0:
        flowerbed[0] = 1
        n -= 1

    
    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] == 0:
            flowerbed[i] = 1
            n -= 1

    if flowerbed[-1] == 0 and flowerbed[-2] == 0:
        flowerbed[-1] = 1
        n -= 1


    print(flowerbed)
    if n <= 0:
        return True
    return False