#!/usr/bin/env python3


class Solution:
    def mySol(self, nums: list) -> list:
        res = [1]
        # there is a 1 because of the way we are calculating the prefix and the postfixes

        preholder = 1
        prefix = nums[-1]

        for i in nums:
            preholder *= i
            res.append(preholder)
        res.pop()

        preholder = 1
        res.reverse()

        reversednums = nums
        reversednums.reverse()

        for iter, num in enumerate(nums):
            res[iter] *= preholder
            preholder *= reversednums[iter]

        return res


solution = Solution()

from sys import argv

argument = [-1, 1, 0, -3, 3]

sol = solution.mySol(argument)

print(sol)
