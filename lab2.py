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



















