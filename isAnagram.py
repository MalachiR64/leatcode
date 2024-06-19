class Solution(object):
    def isAnagram(self, s, t):
        dictCountS, dictCountT = {} , {}

        for char in s:
            if char in dictCountS:
                dictCountS[char] += 1
            else:
                dictCountS[char] = 1

        for char in t:
            if char in dictCountT:
                dictCountT[char] += 1
            else:
                dictCountT[char] = 1
        if dictCountT == dictCountS:
            return True
        else: 
            return False
        