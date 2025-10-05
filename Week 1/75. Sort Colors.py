class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid ,high = 0,0,len(nums)-1
        res = [0] * len(nums)
        print(res)
        while mid <= high:
            if nums[mid] == 2:
                temp = nums[high]
                nums[high] = nums[mid]
                nums[mid] = temp
                high -=1
            elif nums[mid] == 1:
                mid +=1
            elif nums[mid] == 0:
                temp = nums[low]
                nums[low] = nums[mid]
                nums[mid] = temp
                mid +=1
                low +=1