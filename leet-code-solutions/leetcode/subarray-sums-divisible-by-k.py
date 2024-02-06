class Solution:
	def subarraysDivByK(self, nums, k):
		ctr, prefix = 0, 0
		refer = {0 : 1}
		for num in nums:
			prefix = (num + prefix)%k
			ctr += refer.get(prefix, 0) 
			refer[prefix] =  refer.get(prefix, 0) + 1
		return ctr