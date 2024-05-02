class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        for i in nums:
            if (-1 * i) in nums:
                return -1 * i
        return -1