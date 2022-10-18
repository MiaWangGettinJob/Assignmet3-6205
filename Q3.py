class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "" or digits == "1":
            return []
        result = []

        Map = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]  }

        def backtrack(first, path):
            if first == len(digits):
                result.append("".join(path[:]))
                return
            current = Map.get(digits[first])

            for i in range(len(current)):
                path.append(current[i])

                backtrack(first + 1, path)
                path.pop()

        backtrack(0, [])
        return result

        