import itertools
class Solution:
    def get_dict(self):
        mappings = dict()
        c = 97
        for i in range(2, 10):
            mappings[i] = ""
            j_num = 4 if i == 7 or i == 9 else 3
            for j in range(j_num):
                mappings[i] += chr(c)
                c += 1
        return mappings
                
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        mappings = self.get_dict()
        a = []
        for digit in digits:
            a.append(list(mappings[int(digit)]))
        combos = list(itertools.product(*a))
        res = ["".join(combo) for combo in combos]
        return res
            
        