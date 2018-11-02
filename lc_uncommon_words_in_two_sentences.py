# https://leetcode.com/problems/uncommon-words-from-two-sentences/

import collections
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A = A.split(' ')
        B = B.split(' ')
        wordCount = collections.defaultdict(int)
        for i in A:
            wordCount[i] += 1
        for j in B:
            wordCount[j] += 1
        ret = []
        for k in wordCount:
            if wordCount[k] == 1:
                ret.append(k)
        return ret