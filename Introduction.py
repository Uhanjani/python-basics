<html>
<head><title>python</title></head>
<body>
 <pre>
#Basics of python
#A.write a progrm to display the statement
print("Hello, World!")
#B.write a program to demonistrate the basic data types in python
#int
a=10
print(a)
print(type(a))
#float
b=10.5
print(b)
print(type(b))
#complex
c=10+5j
print(c)
print(type(c))
#string
d="Hello"
print(d)
print(type(d))
#boolean
e=True
print(e)
print(type(e))
#list
f=[10,20,30,40,50]
print(f)
print(type(f))
#tuple
g=(10,20,30,40,50)
print(g)
print(type(g))
#set
h={10,20,30,40,50}
print(h)
print(type(h))
#frozenset
i=frozenset({10,20,30,40,50})
print(i)
print(type(i))
#dictionary
i={1:"one",2:"two",3:"three"}
print(i)
print(type(i))
#none
j=None
print(j)
print(type(j))
#range
k=range(10)
print(k)
print(type(k))
#bytes
l=b"Hello"
print(l)
print(type(l))
#bytearray
m=bytearray(10)
print(m)
print(type(m))
#memoryview
n=memoryview(bytes(10))
print(n)
print(type(n))
#C.write a program to format the string and numbers
name="Raj"
age=20
print("My name is {} and age is {}".format(name,age))
#we cant combimne the string and number in this method
#print("my name is " + name + " and age is " + age)
#D.write a program to demonstrate the inbuilt math functions
import math
print(math.pi)
print(math.sqrt(25))
print(math.factorial(5))
print(math.pow(2,3))
print(math.floor(2.5))
#floor is used to round off the number to previous integer
print(math.ceil(2.5))
#ceil is used to round off the number to next integer
print(math.trunc(2.5))
#trunc is used to remove the decimal part
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.log(10))
#log is used to find the natural log
print(math.log10(10))
#log10 is used to find the log with base 10
print(math.log2(10))
#log2 is used to find the log with base 2
print(math.log(10,10))
#log with base 10
#E.write a program to compute the arthemetic operations through user input and display the result
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Addition of two numbers is: ", num1 + num2)
print("Subtraction of two numbers is: ", num1 - num2)
print("Multiplication of two numbers is: ", num1 * num2)
print("Division of two numbers is: ", num1 / num2)
print("Modulus of two numbers is: ", num1 % num2)
print("Exponent of two numbers is: ", num1 ** num2)
print("Floor division of two numbers is: ", num1 // num2)
#F.Write a program to translate mathematical formula into python expression.
#1. (a+b)^2
a=10
b=20
print((a+b)**2)
#2. (a-b)^2
a=10
b=20
print((a-b)**2)
#3. (a+b)^3
a=10
b=20
print((a+b)**3)
#4. (a-b)^3
a=10
b=20
print((a-b)**3)
#5. The area of circle
r=10
print(math.pi*r*r)
#6. The area of triangle
b=10
h=20
print(0.5*b*h)
#7. The area of rectangle
l=10
b=20
print(l*b)
#8. The perimeter of square
a=10
print(4*a)
#9. The perimeter of rectangle
l=10
b=20
print(2*(l+b))
#10. The perimeter of circle
r=10
print(2*math.pi*r)  
</pre>
</body>
</html>


