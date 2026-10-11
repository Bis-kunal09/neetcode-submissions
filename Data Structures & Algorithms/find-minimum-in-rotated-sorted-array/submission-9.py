class Solution:
    def findMin(self, nums: List[int]) -> int:

        i,j=0,len(nums)-1
        res=nums[0]

        while i<=j:

            if nums[i]<nums[j]:
                res=min(res,nums[i])
                break
            
            m=(j+i)//2
            res=min(res,nums[m])
            if nums[i]<=nums[m]:
                i=m+1
            else:
                j=m-1
        return res
        