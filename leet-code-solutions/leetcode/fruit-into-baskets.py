class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window, left, ans = {}, 0, 0
        for right in range(len(fruits)):
            fruit = fruits[right]
            window[fruit] = window.get(fruit, 0) + 1
            while len(window) > 2:
                window[fruits[left]] -= 1
                if window[fruits[left]] == 0:
                    window.pop(fruits[left])
                left += 1
            ans = max(ans, right-left+1)
        return ans