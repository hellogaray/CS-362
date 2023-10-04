# Course: CS 362 - Software Engineering II - Oregon State University
# Author: Leonel Garay
# Homework 02: Improving Coverage

import unittest
from contrived_func import contrived_func


class TestCase(unittest.TestCase):

    # Tests 06: uses 6, should return False.
    def test01(self):
        val = 362
        self.assertFalse(contrived_func(val),
                         msg='Invalid Result'.format(val))

    # Tests 06: uses 6, should return True.
    def test02(self):
        val = 150
        self.assertTrue(contrived_func(val),
                        msg='Invalid Result'.format(val))

    # Tests 06: uses 6, should return True.
    def test03(self):
        val = 125
        self.assertTrue(contrived_func(val),
                        msg='Invalid Result'.format(val))

    # Tests 06: uses 6, should return True.
    def test04(self):
        val = 50
        self.assertTrue(contrived_func(val),
                        msg='Invalid Result'.format(val))

    # Tests 05: uses 6, should return False.
    def test05(self):
        val = 48
        self.assertFalse(contrived_func(val),
                         msg='Invalid Result'.format(val))

    # Tests 06: uses 6, should return False.
    def test06(self):
        val = 6
        self.assertFalse(contrived_func(val),
                         msg='Invalid Result'.format(val))

    # Tests 07: uses 1, should return True.
    def test07(self):
        val = 1
        self.assertTrue(contrived_func(val),
                        msg='Invalid Result'.format(val))


if __name__ == '__main__':
    unittest.main(verbosity=2)
