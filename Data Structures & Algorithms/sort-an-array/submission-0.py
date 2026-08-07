class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        pivot = nums[len(nums) // 2]
        left = [el for el in nums if el < pivot]
        middle = [el for el in nums if el == pivot]
        right = [el for el in nums if el > pivot]

        return self.sortArray(left) + middle + self.sortArray(right)
