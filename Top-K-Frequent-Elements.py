1class Solution(object):
2    def topKFrequent(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: List[int]
7        """
8        nums_hash={}
9        for num in nums:
10            if num in nums_hash:
11                nums_hash[num]+=1
12            else:
13                nums_hash[num]=1
14        return sorted(nums_hash,key=nums_hash.get,reverse=True)[:k]
15
16