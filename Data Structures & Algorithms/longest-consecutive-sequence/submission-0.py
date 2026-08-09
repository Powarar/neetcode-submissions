class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0

        for i in hashset:
            if i - 1 not in hashset:
                cnt = 1
                while cnt + i in hashset:
                    cnt+=1
                longest = max(cnt, longest)

        return longest
