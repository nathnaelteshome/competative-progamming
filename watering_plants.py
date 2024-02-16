class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        curCapacity = capacity
        position = 0

        for plantIndex in range(len(plants) - 1):  
            curCapacity -= plants[plantIndex]
            
            #checking if we can't fill the next plant
            if plants[plantIndex + 1] > curCapacity:
                position += plantIndex + 1
                curCapacity = capacity
                position += plantIndex + 2
            else:
                position += 1
        
        return position + 1

