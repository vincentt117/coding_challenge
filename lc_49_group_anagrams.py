# 49. Group Anagrams

# https://leetcode.com/problems/group-anagrams/description/

# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagramStorage = collections.defaultdict(list)
        for i in strs:
            letterCountList = [0]*26
            for j in i:
                letterCountList[ord(j.lower()) - 97] += 1
            anagramStorage[tuple(letterCountList)].append(i)
        return anagramStorage.values()
    # Solution beats ~40% of all submissions

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        anagramStorage = collections.defaultdict(list)
        for i in strs:
            tempVal = 1
            for j in i:
                tempVal *=  primes[ord(j.lower()) - 97]
            anagramStorage[tempVal].append(i)
        return anagramStorage.values()
    # Solution using unique product of prime as key, found in discussion. Faster than ~40 of submissions
        