class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        if len(nums) < 2: return False
        for i, num in enumerate(nums):
            if num == 0:
                continue
            slow, fast = i, i
            while num * nums[fast] > 0 and num * nums[(fast + nums[fast]) % len(nums)] > 0:
                slow = (slow + nums[slow]) % len(nums) 
                fast = ((fast + nums[fast]) % len(nums) + nums[(fast + nums[fast]) % len(nums)]) % len(nums)
                if slow == fast:
                    if slow == (slow + nums[slow]) % len(nums):
                        break
                    return True
            slow, sign = i, num
            while sign * nums[slow] > 0:
                next = (slow + nums[slow]) % len(nums)
                nums[slow] = 0
                slow = next
        return False

        