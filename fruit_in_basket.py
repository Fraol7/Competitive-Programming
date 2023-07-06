class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = {}
        left, right = 0, 0
        ans = 0

        while right < len(fruits):
            fruit = fruits[right]
            window[fruit] = window.get(fruit, 0) + 1
            while len(window) > 2:
                window[fruits[left]] -= 1
                if window[fruits[left]] == 0:
                    window.pop(fruits[left])
                left += 1
            right += 1
            ans = max(ans, right-left)

        return ans
