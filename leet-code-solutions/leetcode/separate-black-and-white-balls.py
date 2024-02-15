class Solution:
    def minimumSteps(self, s: str) -> int:
        refer, left, right, ops = list(s), 0, len(s)-1, 0
        while left < right:
            if refer[left] == "1" and refer[right] == "0":
                refer[left], refer[right] = refer[right], refer[left]
                ops += right-left
                left += 1
                right -= 1
            elif refer[left] == "1":
                right -= 1
            elif refer[left] == "0":
                left += 1
        return ops
