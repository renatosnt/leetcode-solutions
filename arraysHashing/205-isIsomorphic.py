def isIsomorphic(self, s: str, t: str) -> bool:
    mapST, mapTS = {}, {}

    for i in range(len(s)):
        c1 = s[i]
        c2 = t[i]
        # se c1 ou c2 estão mapeados
        # se já c1 ou c2 já mapeiam para outros valores, retorne falso
        if (c1 in mapST and mapST[c1] != c2) or\
            (c2 in mapTS and mapTS[c2] != c1):
            return False


        mapST[c1] = c2
        mapTS[c2] = c1 
    
    return True
    print(mapST)