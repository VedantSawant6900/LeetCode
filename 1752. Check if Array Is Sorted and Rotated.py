class Solution:
    def check(self, nums: List[int]) -> bool:
        flag=0
        check=0
        l=len(nums)
        for i in range(l-1):
            if nums[i+1]<nums[i]:
                flag+=1
            if flag:
                print("here")
                print(nums[0],nums[i+1:l])
                if any(nums[0]<z for z in nums[i+1:l]):
                    print("here1")
                    check = 1
                    break
        print(flag)
        if flag>1 or check:
            return False
        else:
            return True