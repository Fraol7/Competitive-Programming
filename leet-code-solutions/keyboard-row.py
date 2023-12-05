class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = {1: set("qwertyuiop"), 2: set("asdfghjkl"), 3: set("zxcvbnm")}
        result = []
        for word in words:
            word_lower = word.lower() 
            row = None 
            for key, value in keyboard.items():
                if word_lower[0] in value: 
                    row = key
                    break
            if row is not None and all(char in keyboard[row] for char in word_lower): 
                result.append(word)
        return result