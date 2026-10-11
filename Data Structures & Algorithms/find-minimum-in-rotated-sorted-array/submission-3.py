class Solution:
    def findMin(self, nums: List[int]) -> int:


        i,j=0,len(nums)-1

        while i<j:
            mid= int((i+j)/2)
            print(mid)

            if nums[mid+1]<nums[mid]:
                return nums[mid+1]
            else:
                if nums[i]<nums[i+1]:
                    i+=1
                else:
                    return nums[i+1]
                
                if nums[j]>nums[j-1]:
                    j-=1
                else:
                    return nums[j]
        return nums[0]
        