class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def helper(remains, target, path):
            if target == 0:
                result.append(path[:])
                return

            if target < 0:
                return

            if target > 0:
                for i in range(len(remains)):
                    path.append(remains[i])
                    helper(remains[i:], target - remains[i], path)
                    path.pop()

        helper(candidates, target, [])
        return result

        