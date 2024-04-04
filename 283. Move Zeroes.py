class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=[]
        l=len(nums)
        for i in nums:
            if i !=0:
                a.append(i)
        nums[::]=a+[0]*(l-len(a))