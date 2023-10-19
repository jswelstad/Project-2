import unittest
from cosmicPath import findMean


class TestEgypt(unittest.TestCase):
    def test_answer1(self) -> None:
        nums = [1, 2, 3, 4, 5]
        function_answer = findMean(nums, 5)
        expected_answer = 3
        self.assertEqual(function_answer, expected_answer,
                         f'{function_answer} != {expected_answer}')

    def test_answer2(self) -> None:
        nums = [42, 52, 32, -55]
        function_answer = findMean(nums, 4)
        expected_answer = 17
        self.assertEqual(function_answer, expected_answer,
                         f'{function_answer} != {expected_answer}')

    def test_answer3(self) -> None:
        nums = [1, 1, 1, 1, 1, 1000]
        function_answer = findMean(nums, 6)
        expected_answer = 167
        self.assertEqual(function_answer, expected_answer,
                         f'{function_answer} != {expected_answer}')

    def test_answer4(self) -> None:
        nums = [-1, 1]
        function_answer = findMean(nums, 2)
        expected_answer = 0
        self.assertEqual(function_answer, expected_answer,
                         f'{function_answer} != {expected_answer}')

    def test_answer5(self) -> None:
        nums = [1000, -1000, 10000, 1]
        function_answer = findMean(nums, 4)
        expected_answer = 2500
        self.assertEqual(function_answer, expected_answer,
                         f'{function_answer} != {expected_answer}')

    def test_answer6(self) -> None:
        nums = [69, 420, 42]
        function_answer = findMean(nums, 3)
        expected_answer = 177
        self.assertEqual(function_answer, expected_answer,
                         f'{function_answer} != {expected_answer}')


if __name__ == '__main__':
    unittest.main()
