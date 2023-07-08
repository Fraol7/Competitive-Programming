class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()
        result = []
        for num in nums1:
            if self.binarySearch(nums2, num) and num not in result:
                result.append(num)
        return result
    
    def binarySearch(self, nums1, num):
        left, right = 0, len(nums1) - 1

        while left <= right:
            mid = (left + right) // 2 
            if nums1[mid] == num:
                return True
            elif nums1[mid] < num:
                left = mid + 1
            else:
                right = mid - 1 
        return False
