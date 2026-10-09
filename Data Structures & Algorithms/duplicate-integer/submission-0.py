class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic={}
        for val in nums:
            if val not in dic:
                dic[val]=1
            else:
                return True          
        return False
        