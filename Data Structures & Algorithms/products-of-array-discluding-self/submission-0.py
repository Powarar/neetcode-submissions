class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1 for i in range(len(nums))]
        suff = nums[-1]
        for i in range(1, len(nums)):
            pref[i] = nums[i-1] * pref[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            pref[i] *=  suff
            suff *= nums[i]
        
        return pref