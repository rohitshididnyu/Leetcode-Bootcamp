class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        i =1
        while i <= (len(nums)-1):
            res[i] = nums[i-1]*res[i-1]
            i+=1
        r = len(nums)-1
        right =1
        while r >=0:
            res[r] = res[r]*right
            right = right* nums[r]
            r-=1 
        return res