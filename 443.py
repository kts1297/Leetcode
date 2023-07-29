# https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def compress(self, chars: List[str]) -> int:
        res = ""
        count = 1
        c = chars[0]
        for ndx in range(1, len(chars)):
            if c == chars[ndx]:
                count += 1
            else:
                if count == 1:
                    res = f"{res}{c}"
                else:
                    res = f"{res}{c}{count}"

                count = 1
                c = chars[ndx]
        if count == 1:
            res = f"{res}{c}"
        else:
            res = f"{res}{c}{count}"
        for ndx in range(len(res)):
            chars[ndx] = res[ndx]
        return len(res)