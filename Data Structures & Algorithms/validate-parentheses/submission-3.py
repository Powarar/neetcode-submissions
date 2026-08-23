class Solution:
    def isValid(self, s: str) -> bool:
        map = {"]" : "[", "}" : "{", ")" : "(" }
        curStack = []
        for el in s:
            if el in ("{", "[", "("):
                curStack.append(el)
            else:
                if not curStack or(curStack and curStack.pop() != map[el]):
                    return False
                
        return not curStack