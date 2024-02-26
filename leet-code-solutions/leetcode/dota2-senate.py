class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D = deque()
        R = deque()
        n = len(senate)
        for i in range(n):
            if senate[i] == "D":
                D.append(i)
            else:
                R.append(i)
        i = 0
        while i+1:
            if not D:
                return "Radiant"
            elif not R:
                return "Dire"
            if senate[i%n] == "D" and i%n == D[0]:
                D.append(D.popleft())
                R.popleft()
            elif senate[i%n] == "R" and i%n == R[0]:
                R.append(R.popleft())
                D.popleft()
            i += 1        
