class Solution:
    def longestCommonPrefix(self, strs): 
        # find the longest common prefix between the strings in the list
        # if there is no common prefix, return an empty string
        # if the list is empty, return an empty string
        # if the list has only one string, return the string
        # if the list has more than one string, find the longest common prefix between the strings
        # return the longest common prefix
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        prefix = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
        return prefix

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
    print(sol.longestCommonPrefix(["dog", "racecar", "car"]))
    print(sol.longestCommonPrefix([]))
    print(sol.longestCommonPrefix(["flower"]))
    print(sol.longestCommonPrefix(["flower", "flow", "flight"]))