class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        l3 = min(l1,l2)
        word3 = []
        for i in range(l3):
            word3.append(word1[i])
            word3.append(word2[i])
        if l1<l2:
            word3.append(word2[l1:])
        elif l1>l2:
            word3.append(word1[l2:])
        print(word3)
        merged = ''.join(word3)
        print(merged)
        return merged
        
