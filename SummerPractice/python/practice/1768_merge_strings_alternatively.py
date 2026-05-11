class Solution:
    def mergeAlternately(self, word1, word2):
        word3 = ""

        for i in range(max(len(word1), len(word2))):
            if i < len(word1):

                word3 += word1[i]
            if i < len(word2):
                word3 += word2[i]
            else: 
                print("Error: word2 is longer than word1")
            return word3