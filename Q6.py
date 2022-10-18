class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(first, path):
            if len(path) == k:
                return result.append(path[:])
            for i in range(first, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()



        for k in range(len(nums) + 1):
            backtrack(0,[])


        return result
