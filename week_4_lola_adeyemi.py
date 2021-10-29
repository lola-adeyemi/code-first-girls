#  HOMEWORK WEEK 4
# (handout for students)
"""""
Homework 4 submission from Lola Adeyemi 29/10/21 :)

Please note my answers to questions 1 are greyed out in comments

"""
# TASK 1 (Git and GitHub)
#
# Question 1
# Complete definitions for key Git & GitHub terminology
# GIT WORKFLOW FUNDAMENTALS
# ·        Working Directory - where you have checked out the project
# ·        Staging Area - place to record things before committing
# ·        Local Repo (head) - current branch where you make changes to
# ·        Remote repo (master) - used in collaboration working so you can push commits from your local branch to a
# remote repository once commits are working correctly
#
# WORKING DIRECTORY STATES:
# ·        Staged - stage where file is prepared for commit
# ·        Modified - Changes since last commit. You can select modified files and then commit all the staged changes
# ·        Committed - Snapshot of your repository at a specific time.
# It's like saving a file on Microsoft word document and you have a unique ID for the file version.
#
# GIT COMMANDS:
# ·        Git add - add new or changed files
# ·        Git commit - save changed files
# ·        Git push - upload changes to a local repository
# ·        Git fetch - download from commits from a remote repository to your local repository
# ·        Git merge - combines commits to one singular history of commits
# ·        Git pull - update the local version of a repository from a remote repository
# TASK 2 (Exception Handling)
#
# Question 1
# Simple ATM program
# Using exception handling code blocks such as try/ except / else / finally
# (NB: the more the better, but try to use at least two key words e.g. try/except)
# write a program that simulates and ATM machine to withdraw money.
# Tasks:
# 1.       Prompt user for a pin code
# 2.       If the pin code is correct then proceed to the next step, otherwise ask a user to type in a password again.
# You can give a user a maximum of 3 attempts and then exit a program.
# 3.       Set account balance to 100.
# 4.       Now we need to simulate cash withdrawal
# 5.       Accept the withdrawal amount
# 6.       Subtract the amount from the account balance and display the remaining balance
# (NOTE! The balance cannot be negative!)
# 7.       However, when a user asks to ‘withdraw’ more money than they have on their account,
# then you need to raise an error an exit the program.

# some database perhaps with user details
user_details = {"correct_pin": "3920", "account_balance": "100"}


def pin_length(input_pin):
    """""
    checks if 4 characters was entered
    :param input_pin: int, the inputted pin from user

    """
    str_input_pin = str(input_pin)
    if len(str_input_pin) != 4:
        raise ValueError


def num_check(input_pin):
    """""
    checks if numbers given
    :param input_pin: int, the inputted pin from user

    """
    if not input_pin.isnumeric():
        raise TypeError


def balance(remaining_balance):
    """""
    checks balance is greater than 0
    :param remaining_balance: int, the inputted pin from user

    """
    if remaining_balance < 0:
        raise AssertionError


def balance_check():
    try:
        withdraw = int(input('Please enter amount for withdrawal....£'))
        remaining_balance = int(user_details["account_balance"]) - withdraw
        balance(remaining_balance)
        user_details["account_balance"] = remaining_balance
    except AssertionError:
        print("Balance is not enough for withdrawal")
        exit()
    else:
        print("Your withdrawal of £{} was successful you now have £{} remaining".format(withdraw,
                                                                                        remaining_balance))


def count_check(count, input_pin):
    if count >= 3 and (input_pin != user_details["correct_pin"]):
        print("Too many attempts!")
        exit()


def pin_validator(input_pin, count):
    if input_pin == user_details["correct_pin"]:
        print("Success!")
    if count <= 2 and (input_pin != user_details["correct_pin"]):
        print("Incorrect! Please try again")


def main():
    count = 0
    while count <= 2:
        try:
            count += 1
            input_pin = input('Please enter your pin code....')
            num_check(input_pin)
            pin_length(input_pin)
            count_check(count, input_pin)
            pin_validator(input_pin, count)
            if count >= 3 or input_pin == user_details["correct_pin"]:
                break
        except TypeError:
            print("Please enter only numbers. Retry")
            count_check(count, input_pin)
        except ValueError:
            print("Please enter only 4 digits. Retry")
            count_check(count, input_pin)
        finally:
            if input_pin == user_details["correct_pin"]:
                checker = input("Would you like to make a withdrawal? Yes or No")
                c = checker.lower()[0]
                if c == 'y':
                    balance_check()
                    print("Thank you for using the bank!")
                else:
                    print("Goodbye!")


if __name__ == '__main__':
    main()
# TASK 3 (Testing)
#
# Question 1
# Use the Simple ATM program to write unit tests for your functions.
# You are allowed to re-factor your function to ‘untangle’ some logic into smaller blocks of code to make it easier to write tests.
# Try to write at least 5 unit tests in total covering various cases.

import unittest


class ATM(unittest.TestCase):

    def test_pin_length_four(self):
        self.assertRaises(ValueError, pin_length, 493)

    def test_pin_is_num(self):
        self.assertRaises(TypeError, num_check, "wue")

    def test_correct_pin_validator(self):
        expected = user_details["correct_pin"]
        result = str(3920)
        self.assertEqual(expected, result)

    def test_withdrawal_validator(self):
        checker = "YES"
        c = checker.lower()[0]
        expected = "y"
        result = c
        self.assertEqual(expected, result)

    def test_less_than_zero_balance(self):
        self.assertRaises(AssertionError, balance, -1)
#

if __name__ == "__main__":
    unittest.main()

# to run in command line please use: python -m unittest week_4_lola_adeyemi.ATM
