class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]

        for i in range(len(s)):

            if len(stack)==0:
                stack.append(s[i])
            else:
                if s[i]==')':
                    if stack[-1]=='(':
                        stack.pop()
                    else:
                        return False
                elif s[i]==']':
                    if stack[-1]=='[':
                        stack.pop()
                    else:
                        return False
                elif s[i]=='}':
                    if stack[-1]=='{':
                        stack.pop()
                    else:
                        return False        
                else:
                    stack.append(s[i])
        if len(stack)==0:
            return True
        else:
            return False        