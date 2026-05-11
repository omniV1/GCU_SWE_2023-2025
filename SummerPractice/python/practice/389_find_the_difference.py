class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Use XOR to find the extra character in t.
        # Since t is s with one extra letter (shuffled), XOR of all chars in s+t
        # leaves exactly that extra letter.
        xor_val = 0
        for ch in s:
            xor_val ^= ord(ch)
        for ch in t:
            xor_val ^= ord(ch)
        return chr(xor_val)

if __name__ == "__main__":
    sol = Solution()
    print(sol.findTheDifference("abcd", "abcde"))
    print(sol.findTheDifference("a", "aa"))
    print(sol.findTheDifference("ae", "aea"))
    print(sol.findTheDifference("a", "a"))
    print(sol.findTheDifference("a", "a"))