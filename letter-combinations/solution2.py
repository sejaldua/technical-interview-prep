class Solution:                
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        
        def backtrack(combo, next_digits):
            if len(next_digits) == 0:
                output.append(combo)
            else:
                for letter in phone[next_digits[0]]:
                    backtrack(combo + letter, next_digits[1:])
        
        output = []
        if digits:
            backtrack("", digits)
        return output

        