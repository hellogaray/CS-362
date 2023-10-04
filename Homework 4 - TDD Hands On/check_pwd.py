# Course: CS 362 - Software Engineering II - Oregon State University
# Author: Leonel Garay
# Assignment 02: TDD Hands On

from string import ascii_letters, digits


def check_pwd(password):
    """ check_pwd accepts a string and returns boolean:
    True if it meets the criteria listed, otherwise it returns False.
    """

    special_characters = '~`!@#$%^&*()_+-='  # All special characters that are permitted in a password.

    # Check the length of a password. It should be between 8-20 characters.
    if 20 >= len(password) >= 8:
        # Check if any of the characters is lowercase, if none is return False.
        if not any(char.islower() for char in password):
            return False

        # Check if any of the characters is uppercase, if none is return False.
        if not any(char.isupper() for char in password):
            return False

        # Check if any of the characters is a digit, if none is return False.
        if not any(char.isdigit() for char in password):
            return False

        # Check if any of the characters is a special character, if none is return False.
        if not any(char in special_characters for char in password):
            return False

        # Check if any of the characters is not allowed (not a digit, upper/lowercase or special character from the
        # list). If any character is found that is not listed return False.
        if set(password).difference(ascii_letters + digits + special_characters):
            return False

        else:
            return True

    return False
