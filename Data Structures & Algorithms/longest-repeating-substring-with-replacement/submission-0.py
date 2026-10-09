class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        map={}
        fans=0
        i=0
        res=0
        for j in range(len(s)):

            map[s[j]]=map.get(s[j],0)+1
         
            if (j-i+1)-max(map.values())>k:
                map[s[i]]-=1
                i+=1

            fans=max(fans,j-i+1)
        return fans

        