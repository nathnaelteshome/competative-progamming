class UndergroundSystem:

    def __init__(self):
        self.checkInInfo = defaultdict(tuple) #id : (checkInTime, checkInStationName)
        self.stationTimeInfo = defaultdict(list) #(checkInStationName, checkOutStationName) :[timeTaken]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInInfo[id]=(t,stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkInTime,checkInStationName = self.checkInInfo[id]
        timeTaken = t - checkInTime
        self.stationTimeInfo[(checkInStationName, stationName)].append(timeTaken)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float: # [["leython", "waterloo"]]
        journey = (startStation, endStation)
        listOfTimeTaken = self.stationTimeInfo[journey]
        summation = sum(listOfTimeTaken)
        return summation / len(self.stationTimeInfo[journey])
