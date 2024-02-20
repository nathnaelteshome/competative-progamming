class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [x + 1 for x in range(n)] #[1,2,3,4,5] k = 2

        idx = 0

        while len(friends) != 1:
            idx = (idx + k - 1) % len(friends) # idx = (0 + 2 - 1) % 5
            friends.remove(friends[idx])
        
        return friends[0]