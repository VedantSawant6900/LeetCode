class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s,i,j=0,0,len(nums)-1
        while i<=j:
            if i==j:
                s=s^nums[i]
                i+=1
                j-=1
            else:
                s=s^nums[i]
                s=s^nums[j]
                i+=1
                j-=1
        return s