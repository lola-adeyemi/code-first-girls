"""  PYTHON AND MYSQL ASSESSMENT TEST - 2 hours  """

""" 1. Python theory questions """

# # 1.	What is the program?
# instructions to a computer typically to run processes in a certain order
#
# # 2.	What is the process?
# One thread being excuted
#
# # 3.	What is Cache?
# Temporary memory storage used to make things such as web applications faster
#
# # 4.	What is Thread and Multithreading?
#
#
# # 5.	What is GIL in Python and how does it work?
# Global interpretor lock. It only lets one thing exceute at a time
#
# # 6.	What is Concurrency and Parallelism and what are the differences?
#
#
# # 7.	What do these stand for in programming: DRY, KISS, BDUF
# DRY – don’t repeat yourself
# KISS – keep it simple stupid
# BDUF – basic design up front
#
#
# # 8.	What is Garbage collector? How does it work?
# Automated process to remove objects that are not needed
#
# # 9.	What are ‘deadlock’ and ‘livelock’ in a relational database?
#
#
# # 10.	What is Flask and what can we use it for?
# It’s a webframework for python

""" 2. Discuss the difference between Python 2 and Python 3 """

# Python 2 and 3 are not compatible. Python 3  easier to understand syntax and supports
# libraries which are used in data science. Whereas, python 2 does not support this.
# Also, with libraries there is functionality to mix python with other languages which you cannot do in python 2.

""" 3. Write a function that can define whether a word is a Palindrome 
or not (a word, phrase, or sequence that reads the same backwards as 
forwards, e.g. madam) """

# word/sequence or phrase to check should be entered in word variable or when prompt given
#
# word = " "
#
#
# def palindrome_word_checker(word):
#     if word.isspace() is True:
#         word = input("Please enter a word/phrase/sequence to check....")
#     word_check = word[::-1]
#     palindrome_true() if word == word_check else palindrome_false()
#
#
# def palindrome_true():
#     x = "This is a true palindrome"
#     print(x)
#     return x
#
#
# def palindrome_false():
#     x = "This is not a palindrome"
#     print(x)
#     return x
#
#
# if __name__ == '__main__':
#     palindrome_word_checker(word)

""" 4.	Write tests for the newly created Palindrome function.
Provide a brief explanation for your test case options. """
#
# import unittest
#
# class palindrome_test(unittest.TestCase):
#     def test_is_word_reverse_working(self):
#         word = "word"
#         word_check = word[::-1]
#         expected = "drow"
#         result = word_check
#         self.assertEqual(expected, result)
#
#     def test_check_equals_operator_works(self):
#         word_1 = '101'
#         word_2 = '101'
#         expected = True
#         result = True if word_1 == word_2 else False
#         self.assertEqual(expected, result)
#
#     def test_true_function_is_printing(self):
#         expected = "This is a true palindrome"
#         result = palindrome_true()
#         self.assertEqual(expected, result)
#
# if __name__ == '__main__':
#     unittest.main()

# The first test has been used to check that the word is being reversed properly. 
# As this is the only test used to check if a word is a Palindrome, 
# it is important to test that the main palindrome check is functioning. 
# The second test is to check that the equals operator is giving a true value,
# again as this is part fo the only palindrome check it is important to check that this is functioning correctly. 
# The final check makes sure that  a useable or understandable output is given to the user of the function.


""" 5. Agile methodology, Scrum: name at least 3 types of meetings that are 
exercised by Agile teams and describe the objective of each meeting. """

# Stand-up/daily stand up - this is a meeting where everyone in the team discusses what they are working on that day and
# if there is anything blocking the. The objective of this meeting is to make sure the team knows what everyone is
# working on and if someone is "blocked" to deliver their work then someone can help them or a new task is assigned.
# Retrospective - this meet looks back on a past sprint cycle and the team together discuss
# what could have been done better,
# what worked well and what lessons have been learnt.
# The objective of a retrospective is to help with the next sprint planning so that improvements can be made.
# Sprint Planning - this is to plan the deliverables of the next sprint cycle.
# It should make everyone clear on the tasks they need to carry out over the next sprint.
# A sprint is usually 2 -4  weeks and so this meeting plans the work for the sprint.

""" 6.	Exception handling in Python, explain what each of the following blocks 
means in the program flow:
   
    try, except, else, finally 
    
"""
#
#
# def recipe_number_check(recipe_number):
#     if not recipe_number.isnumeric():
#         raise TypeError
#
# def calculate_egg(recipe_number):
#     if 0 < recipe_number <= 50:
#         eggs = str(2)
#     elif 51 < recipe_number <100:
#         eggs = str(4)
#     else:
#         eggs = str(6)
#
#     return eggs
#
# def number_of_eggs_recipe():
#     try:
#         recipe_number = input("Please enter your recipe number.....")
#         recipe_number_check(recipe_number)
#         calculate_egg(recipe_number)
#         print(eggs)
#     except TypeError:
#         print("Number required, please try again!")
#     else:
#         if eggs > 0:
#             x = ("You need {} eggs for this wonder recipe".format(eggs))
#         else:
#             x = "Cannot calculate"
#         print(x)
#     finally:
#         print("Thanks for using the egg calculator")
#
# if __name__ == '__main__':
#     number_of_eggs_recipe()


#Try - this is for the code to try something
# Except - if an error occurs then the code handling will handle the error rather than breaking the code
# Else - if try doesn't happen then it can try this
# Finally - this will always excute
# See example above which explains this

""" 7. How can we connect a Python program (process) with a database? 
Explain how it works and how do we fetch / insert data into DB tables from a python program. """
#
# Using a API, we generate requests to get data and posts to posts data into the tables.
# Requests and JSON libraries can be used to help support this

""" 
8. Given two SQL tables below: authors and books (!!!PLEASE CHECK THE ASSESSMENT2 DOCUMENT FOR THE TABLES!!!)
●	 The authors dataset has 1M+ rows
●	 The books dataset also has 1M+ rows 
Create an SQL query that shows the TOP 3 authors who sold the most books in total!

SELECT MAX 3(author_name),
FROM AUTHORS
WHERE book_name in {
    select SUM(sold_copies) from books
    order by sold_copies
"""

"""
9.	TWO NUMBER SUM: 

●	Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 
    If any two numbers in the input array sum up to the target sum, the function should return 
    them in an array, in any order. If no tWo numbers sum up to the target sum, the function should 
    return an empty array.
    
●	Note that the target sum has to be obtained by summing two different integers in the array. 
    You cannot add a single integer to itself in order to obtain the target sum.
    
●	You can assume that there will be at most one pair of numbers summing up to the target sum. 

Sample Input: 
    numbers = [3, 5, -4 ,8, 11, 1, -1, 6]  
    target_sum = 10
    
Sample Output: 
    [-1, 11] the numbers can be in any  order, it does not matter. 

my_numbers = [3, 5, -4 ,8, 11, 1, -1, 6] 
target_sum = 10
final_numbers = []
empty_return = []
final_list = []



def number_check(a, b):
    number1 = my_numbers[a]
    number2 = my_numbers[b]
    total = number1 + number2
    return total


def remove_numbers(a, b):
    my_numbers.pop(a)
    my_numbers.pop(b)
    return my_numbers


def number_addition_check(my_numbers):
    max = len(my_numbers)-1
    while max > 2:
        for a in range(max, -1, -1):
            for b in range(0, max, 1):
                if number_check(a, b) == target_sum:
                    final_numbers = [my_numbers[a], my_numbers[b]]
                    final_list.append(final_numbers)
                    max -= 2
                    remove_numbers(a, b)
                    print(final_list)
                    break

if __name__ == '__main__':
    number_addition_check(my_numbers)
"""
