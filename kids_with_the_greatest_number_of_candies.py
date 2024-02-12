class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        output = []
        
        for candy in candies:
            if candy + extraCandies >= max_candy:
                output.append(True)
            else:
                output.append(False)
        
        return output
        