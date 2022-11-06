class Solution:
    def corpFlightBookings(self, bookings, n: int):
        result = [0]*(n+1)
        for i, j, k in bookings:
            result[i-1] += k
            result[j] -= k
        result.pop()
        for i in range(1, n):
            result[i] += result[i-1]
        return result
