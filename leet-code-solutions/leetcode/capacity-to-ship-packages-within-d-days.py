class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)
        def check(cap):
            on_ship = 0 
            passed_days = 1
            for weight in weights:
                if on_ship + weight > cap:
                    passed_days += 1
                    on_ship = 0
                on_ship += weight
    
            return passed_days <= days 
        while start < end:
            mid = start+(end-start)//2
            if check(mid):
                end = mid
            else:
                start = mid+1
        return start

        