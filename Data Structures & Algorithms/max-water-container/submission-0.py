class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxi=-1
        i,j=0,len(heights)-1
        while i<j:
            maxi=max(maxi,min(heights[i],heights[j])*(j-i))
            if heights[i]<=heights[j]:
                i+=1
            else:
                j-=1
        return maxi    
        