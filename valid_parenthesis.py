class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        if s[0] not in ['(', '[', '{']:
            return False
        for bracket in s:
            if bracket in ['(', '[', '{']:
                lst.append(bracket)
            elif len(lst) == 0:
                return False                
            else:
                openning = lst.pop()
                if (openning == '(' and bracket == ')') or (openning == '[' and bracket == ']') or (openning == '{' and bracket == '}'):
                    continue
                else:
                    return False
        if len(lst) == 0:
            return True
        return False
