from collections import Counter, defaultdict


class FrequencyTracker(object):
    def __init__(self) -> None:
        self.freqValuePair = Counter() # number : freq
        self.countFrequency = Counter() # freq : occurance
        
    def add(self, number):
        self.freqValuePair[number] += 1
        self.countFrequency[self.freqValuePair[number]] += 1
        self.countFrequency[self.freqValuePair[number] - 1] -= 1
        
    def deleteOne(self, number):
        if self.freqValuePair[number]:
            self.freqValuePair[number] -= 1
            if self.freqValuePair[number] == 0: 
                del self.freqValuePair[number]
            self.countFrequency[self.freqValuePair[number]] += 1
            self.countFrequency[self.freqValuePair[number] + 1] -= 1 

    
    def hasFrequency(self, frequency):
        return self.countFrequency[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)