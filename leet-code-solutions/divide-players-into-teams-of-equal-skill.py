class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i, j = 1, len(skill)-2
        check = skill[0] + skill[len(skill)-1]
        ans = skill[0]*skill[len(skill)-1]
        while i < j:
            if skill[i]+skill[j] != check:
                return -1
            ans += skill[i]*skill[j]
            i += 1
            j -= 1
        return ans
            