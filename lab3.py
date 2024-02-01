FUNCTIONS


def my_function():
  print("Hello from a function")


calling a function

def my_function():
  print("Hello from a function")

my_function()


arguments

def my_function(fname):
  print(fname + "Refnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


number of arguments

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


Error

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")


arbitrary arguments, *args

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


keyword arguments

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus" )


Arbitrary Keyword Arguments, **kwargs

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


Default Parameter Value

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")