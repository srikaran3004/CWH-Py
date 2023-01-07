# The conversion of one data type into the other data type is known as type casting in python or type conversion in python.

# Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python

# Two Types of Typecasting:
# Explicit Conversion (Explicit type casting in python)
# Implicit Conversion (Implicit type casting in python)

# To make a same line copy down we use shift+alt+downward arrow 

a = "1"
# a = 1
b = "2"
# b = 2
print(int(a) + int(b)) 
# Here int converts the a and b into an integer then performs the operation and prints the output 

# Implicit TypeCasting
c = 1.9
d = 8

print(c + d)
# Explicit 
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)

# Implicit
# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))


