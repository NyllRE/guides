class Solutions:
    def MySolution(self, nums: list[int], k: int) -> list[int]:
        from collections import defaultdict
        res = defaultdict(list)
        nums.sort()

        for num in nums:
            """
            the equation below creates a list in range with
            the smallest number and the biggest number for example
            input = [ -3, -1, 0, 1, 5]
            count = [0,0,0,0,0,0,0,0]
            len(count) = range(-3,5) = 8
            think of it as [ -3, -2, -1, ..., 5 ]
            """
            count = [0] * ( nums[-1]+1 + abs(nums[0]) )
            
            """
            to use it, you need to add the smallest number's
            absolute value to the value you want
            num = -1
            abs(nums[0]) + num = abs(-3) + -1 = 3 + -1 = 2 
            and if you see the count above you'll find that 
            the index of -1 in the count should be in place of nums[2]
            """
            count[ abs(nums[0]) + num ] += 1
            
            res[tuple(count)].append(num)

        res = list(res.values())
        res.sort(key=len, reverse=True)

        finalres = []
        for numgroup in res:
            finalres.append(numgroup[0])

        return finalres[0:k]

sol = Solutions()

mysolution = sol.MySolution([1,1,1,2,2,3,3,3], 2)

