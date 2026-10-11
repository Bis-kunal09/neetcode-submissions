class Solution:
    def search(self, nums: List[int], target: int) -> int:

        i,j=0,len(nums)-1
        idx=-1
        while i<=j:

            

            mid=(i+j)//2

            if nums[mid]==target:
                return mid
            #left sorted portion check
            if nums[i]<=nums[mid]: 
                if target>nums[mid]:
                    i=mid+1
                elif target<nums[i]:
                    i=mid+1
                else:
                    j=mid-1
            # right sorted portion
            else:
                if target>nums[j]:
                    j=mid-1
                elif target<nums[mid]:
                    j=mid-1
                else:
                    i=mid+1
            



            
        return idx



        