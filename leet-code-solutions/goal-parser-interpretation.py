class Solution:
    def interpret(self, command: str) -> str:
        res = ''
        i = 0
        while i < len(command):
            if command[i] == 'G':
                res += 'G'
            elif command[i] == '(':
                if command[i+1] == ')':
                    res += 'o'
                    i += 1
                elif command[i+1:i+4] == 'al)':
                    res += 'al'
                    i += 3
            i += 1
        return res