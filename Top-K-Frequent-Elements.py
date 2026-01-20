1class Solution(object):
2    def topKFrequent(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: List[int]
7        """
8        number_hash={}
9        for num in nums:
10            if num in number_hash:
11                number_hash[num]+=1
12            else:
13                number_hash[num]=1
14        print(number_hash)
15        final_list=sorted(number_hash,key=number_hash.get,reverse=True)
16        print(final_list)
17        return final_list[:k]
18