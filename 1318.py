# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/?envType=study-plan-v2&envId=leetcode-75

# Solution 1
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        val = (a|b)^c
        res = 0
        while (val != 0):
            if (val&1 != 0):
                if (c&1 == 0):
                    if (a&1 == 1): res += 1
                    if (b&1 == 1): res += 1
                else:
                    res += 1

            val = val>>1
            a = a>>1
            b = b>>1
            c = c>>1
        return res

# Solution 2
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        val = (a|b)^c
        another_val = (a&b&val) # gets all bits that are set in a & b and not set in c
        c1 = 0
        while val:
            val = val & (val-1)
            c1 += 1
        c2 = 0
        while another_val:
            another_val = another_val & (another_val-1)
            c2 += 1
        return c1+c2
