class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        finalans=[]
        nums.sort()
        
        for idx, val in enumerate(nums):
            if idx>0 and nums[idx]==nums[idx-1]:
                continue
            j=idx+1
            k=len(nums)-1
            
            while j<k and j<len(nums)-1:
                total=nums[j]+nums[k]+nums[idx]
                if total==0:
                    finalans.append([nums[idx],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate third elements
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1    
        return finalans

        