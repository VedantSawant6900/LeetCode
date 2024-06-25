#User function Template for python3

class Solution:
    def findXOR(self, l, r):
        s1=0
        s2=0
        i=l
        j=r
        while i<j:
            s1=s1^i
            s2=s2^j
            i+=1
            j-=1
        if i==j:
            return s1^s2^i
        else:
            return s1^s2

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        l, r = list(map(int, input().split()))
        ob = Solution()
        res = ob.findXOR(l, r)
        print(res)
# } Driver Code Ends