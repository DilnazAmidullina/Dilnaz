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

#example
# print((6 + 3) - (6 + 3))

#example
print(100 + 5 * 3)










