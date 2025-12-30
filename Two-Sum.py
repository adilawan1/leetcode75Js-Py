1class Solution(object):
2    def twoSum(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        result_map={}
9        results=[]
10        for i, num in enumerate(nums):
11            complement = target - num
12            if complement in result_map:  # Check if complement seen before
13                results = [result_map[complement], i]
14                break
15            result_map[num] = i  # Store the current number's index
16        return results