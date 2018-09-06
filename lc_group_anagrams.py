https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/

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

    # Faster than 24% of all submissions
        
    