class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        product=1

        ltor=[]
        rtol=[]
        finalans=[]
        if len(nums)==2:
            return nums[::-1]
        for idx,val in enumerate(nums):
            product*=val
            ltor.append(product)

        product=1
        for idx,val in enumerate(nums[::-1]):
            product*=val
            rtol.append(product)

        rtol=rtol[::-1]
        finalans.append(rtol[1])
    

        for idx,val in enumerate(nums):
            if idx==0 or idx==len(nums)-1:
                continue
            finalans.append(ltor[idx-1]*rtol[idx+1])
        finalans.append(ltor[-2])
        return finalans