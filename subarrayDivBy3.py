class Solution:
    def subarraysDivByK(self, nums, k):
        count = 0
        prefix_sum = 0
        modulo_count = {0: 1}

        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            count += modulo_count.get(prefix_sum, 0)
            modulo_count[prefix_sum] = modulo_count.get(prefix_sum, 0) + 1

        return count
