# Course: CS 362 - Software Engineering II - Oregon State University
# Author: Leonel Garay
# Assignment 02: TDD Hands On

import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    # Tests 1: empty string.
    def test1(self):
        password = ''
        self.assertFalse(check_pwd(password),
                         msg='Invalid Result'.format(password))

    # Tests 2: one character.
    def test2(self):
        password = 'a'
        self.assertFalse(check_pwd(password),
                         msg='Invalid Result'.format(password))

    # Tests 3: 21 characters.
    def test3(self):
        password = 'abcdefghijklmnopqrstu'
        self.assertFalse(check_pwd(password),
                         msg='Invalid Result'.format(password))

    # Tests 4: string with no lowercase.
    def test4(self):
        password = 'ABCDEFGHILMN'
        self.assertFalse(check_pwd(password),
                         msg='Invalid Result'.format(password))

    # Tests 5: string with no uppercase.
    def test5(self):
        password = 'abcdefghijk'
        self.assertFalse(check_pwd(password),
                         msg='Invalid Result'.format(password))

    # Tests 6: string with no digit.
    def test6(self):
        password = 'Abcdefghijk'
        self.assertFalse(check_pwd(password),
                         msg='Invalid Result'.format(password))

    # Tests 7: string with no special characters.
    def test7(self):
        password = 'Abcdefghijk1'
        self.assertFalse(check_pwd(password),
                         msg='Invalid Result'.format(password))

    # Tests 8: string with a special characters that is not allowed.
    def test8(self):
        password = 'Abcde%ghijk1|'
        self.assertFalse(check_pwd(password),
                         msg='Invalid Result'.format(password))

    # Tests 9: string with a space.
    def test9(self):
        password = 'Abcde%gh 1'
        self.assertFalse(check_pwd(password),
                         msg='Invalid Result'.format(password))


if __name__ == '__main__':
    unittest.main()
