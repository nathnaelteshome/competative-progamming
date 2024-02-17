class UndergroundSystem:

    def __init__(self):
        self.stationCheckIn  = defaultdict(set)
        self.stationCheckOut  = defaultdict(set)
        self.checkInId  = {}
        self.checkOutId  = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInId[id] = t
        self.stationCheckIn[stationName].add(id)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.checkOutId[id] = t
        self.stationCheckOut[stationName].add(id)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float: # [["leython", "waterloo"]]
        set1 = self.stationCheckIn[startStation] #{id1} set
        set2 = self.stationCheckOut[endStation] #{id2} set

        intersectionset = set(set1) & set(set2)
        summation = 0
                
        for ida in intersectionset:
            currDiff = self.checkoutId[ida] - self.checkInId[ida]
            summation += currDiff
        
        return summation/len(intersectionset)
