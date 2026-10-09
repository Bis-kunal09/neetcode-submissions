class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic={}
        ans=[]
        for val in strs:
            if "".join(sorted(val)) in dic:
                dic.get("".join(sorted(val))).append(val)
            else:
                dic["".join(sorted(val))]=[val]
            
        for key,value in dic.items():
            ans.append(value)
              

        return ans        
                