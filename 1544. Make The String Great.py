class Solution:
    def makeGood(self, s: str) -> str:
        ogs=s
        i=0

        while i<len(s)-1:
            if ord(s[i]) - ord(s[i+1]) in [32,-32]:
                if i<len(s)-2:
                    s=s[:i]+s[i+2:]
                else:
                    s=s[:i]
                i=0
                continue
            i+=1
        return s