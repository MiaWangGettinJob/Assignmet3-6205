class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]

        def backtrack(num, times):

            if times == 0:
                return result.append(num)

            digit = num % 10
            next_digits = set([digit + k, digit - k])

            for Nextnum in next_digits:
                if 0 <= Nextnum and Nextnum < 10:
                    newnum = num * 10 + Nextnum
                    backtrack(newnum, times - 1)



        result = []
        for i in range(1,10):
            backtrack(i, n - 1)

        return result