class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		ctr, prefix = 0, 0
		refer = {0 : 1}
		for num in nums:
			prefix += num
			if prefix - k in refer:
				ctr +=refer[prefix - k]
			refer[prefix] = refer.get(prefix, 0) + 1
		return ctr