# CLASSES

# Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.

# class my_class:
#     def getString(self):
#         a = str(input())
#         return a
#     def printString(self, c):
#         print(c.upper())
# p1 = my_class()
# b = p1.getString()
# p1.printString(b)


# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

# class Shape:
#     def area(self, a = 0):
#         print(a)
# class Square(Shape):
#     def __init__(self, length):
#         self.length = length
#     def area(self):
#         print(self.length * self.length)
# p1 = Shape()#p1 is an object of class
# p2 = Square(2)#p2 is an object of a subclass
# p1.area()
# p2.area()


# Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.

# class Shape:
#     def area(self, a = 0):
#         print(a)
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         print(self.length * self.width)
# p1 = Rectangle(4, 5)#p1 is an object of a Rectangle subclass
# p2 = Shape()#p2 is an object of a class Shape
# p1.area()
# p2.area()


# Write the definition of a Point class. Objects from this class should have a
# a method show to display the coordinates of the point
# a method move to change these coordinates
# a method dist that computes the distance between 2 points

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def show(self):
#         print(f"({self.x},{self.y})")
#     def move(self):
#         self.x = int(input("new x coordinate: "))
#         self.y = int(input("new y coordinate: "))
#     def dist(self, obj):
#         print ((((obj.x - self.x)**2) + ((obj.y - self.y)**2))**0.5)
# p1 = Point(2, 4)#added point 1
# p2 = Point(5, 6)#added point 2
# p1.show()#see the coordinates of point 1
# p1.move()#change the coordinates of point 1
# p1.show()#see how the coordinates of point 1 have changed
# p2.show()#see the coordinates of point 2
# p1.dist(p2)#see the distance between point 1 and point 2


# Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

# class bank_account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, d):
#         self.balance += d
#     def withdraw(self, w):
#         if w > self.balance:
#             print("withdrawals may not exceed the available balance")
#         else:
#             self.balance -= w
#     def __str__(self):
#         return (f"{self.owner}, {self.balance}")
# p1 = bank_account("Dilnaz", 10000)
# print(p1)
# p1.deposit(10000)
# print(p1)
# p1.withdraw(5000)
# print(p1)
# p1.withdraw(10000)
# print(p1)


# Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.


    


