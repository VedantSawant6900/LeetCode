#User function Template for python3
class Solution:
    def twoOddNum(self, Arr, N):
        d={}
        ans=[]
        for i in Arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]%2==1:
                ans.append(i)
        ans.sort(reverse=True)
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        ob = Solution();
        ans = ob.twoOddNum(Arr,N)
        for i in range(len(ans)):
        	print(ans[i], end = " ")
        print()
# } Driver Code Ends