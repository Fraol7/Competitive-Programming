class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        dist = len(set(nums))
        refer = defaultdict(int)
        left = 0
        subarrays = 0
        for right in range(len(nums)):
            refer[nums[right]] += 1
            while len(refer) == dist:
                subarrays += len(nums)-right
                refer[nums[left]] -= 1
                if refer[nums[left]] == 0:
                    del refer[nums[left]]
                left += 1
        return subarrays

