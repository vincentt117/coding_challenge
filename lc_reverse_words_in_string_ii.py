# https://leetcode.com/problems/reverse-words-in-a-string-ii/

class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
        [" ","b","l","u","e","t","h","e"," ","s","k","y"," ","i","s"]
        length = index = len(str) - 1
        mark = 0
        while length >= 0:
            if str[index] == " " and length != 0:
                str = str[:mark] + str[index+1:len(str) ]  + [" "] + str[mark:index]
                mark = mark + (len(str) - index)
                index = len(str) - 1
            else:
                index -= 1
            length -= 1
    # Doesn't run, but gives correct answer. 
    
    def reverseWords(self, s):
        def reverse(i, j):
            while 0 <= i < j < len(s):
                s[i], s[j] = s[j], s[i]
                i, j = i + 1, j - 1

        s.append(" ")
        start = 0
        for i, v in enumerate(s):
            if v == " ":
                reverse(start, i - 1)
                start = i + 1
        s.pop()
        reverse(0, len(s) - 1)
    # Found in discussion, reverses each word starting at the beginning. Then the same process except on the words 
    # ie., input: ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    # ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e", " "]
    # ["e","h","t"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    # .
    # .
    # ["e","h","t"," ","y","k","s"," ","s","i"," ","e","u","l","b", " "]
    # ["e","h","t"," ","y","k","s"," ","s","i"," ","e","u","l","b"]
    # ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
