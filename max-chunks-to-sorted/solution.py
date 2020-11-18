"""
Brute Force Approach

Let's try to find the smallest left-most chunk. If the first k elements are [0, 1, ..., k-1], then it can be broken into a chunk, and we have a smaller instance of the same problem.

We can check whether k+1 elements chosen from [0, 1, ..., n-1] are [0, 1, ..., k] by checking whether the maximum of that choice is k.

---

COMPLEXITY ANALYSIS
Time Complexity: O(N), where N is the length of arr
Space Complexity: O(1)
"""

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_elem = 0
        num_chunks = 0
        for i, val in enumerate(arr):
            max_elem = max(max_elem, val)
            if max_elem == i:
                num_chunks += 1
        return num_chunks