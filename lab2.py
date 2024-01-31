#booleans

#example1
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

#example2
# a = 200
# b = 33

# if b > a:
#     print("b is greater than a")
# else:
#     print("b is not greater than a")

#example3
# print(bool("Hello"))
# print(bool(15))

#example4
# x = "Hello"
# y = 15

# print(bool(x))
# print(bool(y))

#example5
# print(bool("abc"))
# print(bool(123))
# print(["apple", "cherry", "banana"])

#example6
# bool(False)
# bool(None)
# bool(0)
# bool(())
# bool("")
# bool([])
# bool({})

#example7
# class myclass():
#     def __len__(self):
#         return 0
    
# myobj = myclass()
# print(bool(myobj))

# example8
# def myFunction():
#     return True

# print(myFunction())

#example9
# def myFunction():
#     return True

# if myFunction():
#     print("YES!")
# else:
#     print("NO!")

# example9
# x = 200
# print(isinstance(x, int))

#exercise1
# print(10 > 9)
# True

# #exercise2
# print(10 == 9)
# False

# #exercise3
# print(10 < 9)
# False

# #exercise4
# print(bool("abc"))
# True

# #exercise5
# print(bool(0))
# False



#operators

#example
# print(10+5)

#example
# x = 5
# y = 3
# print(x + y)

#example
# x = 5
# y = 3
# print(x - y)

#example
# x = 5
# y = 3
# print(x * y)

#example
# x = 12
# y = 3
# print(x / y)

#example
# x = 5
# y = 2
# print(x % y)

#example
# x = 2
# y = 5
# print(x ** y) #2*2*2*2*2

#example
# x = 15
# y = 2
# print(x // y)
#the floor division // rounds the result down to the nearest whole number



#assingment operators

#example
# x = 5
# print(x)

#example
# x = 5
# x += 3
# print(x)

#example
# x = 5
# x -= 3
# print(x)

#example
# x = 5
# x /= 3
# print(x)

#example
# x = 5
# x %= 3
# print(x)

# example
# x = 5
# x //= 3
# print(x)

# example
# x = 5
# x **=3
# print(x)

# AND
# x = 5
# x &= 3
# print(x)
#output 1 

#OR
# x = 5
# x |= 3
# print(x) 
# outputs 7 

#XOR 
# x = 5
# x ^= 3
# print(x)
# outputs 6

#number is shifted to the left
# x = 5
# x <<= 3
# print(x)

# number is shifted to the right
# x = 5
# x >>= 3
# print(x)



# comparison operators

# equal
# x = 5
# y = 3
# print(x == y)

# not equal
# x = 5
# y = 3
# print(x != y)

# greater than
# x = 5
# y = 3
# print(x > y)

# less than
# x = 5
# y = 3
# print(x < y)

# greater than or equal to
# x = 5
# y = 3
# print(x >= y)

# Less than or equal to
# x = 5
# y = 3
# print(x <= y)



# logical operators

# and
# x = 5
# print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10

# or
# x = 5
# print(x > 3 or x < 4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

# not
# x = 5
# print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result



# identity operators

# is
# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z)
# print(x is y)
# print(x == y)


# is not
# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is not z)
# print(x is not y)
# print(x != y)



# membership operators

# in
# x = ["apple", "banana"]
# print("banana" in x)

# not in
# x = ["apple", "banana"]
# print("pineapple" not in x)



# bitwise operations

# &  AND
# print(6 & 3)

# outputs 2

#|  OR
# print(6 | 3)

# outputs 7

# ^ XOR
# print(6 ^ 3)

# outputs 5
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 0

# ~  NOT
# print(~4)

# outputs -4
# 0 1 
# 1 0

# <<  zero fill left shift
# print(3 << 2)

# outputs 12

"""
Shift left by pushing zeros in from the right and let the leftmost bits fall off
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""

# >> signed right shift
# print(8 >> 2)

# outputs 2

"""
Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""



# operator precedence (order of operations)

#parenthese
# print((6 + 3) - (6 + 3))

#multiplication, division, floor division, and modulus (higher precedence)
# print(100 + 5 * 3)

#addition and substraction
# print(100 - 5 * 3)

# Bitwise left and right shifts (lower precedence)
# print(8 >> 4 - 2)

# outputs 2

# Bitwise AND (lower precedence)
# print(6 & 2 + 1)

# outputs 2

# Bitwise XOR (lower precedence)
# print(6 ^ 2 + 1)

# outputs 5

# Bitwise OR (lower precedence)
# print(6 | 2 + 1)

# outputs 7

# comparisons, identity, and membership operators (lower precedence)
# print(5 == 4 + 1)

# outputs true 

# logical NOT (lower precedence)
# print(not 5 == 5)

# outputs False


# and (higher precedence)
# print(1 or 2 and 3)

# outputs 1

# or (lower precedence)
# print(4 or 5 + 10 or 8)

# outputs 4


#example (addition = substraction)
# print(5 + 4 - 7 + 3)

# outputs 5


#exercise1
# print(10*5)

#exercise2
# print(10/2)

# exercise3
# fruits = ["aqpple", "banana"]
# if "apple" in fruits:
#     print("Yes, apple is in fruit!")

# exercise4
# if 5 != 10:
#     print("5 anf 10 are not equal")

# exercise5
# if 5 == 10 or 4 == 4:
#     print("At least one of the statements is true")




# Lists

# example
# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# duplicates
# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)

# length
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# data types
# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]

# print(list1)
# print(list2)
# print(list3)

# different data types
# list1 = ["abc", 34, True, 40, "male"]

# print(list1)

# type()
# mylist = ["apple", "banana", "cherry"]

# print(type(mylist))

# outputs <class 'list'>


# list()
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)


# access list items

# example
# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

# negative indexing
# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

# range of indexes
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# example
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# example
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# Range of Negative Indexes
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# example
# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

# change item Value
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# change a range of item Value
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# insert new value 
# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# insert less items than replace
# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# insert() without replacing
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

add item at the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

insert items at specified Index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

append elements from another list to the current list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

add other iterable object
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

