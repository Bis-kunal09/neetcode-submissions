class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic={}
        for idx,val in enumerate(nums):
            dic[val]=idx

        for idx,val in enumerate(nums):
            if target-val in dic and idx!=dic.get(target-val):
                return sorted([idx,dic.get(target-val)])
        return []
        