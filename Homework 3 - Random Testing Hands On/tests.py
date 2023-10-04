# Course: CS 362 - Software Engineering II - Oregon State University
# Author: Leonel Garay
# Homework 03: Random Testing Hands On

import random
import string
import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    def test1(self):
        # Number of test to generate.
        tests_to_generate = 100000
        # Generate random test cases
        for i in range(tests_to_generate):
            # Prefix to use.
            prefix = random.randint(0, 3)
            # Length of the credit card number, accounting for prefix.
            length = 16 - len(str(prefix))
            digits = string.digits
            # Generate Credit Card number.
            cc_number = str(prefix) + ''.join(random.choice(digits) for i in range(length))
            credit_card_validator(cc_number)

    def test2(self):
        # Number of test to generate.
        tests_to_generate = 100000
        # Generate random test cases
        for i in range(tests_to_generate):
            # Prefix to use.
            prefix = 4
            # Length of the credit card number, accounting for prefix.
            length = 16 - len(str(prefix))
            digits = string.digits
            # Generate Credit Card number.
            cc_number = str(prefix) + ''.join(random.choice(digits) for i in range(length))
            credit_card_validator(cc_number)

    def test3(self):
        # Number of test to generate.
        tests_to_generate = 100000
        # Generate random test cases
        for i in range(tests_to_generate):
            # Possible Prefix for all 3 Credit Card Companies (Visa, MasterCard, and American Express)
            prefix_list = [4, 34, 37, random.randint(51, 55), random.randint(2221, 2720)]
            # Randomly choose one prefix from the prefix list.
            prefix = random.choice(prefix_list)
            # Length of the credit card numbers to generate, according to the chosen prefix.
            if prefix == 34 or prefix == 37:
                length = 15 - len(str(prefix))
            else:
                length = 16 - len(str(prefix))
            digits = string.digits
            # Generate Credit Card number.
            cc_number = str(prefix) + ''.join(random.choice(digits) for i in range(length))
            credit_card_validator(cc_number)


if __name__ == '__main__':
    unittest.main(verbosity=2)
