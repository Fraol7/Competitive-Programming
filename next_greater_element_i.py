class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        for i in nums1:
            j = nums2.index(i)+1
            if j == len(nums2):
                answer.append(-1)
            elif nums2[j] > i:
                answer.append(nums2[j])
            else:
                answer.append(-1)
        return answer
