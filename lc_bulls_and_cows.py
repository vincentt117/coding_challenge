# https://leetcode.com/problems/bulls-and-cows/description/

class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bullCount = 0
        cowCount = 0
        secretCounter = collections.defaultdict(int)
        guessCounter = collections.defaultdict(int)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bullCount += 1
            else:
                secretCounter[secret[i]] += 1
                guessCounter[guess[i]] += 1
        for j in guessCounter:
            if j in secretCounter:
                cowCount += min(secretCounter[j], guessCounter[j])
        return str(bullCount) + "A" + str(cowCount)+ "B"


# Results https://leetcode.com/submissions/detail/183277797/