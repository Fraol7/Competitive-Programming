class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0]*(n+1)
        for first, last, seats in bookings:
            flights[first-1] += seats
            flights[last] -= seats
        prefix = [flights[0]]
        for i in range(1, len(flights)-1):
            prefix.append(prefix[-1]+flights[i])
        return prefix
