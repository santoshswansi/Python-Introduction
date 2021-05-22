import random
import platform
import datetime
import math
import json
import re
import numpy
import os
import requests

"""
  To check the version of your python : python --version
  To write python instructions in command line : py
"""

# How to print
# ____________________
# Syntax : print(object(s), sep = separator, end = ending, file, flush);
#        object(s) : As many objects as you want, will be converted to string
#        separator : (Optional) Specify how to separate the objects if there are
#                    more than one. DEFAULT : ' '
#        end : (Optional) How to print end? DEFAULT : '\n'
#        file : (Optional) An object with a write method.  DEFAULT : sys.stdout
#        flush : To mention output is flushed(TRUE) or buffered(FALSE)
#                DEFAULT : FALSE

print("hello world")
print("Hello ", "world")
print("Hello", "python", sep=",", end="!" + "\n")

# PYTHON INDENTATION :
# ________________________
#  It refers to the space at the beginning of the line
#  It is used to identify block of codes

# PYTHON VARIABLES :
# ____________________
#  There is no concept of variable declaration
#  Variable is created as soon as you assigned a value to it
#  A variable can change to any other type
#  " ", ' ' quotes can be used to assign string value to variable

#  NAMING VARIABLES :
# _______________________
#  First character must be a alphabet OR underscore
#  Name should only contain alpha-numeric letters and underscores (A-Z, a-z, 0-9,_)


firstName = "Santosh"
secondName = "Swansi"
rollNo = 732
marks = 549.8

print("First Name : " + firstName)
print("Last Name : " + firstName)

# GLOBAL VARIABLES :
# _____________________
# Variables declared outside a function
# "global" keyword can be used to make a change in global variable inside a function

x = "Global Variable"


# Defining Functions :
# ____________________
def func():
    global x
    x = "..."
    print("Value of local variable : " + x)


def func2():
    y = "Kelly!"
    print("Hello " + y + x)


# Calling Functions :
# __________________
func()
func2()

# BUILT-IN DATA TYPES :
# ______________________
#  Text Type :  str
#  Numeric Type : int, float, complex
#  Sequence Type : list, tuple, range
#  Mapping Type : dict
#  Set Type : set, frozenset
#  Boolean Type : bool
#  Binary Types: bytes, bytearray, memoryview

# Getting the type of variable : Use type() function
# ____________________________________________________
computerBrand = "Acer"
print(type(computerBrand))

# SETTING THE DATA TYPES :
# ___________________________
employeeName = "Basu"  # str
employeeCode = 234  # int
employeeSalary = 54000.97  # float
complexTypeData = 1j  # complex  (j = root(-1))
employeeList = ["Luke Martin", "Kane Williams", "Trent Bolt"]  # list
employeeTuple = ("Luke Martin", "Kane Williams", "Trent Bolt")  # tuple
salaryRange = range(1200000)  # range

salaryDict = {"Name": "Luke Martin", "age": "36"}  # dict
salarySet = {"50000", "52000", "73000"}  # set
salaryFrozenSet = frozenset({"50000", "52000", "73000"})  # frozenset

booleanValue = True  # bool
bytesValue = b"Hello"  # bytes
byteArrayValue = bytearray(5)  # bytearray
memoryViewValue = memoryview(bytes(5))  # memoryview

# SETTING THE SPECIFIC DATA TYPES : You can use following Constructor function
# _____________________________________________________________________________
shopName = str("General  Store")
shopNumber = int(534)
shopIncome = float(231578.9)
complexType = complex(1j)
shopsList = list(("Apple store", "Acer Store", "Samsung Store"))
shopsSet = set(("Apple store", "Acer Store", "Samsung Store"))
shopTuple = tuple(("Apple store", "Acer Store", "Samsung Store"))
shopFrozenSet = frozenset(("Apple store", "Acer Store", "Samsung Store"))
shopDictionary = dict(name="Apple Store", year="2009")
shopIncomeRange = range(3400000)
shopExist = bool(True)
shopNumberInBytes = bytes(12200)
byteArray = bytearray(20)
memoryView = memoryview(bytes(25))

# PYTHON NUMBERS :
# _____________________
# int, float, complex

intValue = 20
floatValue = -23.89
complexValue = 12 + 1j  # j = complex part
largeValue = 123.78e10  # e : To represent power of 10

# TYPE CONVERSION
# __________________
# Use int(), float(), complex()
# We cannot convert complex number to other type
toComplexType = complex(intValue)
toFloatType = float(intValue)

# RANDOM NUMBERS
# ________________
# Python does not have built-in function random(), but it has module random

print(random.randrange(1, 20))

# PYTHON CASTING
# _________________
# We can use float(), int(), complex() constructor of respective classes

# Integers
# ______________
a = int(1)  # a will be 1
b = int(2.8)  # b will be 2
c = int("3")  # c will be 3

# float
# _________
a = float(1)
b = float(2.9)
c = float("4")

# string
# __________
a = str(2)
b = str(3.0)
c = str("s1")

# PYTHON STRINGS
# ________________

# Multi-line string
# ____________________
string = """This is a
multi-line
string"""
print(string)

# STRINGS AS ARRAY :
# _____________________
# python does not have a character data type, a single character is simply
# string of length = 1
print(string[2])

# SLICING
# ___________
# To return range of characters

# 3-indexed character not included
print(string[1:3])

# Negative Indexing to start slice from end of the string
# 5th indexed character from last not included
print(string[-5:-2])

# length of the string
print(len(string))

# STRING METHODS
# ________________
print(string.strip(), end="\n\n")  # to strip off whitespaces
print(string.upper(), end="\n\n")  # upper case
print(string.lower(), end="\n\n")  # lower case
print(string.replace("i", "a"), end="\n\n")  # replace 'i' with 'a'
print(string.split("s"), end="\n\n")  # to split to string into  sub-strings with separator="s"

# STRING CHECK
# ________________
sPresent = "s" in string  # if 's' is present in string returns True else False
print(sPresent)

sNotPresent = "s" not in string  # return True if 's' is not present in string
print(sNotPresent)

# STRING FORMAT :
# ___________________
# It can be used to combine strings and numbers
# format() can take uncountable number of arguments
age = 20
college = "Harvard College"
txt = "My name is Mac William and i am {} and i am currently studying at {}"
print(txt.format(age, college))

# We can put index number in place-holders also
txt = "My name is Mac William and i am {1} and i am currently studying at {0}"
print(txt.format(college, age))

# ESCAPE CHARACTERS
# ______________________

# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value

# carriage return (\r)
# It takes the cursor to the beginning of the line
# It is th same effect as in a physical typewriter when you move your carriage to
# the beginning and overwrite whatever is there
print("Hello world\rNamaste!")

# octal value :
# backslash followed by three integers will result in a octal value
octalText = "\100\145\154\154\157"
print(octalText)

# Hexa-Decimal Value : backslash followed by an 'x' and a hex number represents
# a hex value

hexadecimalText = "\x48\x65\x6c\x6c\x6f"
print(hexadecimalText, end="\n\n")

# STRING METHODS : All methods returns new string, it does not change the original
#                  string

#  capitalize()  	Converts the first character to upper case
#  casefold()	    Converts string into lower case
#  center()     	Returns a centered string
#  count()	        Returns the number of times a specified value occurs in a string
#  encode()	        Returns an encoded version of the string
#  endswith()	    Returns true if the string ends with the specified value
#  expandtabs()	    Sets the tab size of the string
#  find()	        Searches the string for a specified value and returns the position of where it was found
#  format()	        Formats specified values in a string
#  format_map()	    Formats specified values in a string
#  index()	        Searches the string for a specified value and returns the position of where it was found
#  isalnum()	    Returns True if all characters in the string are alphanumeric
#  isalpha()	    Returns True if all characters in the string are in the alphabet
#  isdecimal()	    Returns True if all characters in the string are decimals
#  isdigit()	    Returns True if all characters in the string are digits
#  isidentifier()	Returns True if the string is an identifier
#  islower()	    Returns True if all characters in the string are lower case
#  isnumeric()	    Returns True if all characters in the string are numeric
#  isprintable()	Returns True if all characters in the string are printable
#  isspace()	    Returns True if all characters in the string are whitespaces
#  istitle()	    Returns True if the string follows the rules of a title
#  isupper()	    Returns True if all characters in the string are upper case
#  join()	        Joins the elements of an iterable to the end of the string
#  ljust()      	Returns a left justified version of the string
#  lower()	        Converts a string into lower case
#  lstrip()     	Returns a left trim version of the string
#  maketrans()  	Returns a translation table to be used in translations
#  partition()	    Returns a tuple where the string is parted into three parts
#  replace()	    Returns a string where a specified value is replaced with a specified value
#  rfind()	        Searches the string for a specified value and returns the last position of where it was found
#  rindex()	        Searches the string for a specified value and returns the last position of where it was found
#  rjust()	        Returns a right justified version of the string
#  rpartition()	    Returns a tuple where the string is parted into three parts
#  rsplit()	        Splits the string at the specified separator, and returns a list
#  rstrip()	        Returns a right trim version of the string
#  split()	        Splits the string at the specified separator, and returns a list
#  splitlines()	    Splits the string at line breaks and returns a list
#  startswith() 	Returns true if the string starts with the specified value
#  strip()	        Returns a trimmed version of the string
#  swapcase()	    Swaps cases, lower case becomes upper case and vice versa
#  title()	        Converts the first character of each word to upper case
#  translate()  	Returns a translated string
#  upper()	        Converts a string into upper case
#  zfill()	        Fills the string with a specified number of 0 values at the beginning


# PYTHON BOOLEANS
# _________________

# Most values are False  except : "", {}, (), [], 0, False, None
# Any numeric value, str, dict, set, tuple evaluates to True if its not 0 or not empty
print(bool(0))
print(bool({}))
print(bool(()))
print(bool([]))
print(False)
print(None)
print(bool(""))


# One more value OR object in this case, evaluates to False :
# If we have created an object of a function __len__() that returns 0 OR False


class MyClass:
    def __len__(self):
        return 0


myObj = MyClass()
print(bool(myObj), end="\n\n")  # It evaluates to False

# Built-in functions that returns boolean value : isinstance(variable, int)
# It tells whether the provided variable is of given type or not
print(isinstance(myObj, object), end="\n\n")

# PYTHON OPERATORS :-
# 1.) Arithmetic Operators  ( +, -, /, *, %, //(Floor Value), **(Exponentiation))
# 2.) Assignment Operators  ( =, +=, *=, /=, %=, **=, //=, |=, &=, ^=, <<=, >>=)
# 3.) Comparison Operators  (==, >=, <=, !=, <, >)
# 4.) Logical Operators     (and, or , not)
# 5.) Bitwise Operators     (&, |, ^, ~(Not), <<, >>)
# 6.) Identity Operators   (is --> Returns True if both variables are of the same object)
#                          (is not --> Returns True if both variables are of the
#                           different object)
# 7.) Membership Operators  (in --> Returns True if specified value is present
#                            in the object)
#                           (not in --> Returns True if specified value is not
#                            present in the object)

# Examples of Arithmetic Operators : // And **
floorValue = 12 // 7
exponentValue = 2 ** 5
print(f"Floor(12/7) = {floorValue}")  # Use of f-string
print(f"Exponent(2,5) = {exponentValue}", end="\n\n")

# Examples of Identity Operators : is AND is not
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

# returns True because z is the same object as x
print(x is z)

print(x is not y)  # returns True because x and y are not the same object

# to demonstrate the difference between "is" and "==": this comparison returns True because x is equal to y
print(x == y)

# To demonstrate the difference between "is not" AND "!="
print(x != y, end="\n\n")  # returns  False since x and y are same

# MEMBERSHIP OPERATORS
print("apple" in x)  # returns True because "apple" is member of object x
print("mango" not in x)  # returns True because "mango" is not a member of object x
print("\n")

# PYTHON COLLECTIONS(ARRAYS) : list, tuple, set, dictionary

# 1.) List : List Collections are ordered and changeable , Use [] brackets to represent it
# Creating And Printing List
thisList = ["Mango", "Litchi", "Orange", ]
print(thisList)

# Accessing List Item
print(thisList[1])  # "Litchi"
print(thisList[-1])  # -1 refers to last element and -2 to last-second element
print(thisList[1:2])  # ["Litchi", "Orange"]
print(thisList[-2:-1])  # ["Litchi"]   { Here -2(Included) AND -1(Excluded) }
print(thisList[:2])  # 0th indexed element to 2(Excluded)
print(thisList[0:])  # 0th indexed element to last element
print("\n\n")

# Modify List

# Change element at 1st index to "Apple"
thisList[1] = "Apple"
print(thisList)

# Iterate through the list
for x in thisList:
    print(x)
print("\n\n")

# Check if specified item exists
if "Apple" in thisList:
    print("Apple is present in the list!", end="\n\n")

# List length
print(len(thisList), end="\n")

# ADD ITEMS IN THE LIST
thisList.append("Guava")  # add specified element at end of the list
print(thisList)

thisList.insert(0, "Peach")  # Insert specified item at specified index
print(thisList)
print("\n\n")

# DELETE ITEM FROM THE LIST
thisList.remove("Apple")  # remove specified item
print(thisList)

thisList.pop(1)  # To delete at particular index, If(EMPTY) : delete last item
print(thisList)

del thisList[0]  # del keyword to delete at particular index
print(thisList)

del thisList  # del keyword to delete whole list

thisList = ["listItem1"]
thisList.clear()  # Empties the list
print(thisList, "\n\n")

# COPY A LIST
# We cannot use list2 = list1 because list2 will be reference of list1 and changes made to
# list2 will be reflected in list1

toDoList = ["Learn Python", "Give Test in Python", "Do some CP Questions"]
toDoList2 = toDoList.copy()  # Using copy()
toDoList2[2] = "Do CP"
print(toDoList)
print(toDoList2)
print("\n\n")

# Copy Using list()
toDoList3 = list(toDoList)
print(toDoList3)

# JOIN TWO LISTS
# 1.) Using + Operator
rollCodes = ["12", "13", "19", "18"]
names = ["Ishita", "Janak", "Manan", "Virat"]
joinedList = names + rollCodes
print(joinedList)

# 2.) Using extend()
names.extend(rollCodes)
print(names)

# 3.) Using append()
for x in names:
    rollCodes.append(x)
print(rollCodes)
print("\n\n")

# LIST METHODS
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


# PYTHON TUPLES
# Tuples are Collections which are ordered and UNCHANGEABLE.
# Represented using () brackets

# Creation and printing of tuples
thisTuple = ("India", "Canada", "USA")
print(thisTuple)
print("\n\n")

# ACCESS TUPLE ITEMS
print(thisTuple[1])  # Canada
print(thisTuple[0:2])  # ("India", "Canada")
print(thisTuple[-2:-1])  # ("Canada")
print(thisTuple[:2])  # ("India", "Canada")
print(thisTuple[1:])  # ("Canada", "USA")
print("\n\n")

# CHANGE TUPLE VALUE :
# Tuples are unchangeable, or immutable (Its value cannot be changed)
# You can convert the tuple into a list, change the list, and convert the list back into a tuple.
tupleList = list(thisTuple)
tupleList[1] = "China"
thisTuple = tuple(tupleList)
print(tupleList)
print("\n\n")

# Loop through a Tuple
for x in thisTuple:
    print(x)

# Length of the tuple
print(len(thisTuple))

# Check if specified item exist
if "Canada" in thisTuple:
    print("Canada exist in the tuple")
else:
    print("Canada does not exist in the tuple")

print("\n\n")

# ADD ITEMS : We cannot add items to tuple (i.e. They are immutable)
# Create Tuple with one item : Add comma after the item
oneItemTuple = ("oneitem",)
print(oneItemTuple)

# REMOVE ITEMS : We cannot change  item in tuple But can remove the whole tuple using
#                del keyword
del thisTuple
# print(thisTuple) : It will raise an error because thisTuple does not exist

# JOIN TWO TUPLES
firstTuple = ("a", "b", "c")
secondTuple = ("1", "2", "3")
joinedTuple = firstTuple + secondTuple
print(joinedTuple)
print("\n\n")

# TUPLE METHODS
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found


# PYTHON SETS :
# It is a Collection which is un-ordered and un-indexed. {} brackets is used to represent it

# Creation and printing of set
thisSet = {"C++", "Python", "Java", "JavaScript"}
print(thisSet)  # We cannot be sure of order of elements

# ACCESS ITEMS
# You cannot access item using index because they are un-indexed
# But you can loop through them OR Get to know whether a specified item present using 'in'
for x in thisSet:
    print(x)

if "C#" in thisSet:
    print("C# is present in the set")
else:
    print("C# is not present in the set")
print("\n\n")

# CHANGE ITEMS IN SETS
# We cannot change set item but we can add new items
# add() : For one item
# update() : For multiple items

thisSet.add("C#")
print(thisSet)

thisSet.update(["Kotlin", "Go", "Swift"])  # must use [] brackets otherwise items will be splited
print(thisSet)

# Length of set
print(len(thisSet))

# REMOVE ITEMS IN SET

# Using remove() : It will raise an error if item does not exist in set
thisSet.remove("Go")
print(thisSet)

# Using discard() : It will not raise an error if item is not present in the set
thisSet.discard("Swift")
print(thisSet)

# Using pop() : It will delete last item, we will not be knowing which item is deleted
#               It returns the deleted item
deletedItem = thisSet.pop()
print("Deleted Item = " + deletedItem)
print(thisSet)

# clear() : It empties the set
thisSet.clear()
print(thisSet)

# del keyword deletes the set
del thisSet

# JOIN TWO SETS

# Using union() : Returns new set containing all elements from both sets
#                 excluding duplicates
set1 = {"1", "2", "3", "1"}
set2 = ("4", "5", "1")
set3 = set1.union(set2)
print(set3)

# Using update() : Inserts items of second set to first set
#                  excluding duplicates
set1.update(set2)
print(set1)
print("\n\n")

# SET METHODS
# add()	        Adds an element to the set
# clear()	    Removes all the elements from the set
# copy()    	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	     Remove the specified item
# intersection() Returns a set, that is the intersection of two other sets
# intersection_update() :	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 Returns whether two sets have a intersection or not
# issubset()   	 Returns whether another set contains this set or not
# issuperset()	 Returns whether this set contains another set or not
# pop()	         Removes an element from the set
# remove()	     Removes the specified element
# symmetric_difference()	     Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	 Inserts the symmetric differences from this set and another
# union()                   	 Return a set containing the union of sets
# update()	     Update the set with the union of this set and others


# DICTIONARY
# It is a Collection which is un-ordered, changeable and indexed
# Written with curly brackets, they have keys and and values

# Create and print Dictionary
thisDict = {
    "firstName": "Santosh",
    "lastName": "Swansi",
    "rollNo": 732
}
print(thisDict)

# ACCESS ITEMS
fName = thisDict["firstName"]  # get the key value of key : firstName
lName = thisDict.get("lastName")  # get the key value of key : lastName
print(fName + " " + lName)

# CHANGE VALUES
thisDict["firstName"] = "Basudev"

# Loop through dictionary
# It will return keys
for x in thisDict:
    print(x, end=",")
print("\n")

# To print values of keys
for x in thisDict:
    print(thisDict[x], end=",")
print("\n")

# To print values using values()
for x in thisDict.values():
    print(x, end=",")
print("\n")

# To print keys, values using items()
for x, y in thisDict.items():
    print(x, y, sep=":", end=", ")
print("\n\n")

# CHECK IF KEY EXISTS
if "firstName" in thisDict:
    print("key : firstName is present in the dictionary")

# DICTIONARY LENGTH
print(len(thisDict))

# ADDING ITEM
thisDict["Course"] = "B.Sc.(Vocational) CA"
print(thisDict)
print("\n")

# REMOVING ITEMS
thisDict.pop("rollNo")
print(thisDict)

thisDict.popitem()  # To remove last inserted item in the dictionary
print(thisDict)

del thisDict["lastName"]  # To delete specified item
print(thisDict)

thisDict.clear()  # It empties the dictionary
print(thisDict)

del thisDict  # To delete the dictionary completely
print("\n\n")

# COPY A DICTIONARY :
# We cannot use dict2 = dict1 (To copy)
# It is because a reference is copied to dist2, changing dist2 values will get reflected in
# dist1

# Using copy()
thisDict = {
    "firstName": "Santosh",
    "lastName": "Swansi",
    "rollNo": 732
}
thisDict2 = thisDict.copy()
print(thisDict2)

# Using dist()
thisDict3 = dict(thisDict)
print(thisDict3)

# NESTED DICTIONARIES
# METHOD - 1 : Create a Dictionary with three dictionaries

myFamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

# Method - 2: Create a dictionary from three already existing dictionaries

child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myFamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print("\n\n")

# DICTIONARY METHODS :
# clear()	       Removes all the elements from the dictionary
# copy()	       Returns a copy of the dictionary
# fromkeys()	   Returns a dictionary with the specified keys and value
# get()	           Returns the value of the specified key
# items()          Returns a list containing a tuple for each key value pair
# keys()	       Returns a list containing the dictionary's keys
# pop()	           Removes the element with the specified key
# popitem()	       Removes the last inserted key-value pair
# setdefault()	   Returns the value of the specified key.
#                  If the key does not exist: insert the key, with the specified value
# update()	       Updates the dictionary with the specified key-value pairs
# values()	       Returns a list of all the values in the dictionary


# CONDITIONS

# if...else
op1 = 12
op2 = 24
if op1 < op2:
    print(f"{op1} < {op2}")
elif op1 == op2:  # Equivalent to else if in C/C++
    print(f"{op1} = {op2}")
else:
    print(f"{op2} > {op1}")

# Using and, or and not logical operators
op3 = 13
if op2 > op1 and op2 > op3:
    print(f"{op2} is largest")

age = 18
citizenship = "India"
if citizenship == "India" or age >= 18:
    print("Eligible for vote")

isValid = False
if not isValid:
    print("Not valid")
else:
    print("Valid")

# Chaining comparision operators :
if op1 <= op2 >= op3:  # Equivalent to op1 <= op2 and op2 >= op3
    print(f"{op2} is greatest of three {op1}, {op2}, {op3}")

# Nested if
if True:
    if True:
        print("Both conditions passed!")

# Short Hand if...else (Also known as Conditional Expressions and
#                                     Ternary Operators
a = 2
b = 4
print(f"{a} > {b}") if a > b else print(f"{a} < {b}")

# multiple else statements in the same line
# Given statements are equivalent to :
#     if a > b:
#          print("a")
#     elif a == b:
#          print("=")
#     else:
#          print("b")
print("Greater element", end=" = ")
print(f"{a}") if a > b else print("Both are Equal") if a == b else print(f"{b}")

# pass statement
# if statements cannot be empty,
# but if we want then put  pass statement to avoid getting an error.
if True:
    pass  # pass statement

print("\n\n")

# WHILE LOOP

i = 0
while i < 5:
    print(i, end=", ")
    i += 1
    if i == 3:
        continue  # continue with the next iteration
    if i == 3:
        break  # move out of the loop
else:  # It will be implemented when while loop is finished
    print("i is no longer less than 5")
print("\n\n")

# FOR LOOP
# It is used for iterating over a sequence(tuple, dictionary, set, list,
#          string)
# This works more like an iterator
# It does not require indexing variable beforehand

# EXAMPLE :
stores = ["Apple Store", "Samsung Store", "LG Store"]
for x in stores:
    if x == "Samsung Store":
        continue
    if x == "LG Store":
        break;
    print(x)

# Looping through a string
for x in "string":
    print(x, end=",")
else:  # after loop has finished
    print("\nLoop Finished!")

# LOOPING THROUGH A RANGE

# range(x)       : 0 to (x-1), increment = 1
# range(x, y)    : x to (y-1), increment = 1
# range(x, y, z) : x to (y-1), increment = z
for x in range(0, 10, 2):
    print(x, end=",")
print("\n")

# NESTED LOOPS  (Form a square of *)
for x in range(5):
    for y in range(5):
        print("*", end="")
    print(end="\n")

# pass statement in for loop
for x in range(2):
    pass


# FUNCTIONS
def my_func1(arg):
    print(f"Passed argument = {arg}")


my_func1(4)  # Function Call


# PARAMETERS AND ARGUMENTS
# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# ARBITRARY ARGUMENTS (*args)
# If we do not know how many arguments will be passed into your function
# Function will receive a tuple of arguments, and can be accessed
# accordingly


def my_func2(*args):
    print(args[3])


my_func2(1, 2, 3, 4)


# KEYWORD ARGUMENTS
# We can also send arguments with key = value syntax
# Here the order of arguments does not matter


def my_func3(fruit1, fruit2, fruit3):
    print(fruit1 + " " + fruit2 + " " + fruit3)


my_func3(fruit1="Apple", fruit2="Orange", fruit3="Litchi")


# ARBITRARY KEYWORD ARGUMENTS (**kwargs)
# If you do not know how many keyword arguments that will be passed into
# our function, add two asterisk: ** before the parameter name
# in the function definition.
# This way the function will receive a dictionary of arguments,
# and can access the items accordingly:

def my_func4(**name):
    print("First name is " + name["fname"])


my_func4(fname="Santosh", lname="Swansi")


# DEFAULT PARAMETER VALUE :
# It will be used when no argument is passed while calling function

def my_func5(age=18):
    if age >= 18:
        return True
    return False  # return statement


if my_func5():  # Default value will be used
    print("Eligible to vote!")
else:
    print("Not Eligible to vote")


# Passing list as an argument :
def my_func6(mylist):
    for item in mylist:
        print(item, end="")
    print(end="\n")


myList = ["1", "2", "3"]
my_func6(myList)

# pass statement
for x in range(3):
    pass


# RECURSION : (Find nth fib number , fib(0) = 0, fib(1) = 1 )
def fib(firstno, secno, n):
    if n == 0:
        print(firstno)
    elif n == 1 or n == 2:
        print(secno)
    else:
        fib(secno, firstno + secno, n - 1)


fib(0, 1, 7)  # print 5th fibonacci number

# PYTHON LAMBDA (ANONYMOUS FUNCTIONS)
# It is a function without a name
# It can take any number of args but can only have one expression
# The expression is evaluated and result is returned
# SYNTAX : lambda arguments : expression

# EXAMPLE - 1 :
doubler = lambda m: m + 10
print(doubler(4))

# EXAMPLE - 2:
add = lambda n, o, p: n + o + p
print(add(1, 2, 3))
print("\n\n")


# EXAMPLE - 3:
# Why Use Lambda Functions?

# The power of lambda is better shown when you use them as an
# anonymous function inside another function.
# Say you have a function definition that takes one argument,
# and that argument will be multiplied with an unknown number:
def my_func7(n):
    return lambda a1: a1 * n


mydoubler = my_func7(2)
mytripler = my_func7(3)

print(mydoubler(11))
print(mytripler(11))


# ARRAYS
# Note-1: Python does not have built-in support for Arrays,
#         but Python Lists can be used instead.
# Note-2: To work with arrays in Python you will have to import
#         a library, like the NumPy library.


# CLASSES AND OBJECTS
# Properties : Data members of the class
# Methods : Functions inside class
# Python is an Object Oriented Language
# Almost everything in Python is an object, with its properties
# and methods
# class is like a blueprint of object

# create class with property x initialised to 5
class MyClass:
    x = 5


# create object of the class
obj = MyClass()
print(obj.x)


# __init__()  : It is like a constructor in C++
# All classes have a built-in function __init__() which is always
# executed when the class is initiated
# Use it to initialise properties of class
# It is automatically called when we make object of the class

# self : like this in C++(Reference to current instance of class)

class Student:
    def __init__(self, name, student_age):  # Like a constructor
        self.name = name
        self.student_age = student_age

    def print_details(self):  # Method : Function inside class
        print("Name: " + student1.name)
        print(f"Age: {student1.student_age}")


student1 = Student("Ravindra Kumar", 19)
student1.print_details()


# self PARAMETER
# NOTE1: The self parameter is a reference to the current instance of
#        the class, and is used to access variables that belongs to the
#        class.
# NOTE2: It does not have to be named self ,you can call it whatever
#        you like, but it has to be the first parameter of any function
#        in the class:

# EXAMPLE :
class Store:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def print_name(self):
        print("Store Name : " + self.name)


obj1 = Store("Gada Electronics", 1234567890)
obj1.print_name()

# Modify object properties
obj1.name = "Apple Store"
obj1.print_name()

# Delete object properties
del obj1.number

# Delete object
del obj1


# pass statement : If we want to have class without any content
class Person:
    pass


print(end="\n\n")


# INHERITANCE :

# Create a Base(Parent) class (Same as creating any class)
class Animal:
    def __init__(self, category, name):
        self.category = category
        self.name = name

    def print_details(self):
        print("Category : " + self.category)
        print("Name : " + self.name)


# Creating sub(child) class : Pass the base class name in the parenthesis
class Cat(Animal):
    pass  # pass keyword is used when we do not want any method(s) here           # in Cat class


obj2 = Cat("Cat", "Meow")  # will be passed to __init__() of base class
obj2.print_details()


# Adding __init__() in sub-class :
# It will override the parent __init__()
# function . To keep the inheritance of parent __init__() function,
# add a call to parent __init__() function
class Cow(Animal):
    def __init__(self, category, name):
        Animal.__init__(category, name)


# Using super() function
class Tiger(Animal):
    def __init__(self, category, name):
        super().__init__(category, name)


# Adding properties and methods to sub-class :
# If sub-class has a function named same as that of base-class
# then the function of base class will be overridden
class Dog(Animal):
    def __init__(self, category, name, cost):
        super().__init__(category, name)
        self.cost = cost  # Adding property cost to Cow class

    def print_message(self):
        print(f"Boo! my name is {self.name} and my price is {self.cost}")


dogObj = Dog("Dog", "Loyal", 100000)
dogObj.print_message()
print(end="\n\n")

# PYTHON ITERATORS
# Iterators are methods that can be iterated upon.
# Technically, in Python, an iterator is an object which implements
# the iterator protocol, which consist of the methods __iter__() and
# __next__().

# Iterable :
# Lists, tuples, dictionaries, and sets are all iterable objects.
# All these objects have a iter() method which is used to get an iterator:

fruitList = ["Apple", "Banana", "Litchi", "Mango"]
it = iter(fruitList)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# strings are also iterable objects
string = "Hello"
it = iter(string)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

print(end="\n")


# We can use for loop as well for iterating iterable objects
# It creates iterable object and use next() method for each loop


# Create an Iterator :
# NOTE-1 : To create an object/class as an iterator you have to
#          implement the methods __iter__() and __next__() to your object.
# NOTE-2 : As we know all classes have a function called __init__(),
#    which allows you to do some initializing when the object is being created.
# NOTE-3 : The __iter__() method acts similar, you can do operations (initializing etc.),
#          but must always return the iterator object itself.
# NOTE-4 : The __next__() method also allows you to do operations,
#          and must return the next item in the sequence.


# EXAMPLE :
# Create an iterator that returns numbers starting with 1, and each sequence
# will increase by one
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        j = self.a
        self.a += 1
        return j


numObj = MyNumbers()
it1 = iter(numObj)
print(next(it1))
print(next(it1))  # ....
print(end="\n\n")


# STOP ITERATION :
# In above example , iteration will be forever if there are enough
# items. To avoid iteration after specified number of iterations
#  we can use StopIteration statement in __next__() method
class MyNumbers2:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 4:
            k = self.a
            self.a += 1
            return k
        else:
            raise StopIteration  # To raise an error


numObj2 = MyNumbers2()
it = iter(numObj2)

for x in it:
    print(x)

print(end="\n\n")

# SCOPE :
# Local Scope : If variable declared inside function.
# Global Scope : If variable declared in the main body of python code
# global keyword : It used to declare global variable inside function
#          It can also be used to change the global variable inside function


# MODULES :
# It is a code library.
# It contains a set of functions that you may want to include in your python code

# CREATE A MODULE :

# EXAMPLE - 1: (Save it with mymodule.py
#   def greetings(name):
#        print("Hello " + name + "!")

# Use the module

# import mymodule
# mymodule.greetings("Santosh")

# VARIABLES IN MODULE :
# Modules can contain variables of all types(arrays, dictionaries, objects, etc.)

# EXAMPLE - 2 (Save it as mymodule.py)
#  person = {
#   fname = "Santosh"
#   lname = "Swansi"
#   gender = "m"
#  }

# import mymodule
# print("Gender = " + mymodule.person["gender"] )

# RENAMING A MODULE :
# import mymodule as mm  (Here alias of mymodule is mm)

# BUILT-IN MODULES :
sys = platform.system()
ver = platform.version()
print("System : "+sys)
print(f"Version : {ver}")

# To list all functions in a module : Use dir()
# It can be used for user-defined modules as well
x = dir(platform)
print(x)
print(end="\n\n")

# IMPORT A PART OF MODULE : (Following file saved as : mymodule.py)

# def greeting(name):
#   print("Hello, " + name)
#
# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }

# from mymodule import person1
# print(person1["name"]      // Do not use mymodule.person1["name"]


# PYTHON DATETIME :

# The date contains year, month, day, hour, minute, second, and microsecond.
currDateTime = datetime.datetime.now()  # first datetime : module name, second : class name
print(currDateTime)  # prints current date and time

# Return year and name of weekday :
print(currDateTime.year)
print(currDateTime.strftime("%A"))  # %A prints full name of weekday
print(currDateTime.strftime("%a"))  # short name of weekday


# CREATING DATE OBJECTS :
# Others like hour, min, sec, micro-sec, time-zone are optional(=0) and (None for timezone)
dateInit = datetime.datetime(2020, 5, 12)
print(dateInit)


# strftime() Method :
# It is used for formatting date obects into readable strings
# Takes one parameter, format, to specify the format of the string

# EXAMPLE : (Display full name of Month)
print(currDateTime.strftime("%B"))
print(currDateTime.strftime("%b"))  # For displaying short name of month


# LIST OF LEGAL FORMAT CODES :
#    Directive	|       Description         	     |          Example
# ______________________________________________________________________________________
#    %a	             Weekday, short version	                      Wed
#    %A	             Weekday, full version	                    Wednesday
#    %w	        Weekday as a number 0-6, 0 is Sunday	           3
#    %d	              Day of month 01-31	                       31
#    %b	          Month name, short version	                      Dec
#    %B	           Month name, full version	                    December
#    %m	            Month as a number 01-12	                       12
#    %y	        Year, short version, without century	           18
#    %Y	              Year, full version	                      2018
#    %H	              Hour 00-23	                               17
#    %I	              Hour 00-12	                               05
#    %p	              AM/PM	                                       PM
#    %M	              Minute 00-59	                               41
#    %S	              Second 00-59	                               08
#    %f	              Microsecond 000000-999999	                548513
#    %z	              UTC offset	                            +0100
#    %Z	              Timezone	                                  IST
#    %j	              Day number of year 001-366	              365
#    %U	       Week number of year, Sunday : first day , 00-53	  52
#    %W	       Week number of year, Monday : first day , 00-53	  52
#    %c	              Local version of date and time	       Mon Dec 31 17:41:00 2018
#    %x	              Local version of date	                   12/31/18
#    %X	              Local version of time	                   17:41:00
#    %%	              A % character	                               %

# UTC Offset : How much is the current time zone ahead or beside of UTC


# MATH

print(math.pow(2, 5))
print(math.sqrt(5))
print(math.ceil(7/4))
print(math.floor((5/3)))
print(min(12, 23, 14, 19))  # find min and max in an iterable object
print(max(12, 23, 14, 19))
print(math.fabs(-21.2))
print(abs(-2))
print(math.pi)
print("\n\n")

# MATH MODULE METHODS :
# ___________________________
# math.acos(x)	     Returns the arc cosine value of x
# math.acosh(x)	     Returns the hyperbolic arc cosine of x
# math.asin(x)	     Returns the arc sine of x
# math.asinh(x)	     Returns the hyperbolic arc sine of x
# math.atan(x)	     Returns the arc tangent value of x
# math.atan2(y,      x)	Returns the arc tangent of y/x in radians
# math.atanh(x)	     Returns the hyperbolic arctangent value of x
# math.ceil(x)	     Rounds a number upwards to the nearest integer, and returns the result
# math.comb(n, k)	 Returns the number of ways to choose k items from n items without repetition and order

# math.copysign(x, y)	Returns a float consisting of the value of the first parameter
#                        and the sign of the second parameter

# math.cos(x)	     Returns the cosine of x
# math.cosh(x)	     Returns the hyperbolic cosine of x
# math.degrees(x)	 Converts an angle from radians to degrees
# math.dist(p, q)	 Calculates the euclidean distance between two specified points (p and q),
#                    where p and q are the coordinates of that point

# math.erf(x)	     Returns the error function of x
# math.erfc(x)	     Returns the complementary error function of x

# math.exp(x)	     Returns the value of Ex, where E is Euler's number
#                    (approximately 2.718281...), and x is the number passed to it

# math.expm1(x)	     Returns the value of Ex - 1, where E is Euler's number
#                    (approximately 2.718281...), and x is the number passed to it

# math.fabs(x)	     Returns the absolute value of a number
# math.factorial()	Returns the factorial of a number
# math.floor(x)	    Rounds a number downwards to the nearest integer, and returns the result
# math.fmod(x, y)	 Returns the remainder of specified numbers when a number is
#                    divided by another number

# math.frexp()	        Returns the mantissa and the exponent, of a specified value
# math.fsum(iterable)	Returns the sum of all items in an iterable (tuples, arrays, lists, etc.)
# math.gamma(x)	        Returns the gamma value of x
# math.gcd()	        Returns the highest value that can divide two integers
# math.hypot()	        Find the Euclidean distance from the origin for n inputs
# math.isclose()	    Checks whether two values are close, or not
# math.isfinite(x)	    Checks whether x is a finite number
# math.isinf(x)	         Check whether x is a positive or negative infinty
# math.isnan(x)	        Checks whether x is NaN (not a number)
# math.isqrt(n)	        Returns the nearest integer square root of n
# math.ldexp(x, i)	    Returns the expression x * 2i where x is mantissa and i is an exponent
# math.lgamma(x)    	Returns the log gamma value of x
# math.log(x, base)	    Returns the natural logarithm of a number, or the logarithm of number to base
# math.log10(x)	        Returns the base-10 logarithm of x
# math.log1p(x)     	Returns the natural logarithm of 1+x
# math.log2(x)	        Returns the base-2 logarithm of x

# math.perm(n, k)	    Returns the number of ways to choose k items from
#                       n items with order and without repetition

# math.pow(x, y)	    Returns the value of x to the power of y

# math.prod(iterable, *, start=1)	:
#                       Returns the product of an iterable (lists, array, tuples, etc.)

# math.radians(x)	    Converts a degree value (x) to radians
# math.remainder(x, y)	Returns the closest value that can make numerator completely divisible by the denominator
# math.sin(x)	        Returns the sine of x
# math.sinh(x)          Returns the hyperbolic sine of x
# math.sqrt(x)          Returns the square root of x
# math.tan(x)           Returns the tangent of x
# math.tanh(x)          Returns the hyperbolic tangent of x
# math.trunc(x)         Returns the truncated integer parts of x


# PYTHON JSON(JavaScript Object Notation)
# _______________________________________________

# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript Object Notation.

# PARSE JSON : Convert from JSON to Python
# __________________________________________
#              Result will be a Python Dictionary

# json file
jsonFile = '{"name":"Santosh","age":"20","City":"Bundu" }'

# parse json(Convert to python equivalent)
pythonEquivalent = json.loads(jsonFile)

# result is python dictionary
print(pythonEquivalent["name"])


# CONVERT FROM PYTHON TO JSON :
# ________________________________

# Python Object
person = {
    "name": "Santosh",
    "age": 20,
    "city": "Bundu"
}

# Convert it to json
# dumps : s stands for string
# loads : s stands for string

jsonEquivalent = json.dumps(person)

# Print it
print(jsonEquivalent)
print(end='\n\n')

# We can convert Python objects of the following types, into JSON strings:
# _________________________________________________________________________
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None


# PYTHON AND JSON EQUIVALENTS :-
# __________________________________________
# If json contains following types then they will be converted to
# corresponding type in python OR vice-versa

#            Python	                     JSON
# ______________________________________________________________________
#            dict	                     Object
#            list	                     Array
#            tuple	                     Array
#            str	                     String
#            int	                     Number
#            float	                     Number
#            True	                     true
#            False	                     false
#            None	                     null

# Convert a json to Pyhton object :
# _________________________________
person_string = '''{
    "People": [
    {
       "name": "John Smith",
       "phone": "12352672",
       "emails": ["johnsmith123email.com", "smith.john@gmail.com"],
       "has_license": false      
    },
    {
      "name": "Jane Anderson",
      "phone": "7278818",
      "emails": null,
      "has_license": true  
    }
    ]
}
'''

# convert the json string to a python obj:
data = json.loads(person_string)

# access name and phone of the json string from python object (data)
for person in data['People']:
    print(person['name'], person['phone'])

print(end='\n\n')

# delete phone number key from each person:
for person in data['People']:
    del person['phone']

# Convert python object to json string
new_people_string = json.dumps(data, indent=2)
print(new_people_string, end='\n\n')

# EXAMPLE - 1 : (TO CONVERT ALL SUPPORTED PYTHON OBJECTS TO JSON STRINGS)
# ___________________________________________________________________

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print(end="\n")


# EXAMPLE - 2 : (TO CONVERT ALL SUPPORTED PYTHON OBJECTS TO JSON STRINGS)
# ________________________________________________________________________

allSupportedPyObjects = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print("Without indentation : ")
print(json.dumps(allSupportedPyObjects))
print(end="\n\n")

# FORMAT THE RESULT : (To make it easy to read)
# Use indentation and separators in dumps() method

print("With Indentation : ")
print(json.dumps(allSupportedPyObjects, indent=4))
print(end="\n\n")


# , and a space : To separate each object,
# -> and a space : To separate keys from values
print("With Indentation and separators : ")
print(json.dumps(allSupportedPyObjects, indent=4, separators={": ", ", "}))
print(end="\n\n")


# ORDER THE RESULT :
# ___________________
# Use the sort_keys param in dumps() method : True/False
print("With Indentation And Sorted Keys : ")
print(json.dumps(allSupportedPyObjects, indent=4, sort_keys=True))


# REAL WORLD EXAMPLE (JSON) :
# ____________________________
# Convert given EUR to any other currency :

r = requests.get('https://api.exchangeratesapi.io/latest')

for_ex_rates_USD = dict()

# converting given json string to python object so that we can work on
# it
rates_data = json.loads(r.text)

print(rates_data)
# print EUR equivalent in different currency :
for rate in rates_data['rates']:
    print(rate, rates_data['rates'][rate])


# json.load() :
# ______________
with open('states.json') as f:

    # Load the file(Convert it to python object) so that we can use it
    US_states_data = json.load(f)
    print(US_states_data)

# json.dump() :
# ____________________________________________________________________
# The dump() method is used when the Python objects have to be
# stored in a file.
# ____________________________________________________________________
# SYNTAX : dump(python equivalent of json, file_object)
# _____________________________________________________________________

# Dump the python equivalent of json to a new file without area codes
with open('states.json') as file:

    # Deleting the area_codes key in python object and not the json file
    US_states_data = json.load(file)
    for data in US_states_data['states']:
        del data['area_codes']

    with open('new_states.json', 'w') as new_file:
        json.dump(US_states_data, new_file, indent=2)


# REGULAR EXPRESSIONS (RegEx) :
# _____________________________________

# Regular Expression is a sequence of characters that form a search
# pattern.
# It can be used to check whether a string contains a specified search
# pattern.
# import re module to use regular expression

# Raw string :
# If we place r OR R before the string it will be treated as raw string
# For e.g.
print(R"\tHello")  # Here \ and s will be two different characters
print(r"\tHello")  # Same
print("\tHello")   # Here \t is a escape character for tab-space
print(end="\n\n")

# EXAMPLE:
# (Search a sub-string beginning with "The" and ending with "down")
# ^ : Begin with specified sequence of character
# $ : End with specified sequence of characters
# . : Any character (Except \n character)
# * : 0 or more occurrences
txt = "The sun is going down"
listOfFoundPatterns = re.search(r"^The.*down$", txt)
print(listOfFoundPatterns)


# RegEx Functions :
# _________________

# Function	   |                             Description
# ___________________________________________________________________
#  findall	               Returns a list containing all matches
#  search                      Returns a Match object (if any)
#  split	                Returns a list of split-ed strings
#  sub	                 Replaces one or many matches with a string
listFindAll = re.findall("s", txt)
print(listFindAll)

matchObj = re.search("i", txt)
print(matchObj)

splitList = re.split("i", txt)
print(splitList)

# Replace count = 1 occurrences of "i"  with "t" in txt
replacedTxt = re.sub("i", "t", string=txt, count=1)
print(replacedTxt)


# METACHARACTERS : ( Characters with a special meaning )
# _____________________
#
# Character	            Description	                Example
# _____________________________________________________________________
#  []	           A set of characters	             "[a-m]"
#  \	    Signals a special sequence (can also be used to escape special characters)	"\d"
#  .	            Any char (except \n char)	     "he..o"
#  ^	                Starts with	                 "^hello"
#  $	                 Ends with	                 "world$"
#  |	                 Either or	               "falls|stays"
# ()                  Capture and group


# QUANTIFIERS :
# _______________

# Character	            Description	                Example
# _____________________________________________________________________
#  *	              0 or more occurrences	          "aix*"
#  +	              1 or more occurrences	          "aix+"
#  {}             Specified no of occurrences	      "al{2}"


# SPECIAL SEQUENCES :
# ___________________
# -> A special sequence is a \ followed by one of the characters
#   in the list below, and has a special meaning:

# Character	           Description	                   Example
# ______________________________________________________________________
# \A	               at the beg 	                   "\AThe"
# \Z	             at the end                        "Spain\Z"
# \b          beg or at the end of a word         r"\bain", r"ain\b"
# \B	    NOT at the beg (or end) of a word     r"\Bain", r"ain\B"
# \d	            digits ( 0-9)	                    "\d"
# \D	        DOES NOT contain digits	                "\D"
# \s	         white space character	                "\s"
# \S	    DOES NOT contain a white space char         "\S"
# \w	  any word characters (a-z, A-Z, 0-9, _)	    "\w"
# \W	     DOES NOT contain any word char	            "\W"


# SETS :
# It is a set of char inside a pair of sq. brackets [] with a special meaning:

# EXAMPLE :
# [a-zA-Z.+] : If there exist any char of the Set[a..z,A..Z,1..9,.,+]


# MATCH OBJECT :
# _______________
# It contains information about the search and the result
# If there is no match : None will be returned


# PROPERTIES AND METHODS of Match object :-
# _____________________________________________________________________
#  METHODS  |                DESCRIPTION
# _____________________________________________________________________
# .span()      returns a tuple (start, end) of the match
# .string      returns the string passed into the function
# .group()   returns the part of the string where there was a match

# EXAMPLE :
# ____________
txt = "The rain in Spain"

# Print a string begin or end with "S" followed by 1 or more
# occurrences of word characters (a-z, A-Z, 0-9, _)
x = re.search(r"\bS\w+", txt)
print(x.span())    # It will give us beg and end positions of pattern

print(x.string)    # It will print the string passed into search()

print(x.group())   # It will give us part of matched string


# EXAMPLE CONTAINING ALL CONCEPTS :
# __________________________________

string = """
Hello how are you ?
violinhi@yahoo.com
augusto@yahoo.ca
bwcarty@att.net
dprice@msn.com
staikos@optonline.net
psharpe@mac.com
andale@yahoo.com
magusnet@icloud.com

123.133.1234
124.789.1378
661.213.1883

ASCII characters.
Is@possible
hello.com
"""

# Search e-mail addresses using RegEx :
foundEMailAdds = re.findall(r"[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,4}", string)

# DESCRIPTION :
# ____________________________________________________________________
# [\w.%+-]+  : Match 1 or more char of set {a-z,A-Z,.,%,+,-}
# @          : Exact char match
# [\w.-]+    : Match 1 or more char of set {a-z,A-Z,.,-}
# \.         : Any char ( except \n )
# [a-zA-Z]   : Match any one char of set {a-z,A-Z}
# {2,4}      : Match at least 2 times but no more than 4 times
print(foundEMailAdds)


# PIP :
# _____
# PIP is a package manager for Python packages.

# WHAT IS A PACKAGE ?
# ___________________
# A package contains all the files we need for a module.
# Modules are Python code libraries you can include in your project.

# Check If PIP is installed   : pip --version
# Download a package          : pip install numpy
# Remove a package            : pip uninstall numpy
# List packages               : pip list

# Using a package :
# _________________
arr = numpy.array({10, 12, 14, 19})
print(arr)
print(end="\n\n")


# PYTHON TRY... EXCEPT (ERROR HANDLING IN PYTHON):
# ________________________________________________

try:                        # try contains error occurring python codes
    print(mask)
except NameError:  # If error is due to var not defined catch with NameError
    print("Variable mask is not defined")
except:            # To catch unknown error
    print("Exception has occurred!")
else:
    print("Nothing went wrong!")

# finally : Its statement will be executed regardless of error occurred
#           OR not
try:
    print(5/0)
except ZeroDivisionError:
    print("Division by zero")
finally:
    print("Try...Except block is finished!")

# finally can be useful to close objects and clean up resources:
try:
    file = open("my.txt", "r")
    file.write("Welcome to my notes!")
except:
    print("Something went wrong while writing to the file")
finally:
    file.close()


# THROW( or RAISE ) AN EXCEPTION :
# _________________________________
# Use raise keyword

# (Uncomment it to test it)
"""
v = 101
if v > 100:
   raise Exception("Number is greater than 100.")
"""

# Raising specific error (Uncomment it to test its working)
"""
 code = "Kanke"
 if not type(code) is int:
     raise TypeError("Integers values are excepted")
"""

# GETTING USER INPUT :
# ____________________

# USING input() [Python 3] { raw_input() [Python 2] }:
# ____________________________________________________
yourName1 = input("Name : ")
print("Name : "+yourName1)


# FORMAT THE OUTPUT :
# _____________________

# NOTE-1 : Sometimes there are parts of a text that you do not control,
#         maybe they come from a database, or user input?
# NOTE-2 : To control such values add placeholder ( {} brackets)
#          in the output string

price = 1234
priceMsg = "Price of the item is {}"
print(priceMsg.format(price))

# Adding parameter inside the place holder to specify how to convert
# value :
priceMsg = "Price of the item is {:.2f}"   # 2 decimal points
print(priceMsg.format(price))

# Formatting Types :
# ___________________

#  :<		Left aligns the result (within the available space)
#  :>		Right aligns the result (within the available space)
#  :^		Center aligns the result (within the available space)
#  :=	  	Places the sign to the left most position
#  :+		   + sign to indicate if the result is +ve or -ve
#  :-		   - sign for -ve values only
#  : 		space to insert an extra space before +ve nos. (and a - sign before -ve nos.)
#  :,		comma as a thousand separator
#  :_		underscore as a thousand separator
#  :b		Binary format
#  :c		corresponding unicode character
#  :d		Decimal format
#  :e		Scientific format (lower case e)
#  :E		Scientific format (upper case E)
#  :f		Fix point number format
#  :F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
#  :g		General format
#  :G		General format (using a upper case E for scientific notations)
#  :o		Octal format
#  :x		Hex format, lower case
#  :X		Hex format, upper case
#  :n		Number format
#  :%		Percentage format

marks = 0.89
percentFormat = "Percentage obtained : {:%}"
print(percentFormat.format(marks))

# Multiple placeholders :
# _______________________
quantity = 3
itemNo = 567
price = 49
myOrder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myOrder.format(quantity, itemNo, price))

# Indexed Placeholders :
# _______________________
myOrder = "I want {0} pieces of item number {2} for {1:.2f} dollars."
print(myOrder.format(quantity, price, itemNo))

# Named Placeholders :
# ____________________
myOrder = "I want {count} pieces of item number {itemNo} for {price:.2f} dollars."
print(myOrder.format(count=5, itemNo=123, price=1234))
print(end="\n\n")

# PYTHON FILE HANDLING :
# ______________________

# OPENING A FILE :
# ________________
# open() methods has two parameters : file_name, mode(singular)
#   MODES       |                           DESCRIPTION
# ____________________________________________________________________
#     r           read mode, error if file does not exist (default)
#     w           write mode, creates the file if it does not exist
#     a           append mode, creates the file if it does not  exist
#     x           create mode, error if file exist

# We can mention if the file should be handled BINARY OR TEXT mode
# _________________________________________________________________
#    t            Text mode (Default)
#    b            Binary mode (e.g. images)

file = open("myFile.txt", "w")  # write
file.write("""Welcome to my file!
You have the following tasks""")
file.close()  # close the file


# OPEN A FILE ON THE SERVER :
# ____________________________

# Use open() method which returns a file object, which has a read()
# method for reading the content of the file
file2 = open("myFile.txt", "r")

# Uncomment one-by-one to check its working :
# ___________________________________________________________________
# CAUTION : Once you have read the file, the read pointer will
#             be at end and it has nothing to read
# ___________________________________________________________________

print(file2.read())   # It will read all contents of the file
# print(file2.read(5))  # It will read only 5 characters
# print(file2.readline())  # Reads first line
# print(file2.readline())  # Reads second line

# for x in file2:      # Reads all contents of the file
#     print(x)

# CLOSE FILE : When we are done using it.
# ________________________________________
file2.close()
print(end="\n\n")

# WRITING TO AN EXISTING FILE :
# _______________________________

# Use 'a' OR 'w' modes to write in a file
# 'a' will append the contents
# 'w' will overwrite if there were existing contents

f = open("newFile.txt", "a")
f.write("""Demo File For Testing Python File Handling :
lorem ipsum adkfhkjs jdgldnk hykiabiy gtsj  ygoqhiuyguyq uiv
jahfj nvuhlgk gkhvi
""")

f = open("newFile.txt", "r")
print(f.read())

f.close()

# Write mode after Append (Overwrite the existing contents) :
f = open("newFile.txt", "w")
f.write("Newly added contents")
f.close()

f = open("newFile.txt", "r")
print(f.read())
f.close()

# DELETE A FILE :
# ________________

# closed files are deleted only!
# Use remove() method of os module :
os.remove("newFile.txt")  # delete the existing file

# CHECK IF FILE EXISTS or NOT :
# ______________________________
# To avoid getting error, we can check for existence of the file
# before deleting!
if os.path.exists("myFile.txt"):
    os.remove("myFile.txt")
else:
    print("File does not exist!")
print(end="\n\n")

# TO REMOVE A DIRECTORY : (Can only remove empty folders)
# ________________________
# os.rmdir("myFolder")


# map() Function :
# _________________
# It executes specified function for each in the iterable. The item is
# sent to the function as a parameter

# SYNTAX : map(function, iterables)
# ___________________________________
# function : It is required to execute for each item
# iterables : A sequence, collection or iterator object.

# EXAMPLE - 1 :
# ______________


def function(par):
    return len(par)


res = map(function, ["Apple", "Orange", "Mango"])
print(list(res))  # Convert the map into a list and print it

print("Print a list of elements :", end="")
inputs = map(int, input().split())
print(list(inputs))


def function(a, b):
    return a + b


x = map(function, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(list(x))


# filter() in Python :
# ____________________

# filter(function, iterable_object) will pass each item through the
# function to test if the item is accepted or not
# It returns an iterator

# Validate age
def filter_func(age):
    if age >= 18:
        return True
    else:
        return False


valid_age_iter = filter(filter_func, [12, 45, 13, 18, 12, 78, 16, 18])
for x in valid_age_iter:
    print(x)
