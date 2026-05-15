class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {']':'[', '}':'{', ')':'('}
        stack = []
        for c in s:
            if stack and c in mapping:
                tmp = stack.pop()
                if tmp != mapping[c]:
                    return False
            else:
                stack.append(c)
        
        return True if stack == [] else False