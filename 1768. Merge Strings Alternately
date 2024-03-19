class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1:
            return word2
        if not word2:
            return word1
        l1=len(word1)
        l2=len(word2)
        s=""
        i=0
        while i < l1 and i < l2:
            s=s+word1[i]
            s=s+word2[i]
            i+=1
        if i==l1:
            s=s+word2[i:l2]
        elif i==l2:
            s=s+word1[i:l1]
        return s