# #HOME

# #example
# print("Hello, world!")

# #exercise 1
# print("Hello world")

# #PYTHON SYNTAX
# #example
# if 5 > 2:
#     print("Five is greater than two!")

#syntax error
# if 5 > 2:
# print("Five is greater tha two!")

# #example
# if 5 > 2:
#     print("Five is greater than two!")
# if 5 > 2:
#         print("Five is greater than two!")

# #syntax error
# if 5 > 2:
#      print("Five is greater than two!")
#         print("Five is greater than two!")
     
# #python variables
# x = 5
# y = "Hello, world!"

# print(x)
# print(y)

# #comments

# #This is a comment.
# print("Hello, World!")

# #exercise 2
# if 5 > 2:
#      print("YES")



# variables

#example
# x = 5
# y = "John"

# print(x)
# print(y)

# #example
# x = 4
# x = "Sally"
# print(x)

# #example
# x = str(3)   #x will be 3
# y = int(3)   #y will be 3
# x = float(3)  #z will be 3

# #example
# x = 5
# y = "John"
# print(type(x))
# print(type(y))

# #example
# x = "John"
# print(x)
# #double quotes are the same as single quotes:
# x = 'John'
# print(x)

# #example
# a = 4
# A = "Sally"
# print(a)
# print(A)
# #A will not overwrite a


# #variable names

# #example
# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"


# print(myvar)
# print(my_var)
# print(_my_var)
# print(myVar)
# print(MYVAR)
# print(myvar2)

# #illegal variable names
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# #camel case
# myVariableName = "John"

# #pascal case
# MyVariableName = "John"

# #snake case
# my_variable_name = "John"


# #assign multiple values

# #example
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# #one value to multiple variables
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)


#output variables

# x = "Python is awesome"
# print(x)

#example
# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)

#example
# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)

# #example
# x = 5
# y = 10
# print(x + y)

# #error example
# x = 5
# y = "John"
# print(x + y)

# #example
# x = 5
# y = "John"
# print(x, y)


#global variables

#example
# x = "awesome"

# def myfunc():
#     print("Python is " + x)

# myfunc()

#example
# x = "awesome"

# def myfunc():
#     x = "fantastic"
#     print("Python is " + x)

# myfunc()

# print("Pythos is " + x)

#global keyword
# def myfunc():
#     global x
#     x = "fantastic"

# myfunc()

# print("Python is " + x)

#example
# x = "awesome"

# def myfunc():
#     global x
#     x = "fantastic"

# myfunc()

# print("Python is " + x)


#exercise1
# carname = "Volvo"

# #exercise2
# x = 50

# #exercise3
# x = 5
# y = 10
# print(x + y)

# #exercise4
# x = 5
# y = 10
# z = x + y
# print(z)

# #exercise5
# x, y, z = "Orange", "Banana", "Cherry"

# #exercise5
# x=y=z = "Orange"

# #exercise5
# def myfunc():
#     global x
#     x = "fantastic"



# comments


# #example

# #This is comment
# print("Hello, World!")

# #example
# print("Hello, World!") #This is comment

# #example

# #print("Hello, World!")
# print("Cheers, Mate!")

# #multiline comments

# #This is a comment
# #written in
# #more than just one line
# print("Hello, World!") 

# #example
# """

# This is comment
# written in 
# more than just one line

# """

# print("Hello, World!")

# #exercise 1
# #This is comment
# """

# This is comment
# written in 
# more than just one line

# """


# data types

# #example
# x = 5
# print(type(x))

# #example
# x = "Hello World"
# print(x)
# print(type(x))

# #example
# x = 20
# print(x)
# print(type(x))

# #example
# x = 20.5
# print(x)
# print(type(x))

# #example
# x = 1j
# print(x)
# print(type(x))

# #example
# x = ["apple", "banana", "cherry"]
# print(x)
# print(type(x))

# #example
# x = ("apple", "banana", "cherry")
# print(x)
# print(type(x))

# #example
# x = {"name" : "John", "age" : 36}
# print(x)
# print(type(x))

# #example
# x = range(6)
# print(x)
# print(type(x))

# #example
# x = frozenset({"apple", "banana", "cherry"})
# print(x)
# print(type(x))

# #example
# x = True
# print(x)
# print(type(x))

# #example
# x = {"apple", "banana", "cherry"}
# print(x)
# print(type(x))

# #example
# x = b"Hello"
# print(x)
# print(type(x))

# #example
# x = bytearray(5)
# print(x)
# print(type(x))

# #example
# x = memoryview(bytes(5))
# print(x)
# print(type(x))

# #example
# x = None
# print(x)
# print(type(x))

# #example
# x = str("Hello World")
# print(x)
# print(type(x))

# #example
# x = int(20)
# print(x)
# print(type(x))

# #example
# x = float(20.5)
# print(x)
# print(type(x))

# #example
# x = complex(1j)
# print(x)
# print(type(x))

# #example
# x = list(("apple", "banana", "cherry"))
# print(x)
# print(type(x))

# #example
# x = tuple(("apple", "banana", "cherry"))
# print(x)
# print(type(x))

# #example
# x = range(6)
# print(x)
# print(type(x))

# #example
# x = dict(name="John", age=36)
# print(x)
# print(type(x))

# #example
# x = set(("apple", "banana", "cherry"))
# print(x)
# print(type(x))

# #example
# x = frozenset(("apple", "banana", "cherry"))
# print(x)
# print(type(x))

# #example
# x = bool(5)
# print(x)
# print(type(x))

# #example
# x = bytes(5)
# print(x)
# print(type(x))

# #example
# x = bytearray(5)
# print(x)
# print(type(x))

# #example
# x = memoryview(bytes(5))
# print(x)
# print(type(x))


# #exercise1
# x = 5
# print(type(x))

# int

# #exercise2
# x = "Hello World"
# print(type(x))

# str

# #exercise3
# x = 20.5
# print(type(x))

# float

# #exercise4
# x = ["apple", "banana", "cherry"]
# print(type(x))

# list

# #exercise5
# x = ("apple", "banana", "cherry")
# print(type(x))

# tuple

# #exercise6
# x = {"name" : "John", "age" : 36}
# print(type(x))

# dict

# #exercise7
# x = True
# print(type(x))

# bool


# casting

#integers
# x = int(1)
# y = int(2.8)
# z = int("3")
# print(x)
# print(y)
# print(z)

#strings
# x = str("s1")
# y = str(2)
# z = str(3.0)
# print(x)
# print(y)
# print(z)

#float
# x = float(1)
# y = float(2.8)
# z = float("3")
# w = float("4.2")
# print(x)
# print(y)
# print(z)
# print(w)

numbers

#example
# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# print(type(x))
# print(type(y))
# print(type(z))

#int
# x = 1
# y = 35656222554887711
# z = -3255522

# print(type(x))
# print(type(y))
# print(type(z))

#float
# x = 1.10
# y = 1.0
# z = -35.59

# print(type(x))
# print(type(y))
# print(type(z))

# #example
# x = 35e3
# y = 12E4
# z = -87.7e100

# print(type(x))
# print(type(y))
# print(type(z))

# #complex
# x = 3+5j
# y = 5j
# z = -5j

# print(type(x))
# print(type(y))
# print(type(z))

# #type conversion
# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# #convert from int to float:
# a = float(x)

# #convert from float to int:
# b = int(y)

# #convert from int to complex:
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))

# #random

# import random

# print(random.randrange(1,10))


#exercise1
x = 5
x = float(x)

#exercise2
x = 5.5
x = int(x)

#exercise3
x = 5
x = complex(x)



string


# #string
# print("Hello")
# print('Hello')

# #example
# a = "Hello"
# print(a)

# #example
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

# #example
# a = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(a)

# #example
# a = "Hello, World!"
# print(a[1])

# #example
# for x in "banana":
#       print(x)

# #example
# a = "Hello, World!"
# print(len(a))

# #example
# txt = "The best things in life are free!"
# print("free" in txt)

# #example
# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")

# #example
# txt = "The best things in life are free!"
# print("expensive" not in txt)

# #example
# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")


# #slicing
# b = "Hello, World!"
# print(b[2:5])

# #slice from the start
# b = "Hello, World!"
# print(b[:5])

# #slice to the end
# b = "Hello, World!"
# print(b[2:])

# #negative indexing
# b = "Hello, World!"
# print(b[-5:-2])


# #uppercase
# a = "Hello, World!"
# print(a.upper())

# #lowercase
# a = "Hello, World!"
# print(a.lower())

# #remove whitespace
# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"

# #replace string
# a = "Hello, World!"
# print(a.replace("H", "J"))

# #split string
# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']

# #string concatenation
# a = "Hello"
# b = "World"
# c = a + b
# print(c)

# #example
# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# #format strings
# #error
# age = 36
# txt = "My name is John, I am " + age
# print(txt)

# #insert numbers into strings
# age = 36
# txt = "My name is John, I am {}"
# print(txt.format(age))

# #example
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))

# #example
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))


# #error 
# txt = "We are the so-called "Vikings" from the north."

# #example
# txt = "We are the so-called \"Vikings\" from the north."

# #single quote
# txt = 'It\'s alright.'
# print(txt) 

# #backslash
# txt = "This will insert one \\ (backslash)."
# print(txt) 

# #newline
# txt = "Hello\nWorld!"
# print(txt) 

# #carriage retern
# txt = "Hello\rWorld!"
# print(txt) 

# #tab
# txt = "Hello\tWorld!"
# print(txt) 


# #This example erases one character (backspace):
# txt = "Hello \bWorld!"
# print(txt) 

# #octal value
# txt = "\110\145\154\154\157"
# print(txt) 

# #hex
# txt = "\x48\x65\x6c\x6c\x6f"
# print(txt) 

# #exercise1
# x = "Hello World"
# print(len(x))

# #exercise2
# txt = "Hello World"
# x = txt[0]

# #exercise3
# txt = "Hello World"
# x = txt[2:5]

# #exercise4
# txt = " Hello World "
# x = txt.strip()

# #exercise5
# txt = "Hello World"
# txt = txt.upper()

# #exercise6
# txt = "Hello World"
# txt =  txt.lower()

# #exercise7
# txt = "Hello World"
# txt = txt.
# replace("H", "J")

# #exercise8
# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))




























