class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokenInfo = {} #tokenId: timeToLive, a dictionary that tells the expiration of the token 
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        totalTime = currentTime + self.timeToLive
        self.tokenInfo[tokenId] = totalTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.tokenInfo.get(tokenId, 0) > currentTime:
            self.tokenInfo[tokenId] = self.timeToLive + currentTime
        
    def countUnexpiredTokens(self, currentTime: int) -> int:
        UnexpiredTokens = [tokenLife for tokenLife in self.tokenInfo.values() if tokenLife > currentTime]
        return len(UnexpiredTokens)
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)