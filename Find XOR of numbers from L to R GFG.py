#User function Template for python3

class Solution:
    def findXOR(self, l, r):
        def rangexor(n):
            if n%4==0:
                return n
            elif n%4==1:
                return 1
            elif n%4==3:
                return 0
            else:
                return n+1
        
        lxor = rangexor(l-1)
        rxor = rangexor(r)
        return lxor^rxor

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