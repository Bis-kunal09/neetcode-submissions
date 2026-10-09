class Solution:

    def encode(self, strs: List[str]) -> str:
        finalans=[]
        for val in strs:
            finalans.append(str(len(val)))
            finalans.append('#')
            
            finalans.append(val)

        s="".join(finalans)
               
        return  s   




    def decode(self, s: str) -> List[str]:

        finalans=[]
        i=0
        while i<len(s):
            j=i+1
            while s[j]!='#':
                j+=1
            l=int(s[i:j])

            i=j+1
            j=i+l
            finalans.append(s[i:j])
            i=j

        return finalans
        



