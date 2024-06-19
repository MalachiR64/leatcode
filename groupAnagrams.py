class Solution(object):
    def groupAnagrams(self, strs):
        anagramDict = {}

        for word in strs:
            wordCount = tuple(sorted(word))
            if wordCount not in anagramDict:
                anagramDict[wordCount] = []
            anagramDict[wordCount].append(word)
        return list(anagramDict.values())