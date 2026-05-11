class Solution:
    def intToRoman(self, num: int) -> str:
        """Convert integer 1..3999 to Roman numeral (LeetCode 12)."""
        result = ""
        while num > 0:
            if num >= 1000:
                result += "M"
                num -= 1000
            elif num >= 900:
                result += "CM"
                num -= 900
            elif num >= 500:
                result += "D"
                num -= 500
            elif num >= 400:
                result += "CD"
                num -= 400
            elif num >= 100:
                result += "C"
                num -= 100
            elif num >= 90:
                result += "XC"
                num -= 90
            elif num >= 50:
                result += "L"
                num -= 50
            elif num >= 40:
                result += "XL"
                num -= 40
            elif num >= 10:
                result += "X"
                num -= 10
            elif num >= 9:
                result += "IX"
                num -= 9
            elif num >= 5:
                result += "V"
                num -= 5
            elif num >= 4:
                result += "IV"
                num -= 4
            else:
                result += "I"
                num -= 1
        return result


if __name__ == "__main__":
    sol = Solution()
    for n in (1994, 58, 9, 4, 1, 10, 100, 1000, 3999, 3749):
        print(n, "->", sol.intToRoman(n))
