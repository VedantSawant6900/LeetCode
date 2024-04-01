class Solution:
    def reverseVowels(self, s: str) -> str:
        rep=s
        i=0
        j=len(s)-1
        v="aeiouAEIOU"
        k=""
        while i<j:
            if s[i] in v and s[j] in v:
                k1=s[i]
                k2=s[j]
                s=s[:i]+k2+s[i+1:]
                s=s[:j]+k1+s[j+1:]
                i+=1
                j-=1
            if s[i] not in v:
                i+=1
            if s[j] not in v:
                j-=1
        return s