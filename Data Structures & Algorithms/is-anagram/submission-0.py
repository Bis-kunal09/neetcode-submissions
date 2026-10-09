class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic={}
        for val in s:
            if val not in dic:
                dic[val]=1
            else:
                dic[val]=dic.get(val)+1

        for val in t:
            if val in dic:
                dic[val]=dic.get(val)-1
                if dic.get(val)==0:
                    del dic[val]
            else:
                return False        

            

        return len(dic)==0