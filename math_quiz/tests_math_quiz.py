import unittest
from math_quiz import random_int, random_calc, calc_result


class TestMathGame(unittest.TestCase):

    def test_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

        print("All test cases passed!")
        

    def test_random_calc(self):
        # Test if random operator is one of the specified characters
        add = "+"
        substract = "-"
        multiply = "*"
        for _ in range(1000):   # Test a large number of random values
            rand_op = random_calc()
            self.assertTrue(rand_op == add or rand_op == substract or rand_op == multiply)

        print("All test cases passed!")

    def test_calc_result(self):
        # Test if the right problem and output are displayed
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (2, 2, '*', '2 * 2', 4),              
            (8, 3, '-', '8 - 3', 5)
        ]   # different test cases

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            
            problem, answer = calc_result(num1, num2, operator)

            # Assert that the results match the expected outputs
            assert problem == expected_problem, f"Expected {expected_problem}, but got {problem}"
            assert answer == expected_answer, f"Expected {expected_answer}, but got {answer}"

        print("All test cases passed!")

                

if __name__ == "__main__":
    unittest.main()
