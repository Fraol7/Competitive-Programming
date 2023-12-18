class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loser_freq, result = {}, [[], []]
        for winner, loser in matches:
            loser_freq[winner] = loser_freq.get(winner, 0)
            loser_freq[loser] = loser_freq.get(loser, 0) + 1
        for player in range(max(chain(*matches)) + 1):
            if player in loser_freq and loser_freq[player] <= 1:
                result[loser_freq[player]].append(player)
        return result