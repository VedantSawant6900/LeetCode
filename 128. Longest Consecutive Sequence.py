class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        prev=None
        max=0
        c=0
        for i in nums:
            if prev==None or prev == i:
                prev = i
                continue
            if i-prev==1:
                c+=1
            else:
                if c+1>max:
                    max=c+1
                c=0
            prev=i
        if c+1>max:
            max=c+1
        return max