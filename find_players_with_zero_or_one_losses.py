class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner, loser = [], []
        dic = defaultdict()

        for win, los in matches:
            if win not in dic:
                dic[win] = 1
            if los not in dic:
                dic[los] = 0
            else:
                if dic[los] == 0:
                    dic[los] = 2
                elif dic[los] == 1:
                    dic[los] = 0

        for key, value in dic.items():
            if value == 1:
                winner.append(key)
            elif value == 0:
                loser.append(key)
        winner.sort()
        loser.sort()
        
        return [winner, loser]
                
            
