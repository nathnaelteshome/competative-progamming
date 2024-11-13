from typing import List


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        print(buyVolumes(nums))


        return True
        

def buyVolumes(volumes):
    ans = []
    prevAvails = set()
    lastAvail = 0
    for volume in volumes:
        prevAvails.add(volume)
        temp = []
        while lastAvail + 1 in prevAvails:
            lastAvail += 1
            temp.append(lastAvail)
        if temp:
            ans.append(temp)
        else:
            ans.append([-1])
    return ans
  

soln = Solution()
soln.primeSubOperation([2,1,4,3])

soln.primeSubOperation([2,1,5,4,6,3])