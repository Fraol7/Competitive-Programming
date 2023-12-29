class Solution:
    def sortSentence(self, s: str) -> str:
        s_list = s.split()
        n = len(s_list)
        result = ""
        refer = defaultdict(int)
        for string in s_list:
            refer[string[-1]] = string[:len(string)-1]
        for i in range(1, n+1):
            result += refer[str(i)]
            if i != n:
                result += ' '
        return result