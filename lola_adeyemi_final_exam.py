"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialization’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""

from random import randint


class CFGStudent:

    def __init__(self, name, surname, age, email, student_id=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = self.get_id()

    @staticmethod
    def generate_id():
        random_id = randint(1000, 10000) #create new student id using random
        return random_id

    def get_id(self):
        return self.generate_id()

    def get_fullname(self):
        create_fullname = (self.name.title()+" "+ self.surname.title())
        return print(create_fullname)


class NanoStudent(CFGStudent):

    def __init__(self, name, surname, email, age, specialization, course_grades=None):
        super().__init__(name, surname, email, age,)
        self.specialization = specialization
        self.course_grades = {course_grades}

    @staticmethod
    def generate_id():
        random_id = randint(1000, 10000) #create new student id using random
        id = print("NANO{}".format(random_id))
        return id
        #"Example 'NANO1234' "

    def add_new_grade(self, subject, grade):
        self.course_grades.add(subject=grade)

    def get_course_grades(self):
        return self.course_grades




############################################
#
# # # Example run
#
s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())
# returns 'Anna Smith'
print(s.student_id)
# returns '3868' or some other random number

cfg_s = NanoStudent('Software', 'Mia', 'Papandopulu', 20, 'mia@mail.com')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
#returns {'theory': 95, 'project': 78}

#
#
# """
# TASK 2
#
# Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence
# and return the sum of all even Fibonacci numbers. See more details in the task description in
# your assessment paper.
# """
#
def even_fibonacci_sum(limit):

    def fibonacci(n=limit): #note doesn't work but if this worked then rest of function should work
        fibonacci_list = []
        # if n <= 2:
        #     fibonacci(0) == 0
        #     fibonacci(1) == 1
        #     fibonacci(2) == 1
        # else:
        #     fibonacci(n-2+ n-1)
            #fibonacci_list.append(fibonacci)
        return fibonacci_list

    list = fibonacci(limit)
    sum_total = 0

    for each in list:
        if each % 2 == 0:
            sum_total += each
    return sum_total

# ##### TESTS ####
#
# print(even_fibonacci_sum(limit=10))  # should be 44
# print(even_fibonacci_sum(limit=15))  # should be 188
# print(even_fibonacci_sum(limit=1))   # should be 0
#
#
#
#
#
# """
# TASK 3
#
# Validate subsequence. Use suggested tests below to check
# correctness of your solution.
# """
#
#
#
# #### TESTS ####

def is_valid_subsequence(array1, sequence1):
    i = 0

    check = sequence1[i]

    if check in array1:
        for each in range (1,len(sequence1), 1):
            if sequence1[each] in array1:
                continue
            else:
                return False
        return True

    return False
# array1 = [5,1,22,25,6,-1,8,10]
# sequence1 = [1,6,-1,-2]
#
#print(is_valid_subsequence(array1, sequence1))  # FALSE
#
#
# array2 = [5,1,22,25,6,-1,8,10]
# sequence2 = [1,6,-1, 10]
#
# print(is_valid_subsequence(array2, sequence2))  # TRUE
#
#
# array3 = [5,1,22,25,6,-1,8,10]
# sequence3 = [25]
#
# print(is_valid_subsequence(array3, sequence3))  # TRUE
#
#
#
# """
# TASK 4
#
# WRITTEN ASSIGNMENT
#
# Write a review on how 'class Employee' can be improved.
# (See PDF document with the code example)
# """
"""""
1. In the __init_the following can be improved:
- Naming can be improved, there is self.active_status which equals is_active this can be confusing
- There is also confusion on the id variable as it is "id: and "id_" which will cause confusion
2. Error handling can be added:
- Either by raising assertion on the type or by using the try/except/finally methodology
3. Validation checking:
- When updating department or updating status it doesn't check if this is for the correct id, this can lead to overwriting the wrong information
4. Database deletion:
- For deletion it only passes through 2 variables, this will lead to an incomplete and confusing database
5. File handling:
- It doesn't close the file once the lines have been added, ensuring the file is saved aftwards should be addedd

"""