class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = []
        for i in range(n):
            ctr = 0
            for j in range(n):
                if i == j:
                    continue
                elif boxes[j] == "1":
                    ctr += abs(i-j)
            answer.append(ctr)
        return answer
