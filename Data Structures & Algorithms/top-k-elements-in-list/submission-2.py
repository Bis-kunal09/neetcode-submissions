class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for val in nums:
            if val not in dic:
                dic[val]=1
            else:
                dic[val]=dic.get(val)+1
        a=[]
        for key,val in dic.items():
            heapq.heappush(a,[val,key])
            if len(a)>k:
                heapq.heappop(a)

            
        finalans=[]
        for idx,val in enumerate(a):
            finalans.append(a[idx][1])

        return finalans