"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

# """
import random


class CashRegister:

    def __init__(self):

        self.total_items = {}  # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def register_request(self):  # user input for function action
        request = input("Enter key for action...Add item - A, Remove item - R, Apply discount - D,"
                        " Show Total - T , Reset - Re , Quit - Q...")
        return request

    def register(self):  # register action
        action = self.register_request()
        action_validator = action.upper()

        options = {"D": cashier.apply_discount, "A": cashier.add_item, "T": cashier.get_total,
                   "R": cashier.remove_item, "RE": cashier.reset_register, "Q": quit}

        if action_validator in options:
            return options[action_validator]()
        else:
            print("Code not recognised")
            self.register()

    def add_item(self):  # creates a random price, adds prices to total price and adds item to total_items dictionary
        new_item = input("Please enter item description: ")
        price_calculator = float(((random.randint(0, 999)) / 100))
        self.total_price += price_calculator
        self.total_items[new_item.lower()] = price_calculator
        self.register()

    def remove_item(self):  # removes item from list and from total price
        print(self.total_items)
        remove_item = input('Please enter item description to remove...')
        if remove_item in self.total_items:
            self.total_price -= self.total_items[remove_item]
            del self.total_items[remove_item.lower()]
        else:
            print('Item not found')
        print(' '.join(['Items remaining in register', format(self.total_items)]))
        self.register()

    def apply_discount(self):
        self.discount = 0.75  # discount of 25%
        for k in self.total_items:
            self.total_items[k] = round(self.total_items[k] * self.discount, 2)
        self.total_price *= 0.75
        print('25% discount applied')
        self.register()

    def get_total(self):  # calls for total items print then shows total price variable
        self.show_items()
        print(' '.join(['Total price is £', format(self.total_price, ',.2f')]))
        self.register()

    def show_items(self):  # print in a for loop
        for k in self.total_items:
            print("{}....£{}".format(k, self.total_items[k], ',.2f'))
        return

    def reset_register(self): # override register and price to empty/0 and confirm with message
        self.total_items = {}
        self.total_price = 0
        print("Register has been reset {}".format(self.total_items))
        self.register()


cashier = CashRegister()
cashier.register()

# The code runs from the register function and actions are selected through this.
# Rather than creating a dictionary of items for the cash register,
# random library has been used to created random fake prices for the items.

# EXAMPLE code run:

# ADD


"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

"""


class Student:  # parent class

    def __init__(self, name, age, id, subjects):
        self.name = name  # as string
        self.age = age  # as int
        self.id = id  # as int
        self.subjects = subjects  # as dictionary

    def display(self):
        print('Student name: {}, student age {} and student id {}'.format(self.name, self.age, self.id))


class CFGStudent(Student):  # child class

    def __init__(self, name, age, id, subjects, total_grade):
        super().__init__(name, age, id, subjects, total_grade)

    @classmethod  # Add specilisation
    def special_subject(cls):
        return ['Software']

    def display(self):  # different display as includes specilisation
        print('Student name: {}, student age {}, student id {} and specialisation - {}'
              .format(self.name, self.age, self.id, CFGStudent.special_subject()))

    def action(self):  # user input for function action
        new_request = input("Enter key for action...Add subject - A, Remove subject - R, View all subjects - V,"
                            " Overall grade - O , Quit - Q...")

        new_request_validator = new_request.upper()

        options = {"A": CFGStudent.add_subject, "V": CFGStudent.subject_display,
                   "R": CFGStudent.remove_subject, "O": CFGStudent.overall_score, "Q": quit}

        if new_request_validator in options:
            return options[new_request_validator](self)
        else:
            print("Code not recognised")
            CFGStudent.action(self)

    def add_subject(self):  # user input new subject and grade to add to dictionary
        new_subject = input('Please enter additional subject...')
        new_subject_grade = input('Please enter subject mark as a number...')
        self.subjects[new_subject.capitalize()] = new_subject_grade
        CFGStudent.action(self)

    def remove_subject(self):  # user input name of subject to remove from dictionary
        remove_subject = input('Please enter subject to remove...').capitalize()
        if remove_subject in self.subjects:
            del self.subjects[remove_subject]
        else:
            print('Subject not found')
        CFGStudent.action(self)

    def subject_display(self):  # print through subjects in a for loop
        for k in self.subjects:
            print("{},".format(k))
        CFGStudent.action(self)

    def overall_score(self):  # generates overall score
        grade = CFGStudent.grade_calculator(self.subjects)
        average_score = CFGStudent.score_cal(grade, len(self.subjects))
        print("Average score {}".format(average_score))
        CFGStudent.action(self)

    @staticmethod   # static method, receives subject dictionary and loops values
    def grade_calculator(subject_dictionary, total_grade=0):
        for k in subject_dictionary:
            total_grade += int(subject_dictionary[k])
        return total_grade

    @staticmethod   # static method, receives total grade and number of subjects and performs calculation
    def score_cal(total_grade_sum, subject_numbers):
        if subject_numbers > 1:
            overall_score = round((total_grade_sum / subject_numbers), 1)
        else:
            overall_score = float(total_grade_sum)
        return overall_score


new_student = Student("Pauline", 19, 192, {"Maths": 92})
CFGStudent.display(new_student)
CFGStudent.action(new_student)
