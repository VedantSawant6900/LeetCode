class Solution:
    def frequencySort(self, s: str) -> str:
        d={}

        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        sd={k: v for k, v in sorted(d.items(), reverse=True, key=lambda item: item[1])}
        stri=""
        for i in sd:
            stri=stri+i*sd[i]
        return stri