class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        lookup=set(nums)
        longest=0
        for num in nums:
            if num-1 not in lookup:
                lenght=1
                while num+lenght in lookup:
                    lenght+=1

                longest=max(longest,lenght)



        return longest        