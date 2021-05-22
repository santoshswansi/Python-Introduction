import concurrent.futures  # Threading + Multi-Processing
import csv
import itertools
import logging
import multiprocessing
import operator
import os
import subprocess
import threading
import time
from contextlib import contextmanager
from functools import wraps
from PIL import Image, ImageFilter

import requests

# LIST COMPREHENSIONS :
# ____________________

nums = [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# We want n for each n in nums ( USING FOR LOOP ) :
# _________________________________________________
my_list = []
for x in nums:
    my_list.append(x)
print("List without list comprehension : {} ".format(my_list))

# ITS LIST COMPREHENSION EQUIVALENT :
# _________________________________
my_list = [n for n in nums]  # [] ---> Means we want a list
print("List using list comprehension : {}".format(my_list))

# EXAMPLE - 1: Get all the squares of numbers in nums :
# _____________________________________________________
my_list = [n * n for n in nums]
print("Squares : {}".format(my_list))

# EXAMPLE - 2: Get all squares using map() and lambda function :
# ______________________________________________________________
# map(function, iterable_object) : Returns a list by applying function
# on each item in iterable_object
my_list = map(lambda n: n * n, nums)
print("Squares : {}".format(list(my_list)))

# EXAMPLE - 3: Print even numbers from the list :
# ____________________________________________
my_list = [n for n in nums if n % 2 == 0]
print("Even numbers : {}".format(my_list))

# Using filter() and lambda function :
# Returns an iterator
# _______________________________________
my_list = filter(lambda n: n % 2 == 0, nums)
print("Squares using filter() and lambda: {} ".format(list(my_list)))

# EXAMPLE - 4: Print all possible pairs :
# ____________________________________
my_pairs_list = [(n, m) for n in nums for m in nums]
print("All possible pairs : {}".format(my_pairs_list))

# DICTIONARY COMPREHENSIONS :
# ___________________________

names = ["Manika", "Alok", "Utkarsh", "Sushant", "Rhea"]
rollCodes = [123, 124, 125, 126, 127]

# zip returns tuple object of (names[i], rollCodes[i])
print("Without dict comprehension : {}".format(dict(zip(names, rollCodes))))

# Make a dictionary of {'name' : 'rollCode'} for each name, rollCode
# in zip(names, rollCodes) :
# ___________________________________________________________________
my_dict = {}
for name, rollCode in zip(names, rollCodes):
    my_dict[name] = rollCode
print("Without Using dict comprehension : {}".format(my_dict))

# Dictionary Comprehension :
# __________________________
my_dict = {name: rollCode for name, rollCode in zip(names, rollCodes)}
print("Using dict comprehension : {}".format(my_dict))

my_dict = {name: rollCode for name, rollCode in zip(names, rollCodes) if name != "Alok"}
print("Using dict comprehension(Name not = Alok) : {}".format(my_dict))

# SET COMPREHENSION :
# ____________________
my_set = {n for n in nums}
print("set from nums list : {}".format(my_set))

# GENERATORS IN PYTHON:
# _____________________
# I want n*n for each n in nums
# It give us result one at a time
# It quite good in performance (space + time)

nums = [1, 2, 4, 5, 6, 7, 8, 9, 10]


def gen_function(nums):
    for n in nums:
        yield n * n


print(end="\n\n")
my_gen = gen_function(nums)
for x in my_gen:
    print(x)

# It is also equivalent to :
# __________________________
my_gen = (n * n for n in nums)  # returns an iterator
# print(list(my_gen)) is not performance(space & time) friendly
for i in my_gen:
    print(i)


# FIRST CLASS FUNCTIONS :
# _______________________
# We should be able to treat function like any other variable

def square(val):
    return val * val


f = square  # We are assigning function to a variable

print(f(2))  # print square of 2


# INSTANCE VARIABLES V/S CLASS VARIABLES :
# _______________________________________
class Student:
    total_students = 0  # class variable
    gender = "m"  # default gender is "male"

    def __init__(self, first_name, last_name, roll):
        self.first_name = first_name  # instance variable
        self.last_name = last_name
        self.roll = roll  # instance variable
        Student.total_students += 1  # class variable gets updated

    def fullname(self):
        print("{} {}".format(self.first_name, self.last_name))

    def email(self):
        print("{}.{}@email.com".format(self.first_name, self.last_name))


# Creating object of class
student_1 = Student("Santosh", "Swansi", 732)
student_2 = Student("Kalki", "Kumari", 849)

# Changing gender of student_2 to 'f' explicitly
student_2.gender = 'f'
print(student_2.gender)

student_1.email()
student_1.fullname()

student_1.first_name = "Subhash"

student_1.email()
student_1.fullname()

# To get dictionary of variables in instance student_1 of class Student
print(student_1.__dict__)

# To get dictionary of variables and functions in class Employee
print(Student.__dict__)
print(end="\n\n")


# CLASS AND STATIC METHODS :
# ____________________________

# STATIC METHODS :
# _________________
# 1.) Static methods are bound to a class rather than the objects for that class
# 2.) This means static method can be called without an object of the class
# 3.) This also means static methods can not modify the state of the object
#     as they are not bound to it.

# CLASS METHODS:
# _______________
# 1.) Class methods are bound to a class rather than the objects for that class
# 2.) It can modify class state that would apply across all the instances
#     of the class
# 3.) It accepts class(cls by convention) parameter that points to the
#     class and not the object instance

# STATIC V/S CLASS METHODS :
# ___________________________
# 1.) Class method takes cls as first parameter while static method
#     needs no specific parameters
# 2.) We use @staticmethod AND @classmethod are used to create static
#     AND class methods respectively.
# 3.) Static methods are utility type methods which takes some parameters
#     and work upon these parameters WHILE class methods must have class
#     as decorator.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year
    @classmethod
    def from_birth_year(cls, name, year):
        from datetime import date
        # pass name name and age with given year
        return cls(name, date.today().year - year)

    # Static method if a person is adult or not
    @staticmethod
    def isAdult(age):
        return age > 18


person_1 = Person("Jason", 23)
# Creating Person object from given year using class method
person_2 = Person.from_birth_year("Mayank", 2002)

print(person_1.age)
print(person_2.age)

# Is given age valid to vote
print(Person.isAdult(23))
print(end="\n\n")


# DUNDER(DOUBLE UNDERSCORES) or MAGIC METHODS :
# ______________________________________________
# This can be used to do operator overloading

# __str__ V/S __repr :
# _____________________


class Store:
    # special method to initialise instance variables
    def __init__(self, name, location, established_year, net_income):
        self.name = name
        self.location = location
        self.established_year = established_year
        self.net_income = net_income

    # It is meant to be unambiguous representation of the object
    # It is meant for developer
    def __repr__(self):
        return "Store({}, {}, {})".format(self.name, self.location, self.established_year)

    # It is meant for readable representation of the object
    # It is meant for end-user
    def __str__(self):
        from datetime import date
        return "(name, age):({}, {})".format(self.name + ", " + self.location,
                                             date.today().year - self.established_year)

    # Illustration of operator overloading :
    # ______________________________________
    def __add__(self, other):
        return self.net_income + other.net_income


# If we print object without __str__() and __repr__() then it will
# print vague set of strings
# BUT with them we can print the object as we want to

store_1 = Store("Apple Store", "Silicon Valley", 2003, 8242572889)
store_2 = Store("Samsung Store", "Tokyo", 2010, 5036362826)

# They will use __str__() method to print objects if it exist
# otherwise they will use __repr__() method
print(store_1)
print(store_2)

# Adding two objects here will call special method __add__() if exist
# Otherwise produce error
print("Total Net Income of both stores : {}".format(store_1 + store_2))
print(end="\n\n")


# PROPERTY DECORATORS (GETTER, SETTER AND DELETER) :
# __________________________________________________
# It allows to define a method and access it as an attribute
# It is a way to implement method overloading in Python

class Animal:
    def __init__(self, name, year, gender):
        self.name = name
        self.year = year
        self.gender = gender

    # This method can be used as an attribute
    @property
    def age(self):
        from datetime import date
        return date.today().year - self.year

    # Setter allows us to modify the function as an attribute
    @age.setter
    def age(self, new_age):
        from datetime import date
        self.year = date.today().year - new_age

    # Deleter allows us to delete the age of the object
    @age.deleter
    def age(self):
        print("Deleting age")
        self.year = None


animal_1 = Animal("Pussy", 2009, "m")
animal_2 = Animal("Tag", 2016, "f")

# Using method as an attribute
print("Age of {} is {}".format(animal_1.name, animal_1.age))

# Modifying age of animal_1
# It will modify the date of birth of the animal_1
# It will go to setter method
animal_1.age = 23

print("Age of {} is {}".format(animal_1.name, animal_1.age))
print("Date of birth of {} is {}".format(animal_1.name, animal_1.year))

# delete the age of animal_1
# del animal_1.age
del animal_1.age
print("Date of birth of {} is {}".format(animal_1.name, animal_1.year))
print(end='\n\n')

# LOGGING BASICS :
# _________________
#       Level                          When it’s used
# _______________________________________________________________________
#       DEBUG            Detailed information, typically of interest
#                                 only when diagnosing problems.
#                                  Integer value : 10

#       INFO           Confirmation that things are working as expected.
#                                  Integer value : 20

#     WARNING          An indication that something unexpected happened,
#                      or indicative of some problem in the near future
#                      (e.g. ‘disk space low’).
#                      The software is still working as expected.
#                                  Integer value : 30

#     ERROR            Due to a more serious problem, the software
#                      has not been able to perform some function.
#                                  Integer value : 40

#    CRITICAL          A serious error, indicating that the program
#                        itself may be unable to continue running.
#                                  Integer value : 50
# ___________________________________________________________________

# DEFAULT LEVEL  :       WARNING, This means program will log
#                                WARNING and higher!

#  EXAMPLE :
# ___________

# Setting Basic Configurations
logging.basicConfig(filename='employee.log', level=logging.DEBUG
                    , format='%(lineno)d:%(levelname)s:%(name)s:%(asctime)s:%(message)s')


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        logging.info('Created employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee("Kamlesh", "Singh")
emp2 = Employee("Kamini", "Gupta")

# LOGGING ADVANCED :
# __________________

# custom logger
# __name__ = __main__  IF   : This is the main file where it started
#                     ELSE  : module's name
logger = logging.getLogger(__name__)

# set level to the custom logger
logger.setLevel(logging.DEBUG)

# creating formatter
formatter = logging.Formatter('%(lineno)d:%(levelname)s:%(name)s:%(asctime)s:%(message)s')

# creating a file handler of particular name
file_handler = logging.FileHandler('sample.log')

# To print logging info to console :
# ___________________________________
# creating stream handler
stream_handler = logging.StreamHandler()

# adding file handler to the custom logger
logger.addHandler(file_handler)

# adding stream handler to the custom logger
logger.addHandler(stream_handler)

# setting formatter to the file handler
file_handler.setFormatter(formatter)

# setting formatter to the stream handler
stream_handler.setFormatter(formatter)


class TechStore:

    def __init__(self, name, city):
        self.name = name
        self.city = city

        logger.debug('Tech Store created : {} -{}'.format(self.email, self.fullname))

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.name, self.city)

    @property
    def fullname(self):
        return '{}, {}'.format(self.name, self.city)


techStore1 = TechStore('Apple Store', 'California')
techStore2 = TechStore('Samsung Store', 'New York')


# Error logging :
# _________________-
def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        # for simple error info
        # logger.error('Tried to divide by zero!')
        # To print detailed error info
        logger.exception('Tried to divide by zero!')
    else:
        return result


num1 = 10
num2 = 0

division_result = division(num1, num2)
print(end='\n\n')

# __name__ is a special variable in Python which has the value :-
# 1.) __main__      : IF the file is the main file
# 2.) module's name : IF the file is imported
print(__name__, end='\n\n')

# NAMED TUPLES :
# _______________
from collections import namedtuple

# Tuple to represent RGB color value
color_tuple = (55, 155, 255)

# Dictionary to represent RGB color value
color_dict = {
    'red': 55,
    'green': 155,
    'red': 255
}

# Named Tuple to represent RGB color value :
# __________________________________________
Color = namedtuple('Color', ['red', 'green', 'blue'])

color = Color(55, 155, 255)  # OR Color(red=55, green=155, red=255)

# Ways to print values in a named tuple
print(color[0])
print(color.blue)
print(end='\n\n')


# HIGHER ORDER FUNCTIONS :
# _________________________
# When function :-
#               1.) Accepts function as arguments OR
#               2.) Returns function as result
# e.g : map(function, iterable_object)


# EXAMPLE OF PASSING FUNCTION IN A FUNCTION  :
# __________________________________________________________

# function passed to the custom map function :
def my_square(val):
    return val * val


def my_cube(val):
    return val * val * val


# Custom map()
def my_map(func, args_list):
    result = []
    for val in args_list:
        result.append(func(val))
    return result


squares = my_map(my_square, [1, 2, 3, 4, 5])
cubes = my_map(my_cube, [1, 2, 3, 4, 5])
print(squares)
print(cubes)


# EXAMPLE OF A FUNCTION RETURNING FUNCTION :
# ___________________________________________

def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text


print_h1 = html_tag("h1")  # print_h1 = wrap_text(msg)
print_h1("This is the header!")  # It remembers the tag we passed before
print_h1("This is the header-2")

print_body = html_tag("body")
print_body("This is the body!")


# CLOSURES :
# __________
# A closure is a nested function which has some access to free variable
# Characteristics :
# __________________
# 1.) It is a nested function
# 2.) It has some access to free variable in outer scope
# 3.) It is returned from the enclosing function

# EXAMPLE :
# __________
def print_msg(first_name):
    msg = f'Hello {first_name}'

    def build_msg():
        return msg

    return build_msg


msg = print_msg("Santosh")
print(msg())  # msg remembers the previously passed in values
print(end="\n\n")


# DECORATORS :
# ______________
# They are callable because they can be called
# They are callable which returns callable
# It accepts a function as an argument, add some kind of functionality
# to it and returns it


# META-PROGRAMMING :
# Using some part of the code to modify other part of the code is
# known as meta-programming

# EXAMPLE :
# __________
def decorator_func(original_func):
    # It accepts any number of positional and keyword arguments
    def wrapper_func(*args, **kwargs):
        # This will add some functionality to original_func
        print("wrapper_func added functionality to {}".format(original_func.__name__))
        return original_func(*args, **kwargs)

    return wrapper_func


@decorator_func  # same as : display = decorator_func(display)
def display():
    print("Display function ran!")


@decorator_func
def display_info(name, age):
    print("display_info function ran with arguments {} and {}".format(name, age))


display()
display_info("Sam", 23)
print(end="\n\n")


# DECORATORS USING CLASS : (Equivalent to above set of codes using class)
# _______________________________________________________________________
class DecoratorClass(object):
    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        # Add some code to existing function display
        print("__call__ added functionality to {}".format(self.original_func.__name__))
        return self.original_func(*args, **kwargs)


@DecoratorClass
def display():
    print("display function ran!")


@DecoratorClass
def display_info(name, age):
    print("display_info function ran with arguments {} and {}".format(name, age))


display()
display_info("Sam", 23)
print(end="\n\n")


# PRACTICAL EXAMPLES :
# ____________________

# 1.) Logging what have been passed to function each time we call it
def my_logger(original_func):
    # logging will use previous setting, no overidding
    # will happen!
    # import logging
    # logging.basicConfig(filename='decoratorExample.log', level=logging.DEBUG,
    #                     format='%(lineno)d:%(levelname)s:%(name)s:%(asctime)s:%(message)s')

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        logging.info('Logging passed params to a function :-')
        logging.info('Ran with args: {} and kwargs: {}'.format(args, kwargs))
        return original_func(*args, **kwargs)

    return wrapper


# Decorating this function with my_logger function
@my_logger  # Same as display_info = my_logger(display_info)
def display_info(name, age):
    print('display_info ran with {} and {}'.format(name, age))


display_info("Sam Smith", 24)
display_info("Kalki Koechlin", 35)


# 2.) Time taken by a function each time it ran
def my_timer(original_func):
    @wraps(original_func)  # to wrap or add functionality to original_func
    def wrapper(*args, **kwargs):
        import time
        t1 = time.time()
        result = original_func(*args, **kwargs)
        t2 = time.time()
        print('Time taken by {} is {}'.format(original_func.__name__, t2 - t1))
        return result

    return wrapper


@my_timer
def sum_of_natural_nos(n):
    result = 0
    for count in range(n):
        result += (i + 1)
    return result


print('Sum of 1-1000000 is {}.'.format(sum_of_natural_nos(1000000)))


# APPLYING BOTH DECORATORS TO SAME FUNCTION :
# _____________________________________________
# We can do this by stacking one decorator above the other

# It is same as : display_store_info = my_timer(my_logger(display_store_info))
@my_logger
@my_timer
def display_store_info(name, established):
    import time
    time.sleep(2)
    print('{} is established in {}'.format(name, established))


display_store_info('Apple Store', 2009)
print(end='\n\n')


# DECORATOR ARGUMENTS :
# _____________________
# It allow us to pass prefix argument to display_my_name function
def prefix_decorator(prefix):
    def decorator_function(original_func):
        def wrapper(*args, **kwargs):
            print(prefix, 'Executed before {}'.format(original_func.__name__))
            result = original_func(*args, **kwargs)
            print(prefix, 'Executed after {}'.format(original_func.__name__))
            return result

        return wrapper

    return decorator_function


@prefix_decorator('TESTING:')
def display_my_name(first_name, last_name):
    print("{} {}".format(first_name, last_name))


display_my_name('Santosh', 'Swansi')

# CONTEXT MANAGERS :  (It contains with statement)
# ___________________

# f = open('sample.txt', 'w')
# f.write('Added contents')
# f.close()

# Above set of codes is equivalent to following set of codes but we do
# not need to close manually when we are done with it:
# ______________________________________________________________________
# 1.) Method one with open() function:
# ______________________________________
with open('sample.txt', 'w') as f:
    f.write('Added contents using open() function!')


# 2.) Custom Context Manager using Class :
# __________________________________________
class OpenFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with OpenFile('sample.txt', 'a') as f:
    f.write('\nAdded contents using class!')

print(f.closed)  # To get whether the file is closed or not


# 2.) Custom Context Manager using Function :
# __________________________________________

@contextmanager
def open_file(filename, mode):
    try:
        file = open(filename, mode)
        yield file
    finally:
        file.close()


with open('sample.txt', 'a') as file:
    file.write('\nAdded contents using Function!')

print(file.closed)


# PRACTICAL EXAMPLE :
# ____________________

# How to do following set of codes using context manager ?
# _________________________________________________________________________

# cwd = os.getcwd()
# os.chdir('new_directory_1')
# print(os.listdir())
# os.chdir(cwd)

# cwd = os.getcwd()
# os.chdir('new_directory_2')
# print(os.listdir())
# os.chdir(cwd)


# Context Manager Equivalent :
# ____________________________
@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        # It will provide us time to do something with the changed directory
        yield
    finally:
        os.chdir(cwd)


print(end='\n\n')

with change_dir('test_folder'):  # nothing is being yield
    print('Files in {} is/are {}'.format('test_folder', os.listdir()))

with change_dir('test_folder2'):
    print('Files in {} is/are {}'.format('test_folder2', os.listdir()))

print(end='\n\n')

# TOP TIPS AND TRICKS TO WRITE BETTER CODE :
# _____________________________________________

# TERNARY CONDITION :
# _____________________
age = 18
is_valid_age = True if age >= 18 else False
print(is_valid_age)
print(end='\n\n')

# SEPARTING NUMBERS WITH UNDERSCORE FOR BETTER READABILITY :
# __________________________________________________________
one_million = 1_000_000
one_billion = 1_000_000_000

print('One Million = {}'.format(one_million))
print(f'One Million = {one_million:,}')  # To print comma using f string

print('One Billion = {}'.format(one_billion))
print(f'One Billion = {one_billion:,}')  # To print comma using f string
print(end='\n\n')

# Print indexes and item using enumerate() :
# __________________________________________
names = ['Santosh', 'Subhash', 'Sangeeta', 'Sachin', 'Sonu', 'Sunita']

# To start with 1 we can use start attribute
for index, name in enumerate(names, start=1):
    print(index, name)
print('\n\n')

# Looping over multiple list using zip()
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')

print(end='\n\n')

# DIFFERENT WAYS OF UNPACKING :
# _______________________________
a, _ = (1, 2)  # If we want to avoid second variable _ is used
print(a)
print(end='\n\n')

# a, b, c = {1, 2, 3, 4, 5}  # Error
a, b, *c = {1, 2, 3, 4, 5}
print(a)  # a = 1
print(b)  # b = 2
print(c)  # c = {3, 4, 5}
print(end='\n\n')

a, b, *_ = {1, 2, 3, 4, 5}  # Not gonna use {3, 4, 5}
print(a)
print(b)
print(end='\n\n')

a, b, *c, d = {1, 2, 3, 4, 5, 6}
print(a)  # a = 1
print(b)  # b = 2
print(c)  # c = {3, 4, 5}
print(d)  # d = 6
print(end='\n\n')

a, b, *_, d = {1, 2, 3, 4, 5, 6}  # not gonna use {3, 4, 5}
print(a)  # a = 1
print(b)  # b = 2
print(d)  # d = 6
print(end='\n\n')


# Dynamically setting attribute of class using variable name :
# ____________________________________________________________
class Name:
    pass


name = Name()

first_key = 'first'
first_val = 'Santosh'
last_key = 'last'
last_val = 'Swansi'

# Setting attribute of person object
setattr(name, first_key, first_val)
setattr(name, last_key, last_val)

# Getting attribute of person object :
first = getattr(name, first_key)
last = getattr(name, last_key)
print(f'{first} {last}')

# Example
my_dict = {'zodiac': 'aquarious', 'other_name': 'Basudev'}
for key, value in my_dict.items():
    setattr(name, key, value)

zodiac = getattr(name, 'zodiac')
other_name = getattr(name, 'other_name')
print(f'(Zodiac, Other name) = ({zodiac}, {other_name})')
print(end="\n\n")

# GETTING PASSWORD FROM USER :
# _____________________________
"""
   username = input('Username: ')
   password = getpass('Password: ')  # run on command line
   print('Logging In...')
"""

# TYPING SYSTEM :
# ________________

# DYNAMIC TYPING :
# _________________
"""
 In Dynamic typing, type checking is done at run-time.
 For example:
 ------------- 
 --> Python is a dynamically typed language.
 --> It means type of a variable changes over its lifetime.
"""

# STATIC TYPING :
# _______________
"""
  In static typing, type is checked at compile time.
  For example :
  ---------------
  --> C++ is a statically typed language.
  --> This means type of a variable cannot change over its lifetime.
"""

# DUCK TYPING :
# ___________________
"""
 --> It is a concept related to dynamic typing, where the type of object
    is less important than the method it defines.
 --> Using duck typing, we do not check types at all.
     Instead we check for the presence of a given attribute or method.
 --> REASON : "If it looks like a duck, quacks like a duck, swims like 
               a duck, then it probably is a duck"    
"""


class Duck:
    def quack(self):
        print("Quack, quack")

    def swim(self):
        print("Swim, swim")


class Person:
    def quack(self):
        print("I Quack like a duck")

    def swim(self):
        print("I know how to swim")


def quack_and_swim(obj):
    # not duck-typed (Non-Pythonic)
    """
        if isinstance(obj, Duck):
          obj.quack()
          obj.swim()
        else:
        print("Passed object is not of type Duck!")
    """

    # Duck Typed :
    # ____________
    # We do not care about what type of object is passed to the function
    # But it is error prone. To avoid we use the concept of EAFP

    """
       obj.quack()
       obj.swim()

       print(end="\n")
    """

    # NON PYTHONIC :
    # ______________
    # LBYL (Look Before You Leap) :
    # ______________________________
    # We first check the presence of attributes we are looking for
    # then we execute them (if present)
    """
        if hasattr(obj, 'quack'):
           if callable(obj.quack):
              obj.quack()

        if hasattr(obj, 'swim'):
           if callable(obj.swim):
              obj.swim()
    """

    # PYTHONIC WAY :
    # ______________
    # EAFP (It is Easier to Ask for Forgiveness than Permission) :
    # ____________________________________________________________
    # We try to execute the methods and if it does not contain them
    # we will be raising error!

    # Advantages :
    # It is faster when there are lesser number of errors expected!
    # It is more readable
    try:
        obj.quack()
        obj.swim()
        obj.bark()
    except AttributeError as e:
        print(e)
    print(end="\n")


duck_obj = Duck()
quack_and_swim(duck_obj)

person_obj = Person()
quack_and_swim(person_obj)

# EXAMPLES (LBYL v/s EAFP):
# _________________________

# EXAMPLE - 1 :
# ______________
student_dict = {'name': 'Santosh', 'roll': 732, 'gender': 'male'}

# Non-Pythonic Way (LBYL):
# __________________
"""
  if 'name' in student_dict and 'roll' in student_dict and 'gender' in student_dict:
    print("I am a {gender} student having name {name} and roll {roll}".format(**student_dict))
"""

# Pythonic Way (EAFP):
# __________________

try:
    print("I am a {gender} student having name {name} and roll {roll} and studying at {school}".format(**student_dict))
except KeyError as e:
    print('Missing some keys')
print(end='\n\n')

# EXAMPLE - 2 :
# ______________
my_list = [1, 2, 3, 4, 5, 6]

# non-pythonic :
"""
    if len(my_list >= 6):
        print(my_list[5])
"""

# pythonic :
try:
    print(my_list[5])
except IndexError as e:
    print(e)

# RACE CONDITION :
# ________________
# A race condition is an undesirable situation that occurs when a
# device or system attempts to perform two or more operations
# at the same time, but because of the nature of the device or system
# the operations must be done in the proper sequence to be done
# correctly.
# Example : Multiple switches connected to the same ceiling light
#           If we try to press both switches at the same time, then
#           it may trip the circuit breaker


my_file = "/test_folder/test1.txt"

# RACE CONDITION (non - pythonic ):
"""
if os.access(my_file, os.R_OK):  # if file is ok
    with open(my_file) as f:
        print(f.read())
else:
    print("File cannot be accessed!")
"""

# NO RACE CONDITION (pythonic ):
try:
    f = open(my_file)
except IOError as e:
    print("File cannot be accessed!")
else:
    with f:
        print(f.read())


# UNIT TESTING :
# _______________
# EXAMPLE - 1:
def add(op1, op2):
    return op1 + op2


def sub(op1, op2):
    return op1 - op2


def multiply(op1, op2):
    return op1 * op2


def divide(op1, op2):
    if op2 == 0:
        raise ZeroDivisionError
    else:
        return op1 / op2


# EXAMPLE - 2:
class Employee:
    pay_raise = 1.05  # 5 percent

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property
    def username(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def email(self):
        return f'{self.first_name}.{self.last_name}@gmail.com'

    def apply_raise(self):
        self.pay = self.pay * Employee.pay_raise

    # Mocking
    # ________
    # There may the reason of website failure for fail of test cases
    # But we want the test cases to fail only when our code fails
    # to do what it is supposed to do
    # To avoid this we use mocking to mock the result of the website
    def monthly_schedule(self, month):  # get the schedule of a month
        response = requests.get(f'http://company.com/{self.last_name}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'


print(end='\n\n')

# ITERTOOLS :
# _____________
# It contains a number of iterators and functions to combine several
# iterators

# 1.) count() : Start with 0 and increase by 1 and can go forever
counter = itertools.count(start=2, step=2)  # print even no. from 2
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# Use :
data = [100, 200, 300, 400, 500]
# zip pair up-to shortest iterables
daily_data = list(zip(itertools.count(), data))
print(daily_data)

# 2.) zip_longest :
# __________________
# zip_longest pair up iterables up-to longest iterables and None
# is placed where there  is absence of data
daily_data = list(itertools.zip_longest(range(8), data))

print(daily_data)

# 3.) cycle() :
# _____________
daily_data = itertools.cycle([1, 2])
print(next(daily_data))  # 1
print(next(daily_data))  # 2
print(next(daily_data))  # 1
print(next(daily_data))  # 2
print(next(daily_data), end='\n\n')  # 1

# 4.) repeat() :
daily_data = itertools.repeat(1, times=3)  # repeat 1 three times
print(next(daily_data))
print(next(daily_data))
print(next(daily_data), end='\n\n')

# Using repeat() to get cube of first 10 numbers
daily_data = map(pow, range(1, 11), itertools.repeat(3))
print(list(daily_data), end='\n\n')

# 5.) starmap() : Takes list of tuples as iterable
daily_data = itertools.starmap(pow, [(1, 2), (2, 2), (3, 2)])
print(list(daily_data), end='\n\n')

# 6.) permutations()  : Order does matter
# 7.) combinations()  : Order does not matter
letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3]
fruits = ['Apple', 'Banana', 'Litchi']

# possible fruits juices using two fruits
possible_fruit_juice = itertools.combinations(fruits, 2)
print(list(possible_fruit_juice), end='\n\n')

# possible dictionary of words using above list of letters
# of len = 3 without repeating single letter twice or more
possible_dict = itertools.permutations(letters, 3)
print(list(possible_dict), end='\n\n')

# 8.) product():

# --> All possible arrangements of pass-code of 3 numbers with repeat
# --> Product(numbers, repeat=3) returns cartesian product of
#     [1,2,3] three times
possible_codes = itertools.product(numbers, repeat=3)
print(list(possible_codes), end='\n\n')

# 9.) combination_with_replacements() :
#     Returns all possible combinations with repeat
possible_codes = itertools.combinations_with_replacement(numbers, 3)
print(list(possible_codes))

# 10.) chain() : It will loop through each iterables one by one
combined = itertools.chain(letters, numbers, fruits)
print(list(combined), end='\n\n')

# 11.) islice(iterable, start, end, step) :
#      It is used to slice the iterable
#      Only one argument : start
#      Two arguments  : start, end
#      Three arguments : start, end, step

result = itertools.islice(letters, 1, 5, 2)
print(list(result), end='\n\n')  # ['b', 'd']

# slice first three lines of the log file
with open('some_log.log', 'r') as f:
    # file object is also an iterator, calling next on them
    # give us next line
    header = itertools.islice(f, 3)

    for line in header:
        print(line, end='')

# ___________________
print(end='\n')
# ___________________

# 12.) compress(iterable, true_false_iterable):
#      It will give us an iterable of items which has corrsponding
#      True value in true_false_iterable!

data_s = [1, 2, 3, 4]
selectors = [True, False, True, True]

selected_items = itertools.compress(data_s, selectors)
print(list(selected_items))

# ___________________
print(end='\n')
# ___________________

# 13.) filterfalse(function, iterable) :
# Returns an iterable of items if applying function on item returns False
ages = [18, 23, 8, 101, 54, 23, 14, 8, 1, 7]


def is_valid_age(age):
    if age >= 18:
        return True
    else:
        return False


# Print valid ages using filter()
valid_ages = filter(is_valid_age, ages)
print(list(valid_ages))

# ___________________
print(end='\n')
# ___________________

# Print in-valid ages using filterfalse()
invalid_ages = itertools.filterfalse(is_valid_age, ages)
print(list(invalid_ages))

# ___________________
print(end='\n')
# ___________________

# 14.) takewhile(filter_function, iterable) :
#      Take all items of the iterables until first False (returns
#      by filter_function)
result = itertools.takewhile(is_valid_age, ages)
print(list(result))

# ___________________
print(end='\n')
# ___________________

# 15.) dropwhile(filter_function, iterable) :
#      Drop all items of the iterables until first False(returned
#      by filter_function
result = itertools.dropwhile(is_valid_age, ages)
print(list(result))

# ___________________
print(end='\n')
# ___________________


# 16.) accumulate(iterable, operator.mul(DEFAULT : operator.add))
#      It returns partial sum till its index by default

nums = [1, 2, 4, 5, 0, 8]

partial_sums = itertools.accumulate(nums)
print(f'Partial Sums = {list(partial_sums)}', end='\n\n')

partial_products = itertools.accumulate(nums, operator.mul)
print(f'Partial Products = {list(partial_products)}', end='\n\n')


# 17.) groupby(iterable, function(Give us key for grouping))
# ____________________________________________________________________
# PRE=REQUISITE : The key that on which we want to group must be sorted
#                 Otherwise it won't work.


# To get state of a person
# (Here it is the state of person on which we group person together)
def get_state(person):
    return person['state']


# list of dictionaries of person
people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

# It will give us tuple of key(here state) and group(contains all info)
group_of_same_state_person = itertools.groupby(people, get_state)

for key, group in group_of_same_state_person:

    # copy/replicate the iterator
    # we cannot use group iterator after replicating
    group1, group2 = itertools.tee(group)

    # print the list of dictionaries belong to this key
    # Total person belong to this state
    count = len(list(group1))
    print('Person belongs to {} are {} and are :-'.format(key, count))

    for person in list(group2):
        print(person)

    print(end='\n')

# ___________________
print(end='\n')
# ___________________


# SORTING :
# __________

nums_list = [1, 5, 3, 19, 17, 12, 2, 8, 14]

# 1.) sort() :
# ____________________________________________________________________
# Restriction : It cannot sort containers other than list
# --------------------------------------------------------------------

# To sort the num_list in place(Without using other list) :
nums_list.sort()
print(f'Sorted list using sort() : {nums_list}')

# To sort the num_list in place in reverse order :
nums_list.sort(reverse=True)
print(f'Reverse sorted list using sort() : {nums_list}', end='\n\n')

# 2.) sorted() :
# _______________
sorted_nums_list = sorted(nums_list)
print(f'Sorted list using sorted() : {sorted_nums_list}')

rev_sorted_nums_list = sorted(nums_list, reverse=True)
print(f'Sorted list using sorted() : {rev_sorted_nums_list}')

# sorting dict using sorted() :
person_dict = {'name': 'Santosh', 'gender': 'm', 'age': '20'}
sorted_keys_person_dict = sorted(person_dict)
print(f'Sorted keys of person_dict : {sorted_keys_person_dict}')

# Sorting numbers list A/T absolute value of numbers in the list:
# 'key' parameter can be initialised with abs() which will be applied
# to all the numbers in the list
profits_hour = [-100, 1000, 10, -20, -56, 828]
sorted_by_abs_value = sorted(profits_hour, key=abs)
print(f'Sorted A/T absolute value : {sorted_by_abs_value}')


# sorting class objects by any of the instance variable :
class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # It is used to print the object the way we want to
    # It should be more readable than __str__()
    def __repr__(self):
        return f'({self.name}, {self.age}, ${self.salary})'


emp1 = Employee('Aman Chautala', 27, 59000)
emp2 = Employee('Samar Verma', 12, 88000)
emp3 = Employee('Pawan Das', 23, 67000)

# list of Employee objects  :
emps_list = [emp1, emp2, emp3]


# To sorted class objects we can pass (a custom function) OR (lamda
#  function)

# A.) Using Custom Function  :
# _____________________________
def name(emp):
    return emp.name


sorted_by_name = sorted(emps_list, key=name)
print(f'Sorted by name : {sorted_by_name}')

# B.) Using Lambda Function :
# _____________________________
sorted_by_age = sorted(emps_list, key=lambda emp: emp.age)
print(f'Sorted by age : {sorted_by_age}')

# C.) Using attrgetter() :
# __________________________
from operator import attrgetter

sorted_by_salary = sorted(emps_list, key=attrgetter('salary'))
print(f'Sorted by salary : {sorted_by_salary}', end='\n\n')

# CSV(Comma Separated Values, Default delimiter = ',') Files :
# ____________________________________

# Reading CSVs :
# ______________
with open('csv_file.csv', 'r') as f:
    # It will read the file considering delimiter  = ','
    csv_reader = csv.reader(f)

    # To skip field
    next(csv_reader)

    for line in csv_reader:
        print(line[2])  # to print all e-mail
print(end='\n\n')

# Writing contents into CSVs :
# ______________________________
# Read contents  of csv_file.csv and write contents of it in new_file.csv
# with delimiter as '-'.
# If the values contain '-' in themselves then csv writer will
#  put quotes over values
with open('csv_file.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Pass '' to 'newline' parameter if you do not want to have new line
    # between each row in output file
    with open('new_file.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-')

        # Read from csv_file.csv and write to new_file.csv
        for line in csv_reader:
            csv_writer.writerow(line)

    # Reading the new_file.csv file with delimiter = '-'
    with open('new_file.csv', 'r') as new_file:
        csv_reader1 = csv.reader(new_file, delimiter='-')

        for line in csv_reader1:
            print(line)
print(end='\n\n')

# Reading Using DictReader :
# ______________________________
# It gives us lines of sortedDict
with open('csv_file.csv', 'r') as f:
    csv_dict_reader = csv.DictReader(f)

    for line in csv_dict_reader:
        print(line)

# Writing Using DictWriter :
# ___________________________
# Read the contents of the file of csv_file.csv using DictReader
# and write them(without email) to new_file2.csv with delimiter = '\t'
with open('csv_file.csv', 'r') as f:
    csv_dict_reader = csv.DictReader(f)

    # newline = '' will not write '\n' at the end of each line
    #              instead use ''
    with open('new_file2.csv', 'w', newline='') as new_file2:
        field_names = ['first_name', 'last_name', 'email']

        # create a csv.DictWriter with delimiter = '\t'
        csv_dict_writer = csv.DictWriter(new_file2, fieldnames=field_names, delimiter='\t')

        # To write header in the optput file :
        del field_names[2]
        csv_dict_writer.writeheader()

        for line in csv_dict_reader:
            # It will delete email and then write
            del line['email']
            csv_dict_writer.writerow(line)
print(end='\n\n')

# REAL WORLD EXAMPLE :
# _________________________
# Patreon give us a scv file of all the contributors that we need to
# parse to a html script as an unordered list

with open('patreon.csv', 'r') as f:
    csv_data = csv.DictReader(f)  # It will give us ordered dict

    # To store contributor names
    names = []

    # We do not want first line of bad data
    next(csv_data)

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            continue
        names.append(f"{line['FirstName']} {line['LastName']}")

html_output = f'<p>There are total {len(names)} contributors. Thanks to all of them!</p>'
html_output += f'\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += f'\n</ul>'

print(html_output, end='\n\n')

"""
# REQUESTS MODULE :
# ____________________
r = requests.get('https://xkcd.com/353/')

# It will give us the content of the response in unicode
print(r.text, end='\n\n')

# To get all the properties and functions of requests.get() object
print(dir(r), end='\n\n')

# To get in-depth description of all the methods and properties of
# requests.get() object :
print(help(r), end='\n\n')

# To get the url
print('url: ', r.url, end='\n\n')

# To get the different headers that we may find useful
print('headers: ', r.headers, end='\n\n')


# Downloading an image from a website :
# ______________________________________
image = requests.get('https://imgs.xkcd.com/comics/python.png')

with open('comic.png', 'wb') as f:
    f.write(image.content)  # Write image content in bytes to 'comic.png'

# Checking the status code of a website :
# _______________________________________

# 1xx : informational response – the request was received, continuing process
# 2xx : successful – the request was successfully received, understood, and accepted
# 3xx : redirection – further action needs to be taken in order to complete the request
# 4xx : client error – the request contains bad syntax or cannot be fulfilled
# 5xx : server error – the server failed to fulfil an apparently valid request


# print status code
print(r.status_code)

# Check if the status code < 400 (OK response)
print(r.ok, end='\n\n')


# TESTING DIFFERENT http methods (Using httpbin.org):
# ___________________________________________________

# httpbin gives us a json string to check whether the test is successful
# or not

# passing arguments to website route
payload = {'page': 2, 'count': 25}
req = requests.get('https://httpbin.org/get', params=payload)

# httpbin.org will gives us json file where we can check for specific
# things
print(req.text)

# posting data to the website route :
payload = {'username': 'santosh', 'password': 'testing'}
req = requests.post('https://httpbin.org/post', data=payload)
print(req.text)


# Since httpbin.org site giving us a json file we can use json()
# method to convert it to python object and can use for our purpose
req_dict = req.json()
print(req_dict['form'])  # printing the posted data


# Testing basic authorisation using httpbin.org
# Look for the syntax in the site for basic-auth :
#      SYNTAX:            /basic-auth/{user}/{passwd}
auth_req = requests.get('https://httpbin.org/basic-auth/santosh/testing', auth=('santosh', 'testing'))


# If the correct credentials are not given  it will provide no response
# OR status_code of 4xx and above
if auth_req.status_code < 400:
    print(auth_req.text)
else:
    print('Wrong credentials used!')


# If a site is taking a lot of time than expected then we can pass
#  'timeout' parameter to requests.get()
#   SYNTAX : /delay/{delay}

# We are delaying upto 2 seconds and have a timeout at 3 seconds
del_req = requests.get('https://httpbin.org/delay/2', timeout=3)
if del_req.ok:
    print(del_req.text)
else:
    print('Taking longer time than expected!')

print(end='\n\n')

# WEB SCRAPPING USING BEAUTIFUL-SOUP AND REQUESTS:
# ___________________________________________________
# WEB SCRAPPING  :
# _________________
# Web scraping, web harvesting, or web data extraction is data scraping
# used for extracting data from websites.

# We can use parsers like lxml or htmllib5 (based on html 5)
# They can yield different result if we try the parse unperfectly
# formatted HTML
# It is recommended to use : lxml parer but htmllib5 is also fine


# web scrapping from a html file :
# ___________________________________
with open('html_file.html') as html_file:

    # It will give us formatted html code of the file
    # 'lxml' is used as parser to parse the html if html file
    # contains an imperfectly formatted html
    source = BeautifulSoup(html_file, 'lxml')

    # prettify() is used to get properly indented file
    print(f'Prettified html :\n{source.prettify()}', end='\n\n')

    # To print prettified first div
    print(f'First div: \n{source.div.prettify()}', end='\n\n')

    # To print first div text
    print(f'First div text : {source.div.text}', end='\n\n')

    # To print tag div of class = 'footer :
    footer = source.find('div', class_='footer')
    print(f'Prettified footer : \n{footer}')

    # Scrap the Useful content of the file :
    # ______________________________________
    for article in source.find_all('div', class_='article'):
        print(end='\n\n')
        print(article.h2.text)
        print(article.p.text)


# Scrapping all posted information from a real website : 'https://coreyms.com' :
# __________________________________________________________________________
source_code = requests.get('https://coreyms.com').text

corey_ms = open('corey_ms.csv', 'w')
csv_writer = csv.writer(corey_ms)
csv_writer.writerow(['headline', 'summary', 'video_link'])

# parsed HTML :
soup = BeautifulSoup(source_code, 'lxml')

for article in soup.find_all('article', class_='post'):
    headline = article.header.h2.a.text
    print(headline)

    summary = article.div.p.text
    print(summary)
    # Src is embedded in the website so we need to get the video id
    # and then form a route to go to youtube and allow us to
    # watch the video we wanted
    link = article.find('iframe')
    if link is not None:
        video_src = link['src']
        video_id = video_src.split('/')[4]
        video_id = video_id.split('?')[0]

        video_link = f'http://youtube.com/watch?v={video_id}'
    else:
        video_link = None

    print(video_link, end='\n\n')

    csv_writer.writerow([headline, summary, video_link])

# close the file
corey_ms.close()
"""

# ZIP_FILE :
# ___________

# general method
# _________________
# create a zip_file names zip_file.zip
"""
cwd = os.getcwd()

my_zip = zipfile.ZipFile(f'{cwd}' + r'\test_zip_file.zip', 'w')

# write the files you want to zip together
my_zip.write(f'{cwd}' + r'\Screenshot.png')
my_zip.write(f'{cwd}' + r'\test1.txt')

my_zip.close()
"""

"""
# Using Context manager
with zipfile.ZipFile('new_zip_file.zip', 'w') as my_zip:
    my_zip.write('Screenshot.png')
    my_zip.write('test1.txt')
"""

# With compression parameter to get compressed zip file :
# ________________________________________________________
"""
with zipfile.ZipFile('new_zip_file.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write('comic.png')
    my_zip.write('new_file.csv')
"""

# To extract files from zip file :
# _______________________________
"""
with zipfile.ZipFile('new_zip_file.zip', 'r') as my_zip:
    print(my_zip.namelist())  # To get the all file names

    # To extract all files in the zip file in a folder named 'extracted_file'
    my_zip.extractall('extracted_file')

    # To extract comic.png file from the new_zip_file.zip
    my_zip.extract('comic.png')
"""

# shutil module to make zip file from a directory :
# __________________________________________________
"""
shutil.make_archive('another_zip_file', 'zip', 'test_folder')
"""

# To unzip the files using shutil :
# _________________________________
# unpack another_zip_file.zip to a folder named 'another_extracted_file'
"""
shutil.unpack_archive('another_zip_file.zip', 'another_extracted_file')
"""

# We can use other archive format in 'format' parameter of make_archive()
#   OR  unpack_archive()

# EXAMPLE :
# ___________
# packing
"""
shutil.make_archive('new_gztar_file', 'gztar', 'test_folder')
"""

# unpacking
"""
shutil.unpack_archive('new_gztar_file.tar.gz', 'extracted_gztar_file')
"""

# DOWNLOADING ZIP FILE FROM INTERNET :
# _________________________________________

r = requests.get('https://github.com/donnemartin/system-design-primer/archive/master.zip')

"""
with open('systemDesign.zip', 'wb') as my_zip:
    # write the bytes of r in my_zip
    my_zip.write(r.content)
"""

"""
with zipfile.ZipFile('systemDesign.zip', 'r') as f:
    f.extractall('System Design')
"""

# INTERNAL COMMANDS V/S EXTERNAL COMMANDS :
# __________________________________________


# INTERNAL COMMANDS
# ___________________

# What they are ?
# __________________
# -> An internal command is an MS-DOS command that is stored in the
#    system memory and loaded from the command.com or cmd.exe.

# Where are the internal command files stored ?
# ______________________________________________
# -> Internal commands are part of the shell { command.com or cmd.exe
#    (depending on version of MS-DOS or Windows) } and are not
#    separate files on the hard drive.

# How do you run an internal command?
# _______________________________________
# As long as you can open a command line, you can run any of the
# internal commands included with your version of MS-DOS
# or Microsoft Windows.

# EXTERNAL COMMANDS :
# ___________________
# -> An external command is an MS-DOS command that is not included
#    in command.com.
# -> External commands are commonly external either because they
#    have large requirements or are not commonly used commands.

# Where are the external command files stored?
# _____________________________________________
# -> Many of the external commands are located in the Windows\system32
#    or Winnt\system32 directories.
# -> If you need to locate the external file to delete it, rename it
#    or replace it, you can also find the file through MS-DOS.

# How do you run an external command?
# ____________________________________
# -> As long as the file exists and you have the proper paths,
#    an external command runs like an internal command by typing
#    the command name at the prompt.
# -> However, if the paths are not set properly or they are missing
#    because the command line would not know where to look for
#    the external command, you would get an error.

# RUNNING EXTERNAL COMMANDS USING SUBPROCESS MODULE :
# _____________________________________________________

# It returns args and returncode and output the result of the command(s)

p1 = subprocess.run('dir', shell=True)
# print(p1.args)   # Returns args list. Here p1.args = ['dir']
# print(p1.returncode)  # 0 : No Error
print(end='\n\n')


# If we do not want to print the command passed to run() :
p1 = subprocess.run('dir', shell=True, capture_output=True)

# p1.stdout returns a byte which can be converted to string by decode()
#  to decode the bytes to string
print(p1.stdout.decode())
print('\n\n')

# If we do not want decode the stdout we can use text = True in run()
p1 = subprocess.run('dir', shell=True, capture_output=True, text=True)
print(p1.stdout)
print('\n\n')

# capture_output set stdout = subprocess.PIPE and it also set stderr
# we can directly set stdout = subprocess.PIPE to get the same result
p1 = subprocess.run('dir', shell=True, stdout=subprocess.PIPE, text=True)
print(p1.stdout)
print('\n\n')


# REDIRECTING EXTERNAL COMMAND OUTPUT TO OTHER PLACES :
# _________________________________________________________

# REDIRECTING THE stdout TO OTHER FILE:
# __________________________________________
with open('stdout.txt', 'w') as f:
    p1 = subprocess.run('dir', shell=True, stdout=f, text=True)


# EROOR IN RUNNING EXTERNAL COMMAND :
# ____________________________________
# -> Python does not throw an error when an external command fail but
#    it returns a non-zero returncode

# -> Let's try to list out files of directory ['dne'] which does not
#    exist in root directory
p1 = subprocess.run(['dir', 'dne'], shell=True, capture_output=True, text=True)


# print returncode (Must be non-zero, means an error)
print(p1.returncode)

# To print the stderr
print(p1.stderr, end='\n\n')

# We can pass check = True in run() to tell Python to throw an
# exception when exception occurred
"""
p1 = subprocess.run(['dir', 'dne'], shell=True, capture_output=True, text=True, check=True)
print('\n\n')
"""

# Ignoring error by redirecting them to DEVNULL :
# ________________________________________________
# shell = True.Then we can pass command as a string
# shell = False.Then we can pass multi-word command using a list of them
p1 = subprocess.run('dir dne', shell=True, stderr=subprocess.DEVNULL)

# We have ignored the error therefore it should print None
print(p1.stderr)  # None

# We can put input parameter to run to pass in a custom input


# VIRTUAL ENVIRONMENT :
# _______________________

# What is it? What are its purpose?
# ____________________________________
# -> Virtual environment can be used to separate packages for different
#    projects

# Example :
# _________
# -> Suppose some of my project use older version of django and a
#    newer project use newer version of django.
# -> If we create both projects in same global environment, we have
#    to update django to newer version so that newer projects
#    get to use them. But older projects may break because they are
#    using older version of django

# SOLUTION :
# ____________
#  -> We can create two virtual enviroments each for older and newer
#     projects to separate their dependencies


# COMMAND LINE COMMANDS :
# ____________________________________________________________________

# TO CREATE VIRTUAL ENVIRONMENT :
# ________________________________
# -> Move to the directory where you want to create virtual env
# -> Then type:
#    SYNTAX : python -m venv {name_of_the_virtual_environment}

# TO ACTIVATE CREATED VIRTUAL ENVIRONMENT :
# _________________________________________
# SYNTAX :  {name_of_the_virtual_environment}\Scripts\activate.bat


# -> Created virtual environment use same version of python as you have
#    created virtual environment on
# -> We can now install the packages we will be requiring for this
#    environment

# INSTALL : pip install {package_name}
# UNINSTALL : pip uninstall {package_name}


# TO EXPORT THE LIST OF PACKAGES AND DEPENDENCIES OF A ENVIRONMENT
# TO OTHER PEOPLE SO THAT THEY CAN CREATE THE ENVIRONMENT AND INSTALL
# ALL THE REQUIREMENTS
# ____________________________________________________________________

# -> For this we can use 'pip freeze' command to get the installed
#    packages in requirement format AND then copy the output to
#    requirements.txt file

# TO DEACTIVATE VIRTUAL ENVIRONMENT :
# _____________________________________
# deactivate

# TO DELETE THE VIRTUAL ENVIRONMENT :
# ____________________________________
# SYNTAX : rmdir {virtual_environment_name} /s (Deletes all contents)


# ->  Suppose we are making a new environment that is going to use
#     all the packages listed in a requirements.txt file
#     ( Obtained from 'pip freeze' command' )
# ->  Then type: (venv is the standard name given to virtual environment)
#     1.) Creation : python -m venv {folder_name}\venv
#     2.) Activation : {folder_name}\venv\Scripts\activate.bat
#     3.) Installation : pip install -r requirements.txt
#     4.) Un-installation : pip uninstall -r requirements.txt


# TO CREATE VIRTUAL ENVIRONMENT CONTAINING SYSTEM PYTHON PACKAGES
# _________________________________________________________________
# SYNTAX : python -m venv venv --system-site-packages

# TO GET THE PACKAGES INSTALLED IN THIS ENVIRONMENT :
# _______________________________________________________
# SYNTAX : pip list --local


# PIPENV :
# _____________________________________________________________________

# 'pip' is a package manager used to manage packages in python
# 'venv' is a module to use virtual environment in python
# 'pipenv' combines the  functionalities of both 'pip' and 'venv'

# Previously, we would create a virtual environment where our project
# is located and activate it manually and also install the packages
# we will be needed for the project.

# But now with 'pipenv' :
# ___________________________
# Move to the folder where you want your new project to be
# And type :
#           pipenv install {package_name}

# WHAT IT DID?
# ______________
# 1.) It creates the virtual environment of the project if there
#     aren't any.
# 2.) It gives the location of the 'pipfile'
# 3.) It also gives the version of python it is using.
# 4.) It also gives the location of virtual environment {Which we can
#     to activate the virtualenv manually. But pipvenv has simpler
#     command that do same work for us.)
# 5.) It creates the 'pipfile' (It is similar to requirements.txt file
#      It contains packages and their dependencies along with their
#      versions )
# 6.) It will install the packages and dependencies we have mentioned.
# 7.) It creates 'pipfile.lock' ( Similar to 'pipfile' but cannot be
#                                   modified )

# PIPENV COMMANDS :
# ____________________________________________________________________

# TO ACTIVATE PROJECT'S VIRTUALENV :
# _____________________________________________________________________
# SYNTAX: pipenv shell

# TO RUN A COMMAND INSIDE VIRTUALENV :
# _____________________________________________________________________
# SYNTAX: pipenv run

# pipfile AND pipfile.lock :
# ______________________________________________________________________

# pipfile :
# ______________________________________________________________________
# -> 'pipfile' contains source of the packages, packages list and their
#     version
# -> If the version of package is '*' means we have not specified the
#    the version while installing it .
#    -> This also means if we try to install this  package again
#        then, it will check for newer version and install it.
#    -> This may break our code. Here 'pipfile.lock' comes in rescue
#       in that situation
# -> If we specify version while downloading packages then it will not
#    change even if newer version of the package is available
# -> It also contain version of python info.
# -> It is also editable. After editing we can rerun the install command
#    to install all the packages we have added.

# pipfile.lock
# _____________________________________________________________________
# -> It is not meant to be editable.
# -> It contains exact packages and dependencies along with their
#    versions of the project which is working as expected.
# -> After successful execution of the project after adding new
#    packages and codes and we can update 'pipfile.lock'


# TO DEACTIVATE VIRTUALENV :
# ___________________________________________________________________
# exit

# TO RUN COMMAND WITHIN THAT VIRTUALENV AFTER EXITING FROM THE VIRTUALENV:
# _________________________________________________________________________
# SYNTAX: pipenv run {command}
# Eg : pipenv run python

# TO RUN PYTHON SCRIPT INSIDE THAT VIRTUALENV:
# _____________________________________________________________________
# SYNTAX: pipenv run python {name.py}

# TO INSTALL LIST OF PACKAGES FROM 'requirements.txt' :
# ____________________________________________________________________
# SYNTAX: pipenv install -r requirements.txt

# TO VIEW THE PACKAGES AND DEPENDENCIES THAT CAN BE COPIED TO
#  'requirements.txt' file
# ____________________________________________________________________
#  SYNTAX : pipenv lock -r

# TO INSTALL PACKAGE IN A DEV ENVIRONMENT THAT WE DO NOT NEED IN
# PRODUCTION :
# ____________________________________________________________________
# Eg : pytest package is only need during development but there is no
#      need of it in production

# SYNTAX : pipenv  install {package_name} --dev


# TO UNINSTALL PACKAGE :
# _______________________________________________________________________
# SYNTAX: pipenv uninstall {package_name}


# TO CHANGE THE VERSION OF PACKAGE OR PYTHON :
# _____________________________________________________________________
# 1.) Manually edit the 'pipfile'
# 2.) SYNTAX OF COMMAND : pipenv --python {version}

# TO REMOVE AN VIRTUALENV :
# _____________________________________________________________________
# SYNTAX: pipenv --rm
# NOTE : It won't delete  (a) pipfile, (b) pipfile.locks


# TO CREATE VIRTUALENV FORM 'pipfile' :
# SYNTAX: pipenv install  (After moving to the folder where there is
#                           pipfile)

# TO LOOK PATH OF THE VIRTUALENV :
# ______________________________________________________________________
# SYNTAX: pienv --venv


# OTHER TOP FEATURES (pipenv):
# _____________________________________________________________________

# 1.) TO CHECK NON-SECURITY VULNERABILITIES OF THE INSTALLED PACKAGES
# ______________________________________________________________________
#   SYNTAX: pipenv check
#   -> We can use the recommendation by updating the version of
#       packages and can install them using : "pipenv install" command

# 2.) TO DISPLAY PACKAGES AND THEIR DEPENDENCIES SEPARATELY :
# _______________________________________________________________________
#    SYNTAX: pipenv graph

# TO UPDATE 'pipfile.lock' to all the dependencies of the project:
# _____________________________________________________________________
# SYNTAX: pipenv lock

# TO INSTALL PACKAGES AND DEPENDENCIES IN 'pipfile.lock' (For Production):
# ________________________________________________________________________
# SYNTAX: pipenv install  --ignore_pipfile
# NOTE : It will create an virtual environment that uses the packages
#        and dependencies in the 'pipfile.lock'


# ENVIRONMENT VARIABELE :
# ____________________________________________________________________
# -> They are the variables that exist outside of our code as part of the
#   server environment .
# -> They can help us both in :-
#          a.) streamlining
#          b.) making more secure the process of running scripts
#              and applications.

# USES :
# 1.) Authentication keys (like API token)
# 2.) Execution Mode (Eg : Development, Staging, Production)

# Create environment variables in .env file and that can be accessed
# using os module but file should be commited to github :
# ____________________________________________________________________

# Accessing environment variable :
# ____________________________________________________________________
# import os
# os.environ[{name_of_env_variable}]


# THREADING :
# _____________________________________________________________________
"""
 -> A thread is an execution context, which is all the information 
    a CPU needs to execute a stream of instructions.

 -> Suppose you're reading a book, and you want to take a break right
    now, but you want to be able to come back and resume reading from
    the exact point where you stopped. One way to achieve that is by 
    jotting down the page number, line number, and word number.
    So your execution context for reading a book is these 3 numbers.

 -> If you have a roommate, and she's using the same technique, 
    she can take the book while you're not using it, and resume
    reading from where she stopped. Then you can take it back,
    and resume it from where you were.

 -> Threads work in the same way. A CPU is giving you the illusion
    that it's doing multiple computations at the same time. 
    It does that by spending a bit of time on each computation.
    It can do that because it has an execution context for each
    computation. Just like you can share a book with your friend,
    many tasks can share a CPU.

 -> On a more technical level, an execution context
    (therefore a thread) consists of the values of the CPU's
    registers

"""

# CPU BOUND V/S I/O BOUND :
# ___________________________
"""   
 -> A program is CPU bound if it would go faster if the CPU were 
    faster, i.e. it spends the majority of its time simply using
    the CPU (doing calculations). A program that computes new 
    digits of π will typically be CPU-bound, it's just crunching 
    numbers.
    EXAMPLE : Image processing, video processing, etc.

 -> A program is I/O bound if it would go faster if the I/O
    subsystem was faster. Which exact I/O system is meant can vary;
    It is typically associated with disk, but networking 
    (or communication in general) is common too. A program that
    looks through a huge file for some data might become I/O bound,
    since the bottleneck is then the reading of the data from disk.
    EXAMPLE : Downloading and uploading data from internet,
              reading and writing files to a disk, etc. 
"""

# SYNCHRONOUSLY V/S ASYNCHRONOUSLY
""" 
  Synchronously means running one at a time
  Asynchronously means running concurrently
"""

"""
# time.perf_counter() gives us the relative time
# It does not have any relation with the real world time
start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)')
    time.sleep(seconds)
    print(f'Finished sleeping {seconds} second(s)')


# -> Sleeping for these list of seconds synchronously cost us sum
#    of all values
# -> Sleeping for these list of seconds asynchronously cost us the
#    max(list(secs))  (Using Threading)
secs = [5, 1, 4, 2, 6, 8]
threads = []

for sec in secs:
    # Creating thread with target function : 'do_something'
    # args : It is a list of arguments that the function need to be passed
    t = threading.Thread(target=do_something, args=[sec])

    # To start the thread
    t.start()
    threads.append(t)

# JOIN() :
# _____________________________________________________________________
# -> You want to concurrently download a bunch of pages to concatenate
#    them into a single large page, you may start concurrent downloads
#    using threads, but need to wait until the last page/thread is
#    finished before you start assembling a single page out of many.
# -> That's when you use join().
for thread in threads:
    thread.join()

end = time.perf_counter()
print(f'Finished in {end-start} second(s)', end='\n\n')


# BETTER METHOD FOR USING THREADING (Using concurrent.futures module) :
# _____________________________________________________________________

start = time.perf_counter()


def do_something(seconds):
    print('Sleeping {} seconds'.format(seconds))
    time.sleep(seconds)
    return f'Done sleeping {seconds} seconds'


with concurrent.futures.ThreadPoolExecutor() as executor:
    # submit() schedules the method and returns a futures object
    # 'results' contains now list of futures object
    results = [executor.submit(do_something, sec) for sec in secs]

    # If we don't care about the order:
    for f in concurrent.futures.as_completed(results):
        # result() of futures object gives us the return value of the
        # function
        print(f.result())
    print(end='\n\n')

    # Using executor.map() :
    # -> It returns a list of results (As we have seen above)
    # -> executor.map() is going to return result in the order they are
    #    started

    # NOTES -> If our function raises an exception then it won,t raise
    #         exception while running the thread
    #       -> But exception will be raised when the value is retrieved
    #          from the 'results' iterator
    results = executor.map(do_something, secs)
    for result in results:
        print(result)

end = time.perf_counter()
print(f'Finished in {end-start} second(s)', end='\n\n')
"""

# REAL WORLD EXAMPLE :
# _____________________________________________________________________
# DOWNLOADING A SET OF IMAGES FROM a set of image urls
# from website : 'unsplash.com'

"""
start = time.perf_counter()

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
    ]


def download_image(img_url):
    content = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name += '.jpg'

    with open(img_name, 'wb') as img_file:
        img_file.write(content)
    print(f'Image Downloaded {img_name}')


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)

end = time.perf_counter()
print(f'Finished in {end-start} second(s)', end='\n\n')

"""


# MULTI-PROCESSING :
# ____________________________________________________________________
# For Parallel computation of several tasks
"""
def do_something(seconds):
    print('Sleeping {} seconds'.format(seconds))
    time.sleep(seconds)
    print('Done sleeping {} seconds'.format(seconds))


secs = [1, 4, 3, 2, 5]

# Method - 1:
# ____________________________________________________________________
start = time.perf_counter()
processes = []
for sec in secs:
    p = multiprocessing.Process(target=do_something, args=[sec])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

end = time.perf_counter()
print(f'Finished in {end-start} second(s)', end='\n\n')
"""

"""
# METHOD - 2: (Using concurrent.futures.ProcessPoolExecutor())
# _____________________________________________________________________

# Using context manager will automatically join all the  processes
# we create
start = time.perf_counter()
with concurrent.futures.ProcessPoolExecutor() as executor:
    # Using submit() to get futures object
    # Here results is the list of futures objects
    results = [executor.submit(do_something, sec) for sec in secs]
    for res in results:
        print(res.result())

    # Using builtin map():
    # Here results is the list of results returned by function
    #  'do_something'
    results = executor.map(do_something, secs)
    for res in results:
        print(res)


end = time.perf_counter()
print(f'Finished in {end-start} second(s)', end='\n\n')
"""


# REAL WORLD EXAMPLE OF USING MULTI-PROCESSING :
# ____________________________________________________________________
# Using 'multiprocessing' module to process multiple images
# parallel

"""
start = time.perf_counter()

img_names = [

 'photo-1493976040374-85c8e12f0c0e.jpg'
 'photo-1504198453319-5ce911bafcde.jpg'
 'photo-1507143550189-fed454f93097.jpg'
 'photo-1513938709626-033611b8cc03.jpg'
 'photo-1516117172878-fd2c41f4a759.jpg'
 'photo-1516972810927-80185027ca84.jpg'
 'photo-1522364723953-452d3431c267.jpg'
 'photo-1524429656589-6633a470097c.jpg'
 'photo-1530122037265-a5f1f91d3b99.jpg'
 'photo-1530224264768-7ff8c1789d79.jpg'
 'photo-1532009324734-20a7a5813719.jpg'
 'photo-1541698444083-023c97d3f4b6.jpg'
 'photo-1549692520-acc6669e2f0c.jpg'
 'photo-1550439062-609e1531270e.jpg'
 'photo-1564135624576-c5c88640f235.jpg'
]

thumbnail_size = (1200, 1200)


def process_image(img_name):
    # Opening the image
    img = Image.open(img_name)

    # Filtering the image with GaussianBlur of value = 15
    # To reduce detail
    img = img.filter(ImageFilter.GaussianBlur(15))

    # setting the thumbnail size
    img.thumbnail(thumbnail_size)

    # saving to a particular location
    img.save(f'Processed Images/{img_name}')
    print(f'{img_name} was processed...')


with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, img_names)


end = time.perf_counter()
print(f'Finished in {end-start} second(s)')
"""

# Anaconda :
# ____________________________________________________________________
# It is a python distribution which contains all the packages we
# need for data-science, package manager conda, etc

# Creating virtual environment using conda
# _____________________________________________________________________
# conda create --name {name} {packages(at least 1)}

# Activating venv :
# _____________________________________________________________________
# WINDOWS : activate {venv_name}

# To get the python path of the venv : which python

# Deactivate venv :
# _____________________________________________________________________
# WINDOWS : deactivate {venv_name}

# To install different python version for our project using conda :
# _____________________________________________________________________
# conda create --name {venv_name} python={version} {packages_list_separated_by_space}


# To view the list of venvs :
# _____________________________________________________________________
# SYNTAX : conda env list

# To remove an env :
# _____________________________________________________________________
# SYNTAX :  conda remove {env_name} --all{All packages we want to delete}
