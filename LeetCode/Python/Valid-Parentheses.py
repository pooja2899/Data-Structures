class Solution:
    def isValid(self, s: str) -> bool:
        bracket =  {'(':')','{':'}','[':']'}
        open_bracket = set(['(','{','['])
        stack=[]
        
        for i in s:
            if i in open_bracket:
                stack.append(i)
                
            elif stack and i == bracket[stack[-1]]:
                stack.pop()
                
            else:
                return False
        return stack == []
