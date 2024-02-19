class Solution:
    def nextGreaterElement(self, nums1, nums2):
        answer = []
        for i in nums1:
            j = nums2.index(i)
            if j+1 < len(nums2):
                max_val = i
                for k in range(j+1,len(nums2)):
                    if max_val < nums2[k]:
                        answer.append(nums2[k])
                        max_val = nums2[k]
                        break
                if max_val == i:
                    answer.append(-1)
            else:
                answer.append(-1)
        return answer        