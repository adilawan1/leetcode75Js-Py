1class Solution(object):
2    def groupAnagrams(self, strs):
3        """
4        :type strs: List[str]
5        :rtype: List[List[str]]
6        """
7        anagrams=defaultdict(list)
8        for string in strs:
9            alphabets=[0]*26
10            for c in string:
11                alphabets[ord(c)-ord('a')]+=1
12            key=tuple(alphabets)
13            anagrams[key].append(string)
14        return list(anagrams.values())