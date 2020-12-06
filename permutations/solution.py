class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(combo, next_elems):
            if not next_elems:
                output.append(combo)
            else:
                for elem in next_elems:
                    new = next_elems[:]
                    new.remove(elem)
                    backtrack([*combo, elem], new)
        output = []
        if nums:
            backtrack([], nums)
        return output
