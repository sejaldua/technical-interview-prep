# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        # [1, 0, 0, 1, 0],
        # [1, 0, 1, 0, 0],
        # [0, 0, 1, 0, 1],
        # [1, 0, 1, 0, 1],
        # [1, 0, 1, 1, 0]
        testInput = [[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]]
        expected = [1, 2, 2, 2, 5]
        self.assertEqual(sorted(program.riverSizes(testInput)), expected)
        print("pass")

    def test_case_2(self):
        # [1, 0, 0, 1, 0],
        # [1, 0, 0, 0, 0],
        # [1, 0, 0, 0, 0],
        # [1, 0, 1, 0, 0],
        # [1, 1, 1, 1, 1]
        testInput = [[1, 0, 0, 1, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 1, 0, 0], [1, 1, 1, 1, 1]]
        expected = [1,10]
        self.assertEqual(sorted(program.riverSizes(testInput)), expected)
        print("pass")

test = TestProgram()
test.test_case_1()
test.test_case_2()