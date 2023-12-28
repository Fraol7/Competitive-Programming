class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.refer = defaultdict(int)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.refer[tokenId] += currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.refer[tokenId] > currentTime:
            self.refer[tokenId] = currentTime + self.timeToLive        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        ctr = 0
        for i in self.refer:
            if self.refer[i] > currentTime:
                ctr += 1
        return ctr        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)