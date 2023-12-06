class Solution:
    def totalMoney(self, n: int) -> int:
        week = n // 7
        week_gain = int(week/2 * (56 + (week - 1)*7))
        remaining_days = n % 7
        remaining_gain = int(remaining_days/2 * (2*(week + 1) + (remaining_days - 1)))
        return week_gain + remaining_gain