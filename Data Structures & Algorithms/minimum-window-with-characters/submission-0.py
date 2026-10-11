class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        maped={}
        txt={}
        i,j=0,0
        res,resLen=[-1,-1],float("infinity")
        count=0
        for val in t:
            txt[val]=txt.get(val,0)+1
        need=len(txt)
        while j<len(s):
            
            if s[j] in txt:
                maped[s[j]]=maped.get(s[j],0)+1
                if maped[s[j]]==txt[s[j]]:
                    count+=1

            
            while count==need:
                if(j-i+1)<resLen:
                    res=[i,j]
        
                    resLen=j-i+1
                if s[i] in maped:
                    
                    maped[s[i]]=maped.get(s[i],0)-1
                    if maped[s[i]]<txt[s[i]]:
                        count-=1
                    
            
                i+=1
            j+=1
        l,r=res    
        return s[l:r+1]




