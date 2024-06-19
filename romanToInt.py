class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbolDict= {"I":1,"M":1000, "D":500, "C":100,"L":50,"X":10,"V":5}
        totalNum = 0
        i=0
        while i < len(s):
            if i + 1 < len(s) and symbolDict[s[i]] < symbolDict[s[i +1]]:
                tempNum = symbolDict[s[i+1]] - symbolDict[s[i]] 
                totalNum += tempNum 
                i += 2
            else:
                totalNum += symbolDict[s[i]]
                i += 1     
            tempNum = 0
        return totalNum