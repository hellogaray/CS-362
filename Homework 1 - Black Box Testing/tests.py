# Course: CS 362 - Software Engineering II - Oregon State University
# Author: Leonel Garay
# Homework 01: Writing Black Box Tests

import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):

    # Assignment Requirement: "Contains tests for each prefix range."
    # Verifies if prefix 4 returns True.
    def test01(self):
        cc_num = "4893701558500034"
        self.assertTrue(credit_card_validator(cc_num),
                        msg='Invalid Input'.format(cc_num))

    # Assignment Requirement: "Contains tests for each prefix range."
    # Verifies if prefix 34 returns True.
    def test02(self):
        cc_num = "349676468640278"
        self.assertTrue(credit_card_validator(cc_num),
                        msg='Invalid Input'.format(cc_num))

    # Assignment Requirement: "Contains tests for each prefix range."
    # Verifies if prefix 37 returns True.
    def test03(self):
        cc_num = "370008887203763"
        self.assertTrue(credit_card_validator(cc_num),
                        msg='Invalid Input'.format(cc_num))

    # Assignment Requirement: "Contains tests for each prefix range."
    # Verifies if prefix 51 returns True.
    def test04(self):
        cc_num = "5172075604803406"
        self.assertTrue(credit_card_validator(cc_num),
                        msg='Invalid Input'.format(cc_num))

    # Assignment Requirement: "Contains tests for each prefix range."
    # Verifies if prefix 55 returns True.
    def test05(self):
        cc_num = "5574235628830223"
        self.assertTrue(credit_card_validator(cc_num),
                        msg='Invalid Input'.format(cc_num))

    # Assignment Requirement: "Contains tests for each prefix range."
    # Verifies if prefix 2221 returns True.
    def test06(self):
        cc_num = "2221075604803404"
        self.assertTrue(credit_card_validator(cc_num),
                        msg='Invalid Input'.format(cc_num))

    # Assignment Requirement: "Contains tests for each prefix range."
    # Verifies if prefix 2720 returns True.
    def test07(self):
        cc_num = "2720075604800018"
        self.assertTrue(credit_card_validator(cc_num),
                        msg='Invalid Input'.format(cc_num))

    # Verifies if a number lower than 10 digit  returns False.
    # Picked using Boundary Testing
    def test08(self):
        cc_num = "4324415159"
        self.assertFalse(credit_card_validator(cc_num),
                         msg='Invalid Input'.format(cc_num))

    # Verifies if an empty string  returns False.
    # Picked using Boundary Testing
    def test09(self):
        cc_num = ""
        self.assertFalse(credit_card_validator(cc_num),
                         msg='Invalid Input'.format(cc_num))

    # Verifies if a number higher than 19 digits  returns False.
    # Picked using Boundary Testing
    def test10(self):
        cc_num = "42918374859302340005"
        self.assertFalse(credit_card_validator(cc_num),
                         msg='Invalid Input'.format(cc_num))

    # Verifies if a number that starts with an invalid lower prefix returns False.
    # Picked using Category Partition Testing
    def test11(self):
        cc_num = "3000000004"
        self.assertFalse(credit_card_validator(cc_num),
                         msg='Invalid Input'.format(cc_num))

    # Verifies if a Visa number with an invalid length returns False.
    # Picked using Category Partition Testing
    def test12(self):
        cc_num = "412345678912008"
        self.assertFalse(credit_card_validator(cc_num),
                         msg='Invalid Input'.format(cc_num))

    # Verifies if a MasterCard number with an invalid length returns False.
    # Picked using Category Partition Testing
    def test13(self):
        cc_num = "22215678901230001"
        self.assertFalse(credit_card_validator(cc_num),
                         msg='Invalid Input'.format(cc_num))

    # Verifies if an American Express number with an invalid length returns False.
    # Picked using Category Partition Testing
    def test14(self):
        cc_num = "3434567890120007"
        self.assertFalse(credit_card_validator(cc_num),
                         msg='Invalid Input'.format(cc_num))

    # Verifies if a number outside allowed prefixes (low end) returns False.
    # Picked using Category Partition Testing
    def test15(self):
        cc_num = "30569309025904"
        self.assertFalse(credit_card_validator(cc_num),
                         msg='Invalid Input'.format(cc_num))

    # Verifies if a number outside allowed prefixes (high end) returns False.
    # Picked using Category Partition Testing
    def test16(self):
        cc_num = "93090259042728"
        self.assertFalse(credit_card_validator(cc_num),
                         msg='Invalid Input'.format(cc_num))


if __name__ == '__main__':
    unittest.main(verbosity=2)
