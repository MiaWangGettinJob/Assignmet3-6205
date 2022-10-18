class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(first, nums):
            if first == len(nums):
                result.append(nums[:])
                return
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1, nums)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack(0, nums)
        return result