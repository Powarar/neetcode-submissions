class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        
        while left < len(nums) and nums[left] == 0:
            left+=1
        
        while right >= 0 and nums[right] == 2:
            right-=1

        i = left
        while i <= right:
            if nums[i] == 1:
                i+=1

            elif nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left+=1
                i+=1

            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right-=1