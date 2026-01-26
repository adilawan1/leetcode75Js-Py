1class Solution(object):
2    def productExceptSelf(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        postfix=[1]
8        prefix=[1]
9        prod=1
10        post=1
11        array=[]
12        length=len(nums)
13        for num in range(length-1):
14            prod*=nums[num]
15            prefix.append(prod)
16        for num in range(length-1):
17            post*=nums[length-num-1]
18            postfix.append(post)
19        postfix.reverse()
20        for num in range(length):
21            array.append(postfix[num]*prefix[num])
22        return array