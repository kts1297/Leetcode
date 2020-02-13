# https://leetcode.com/problems/two-sum/

from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int)
        res = []
        for x in range(len(nums)):
            if target-nums[x] in dic:
                res.append(dic[target-nums[x]])
                res.append(x)
                return res
            dic[nums[x]] = x