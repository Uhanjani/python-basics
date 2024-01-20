#3.Functions and Strings
"""def function_name(parameters):
call the function
return [expression]"""
#A.write a function to find the multiplication of two numbers and demostrate the use of keyword arguments and parameters of function.
def mul(a,b):
    return a*b
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print(mul(a,b))
#B.Write a function QUAEQU (a,b,c,x) to find the roots of the quadratic equation ax^2+bx+c=0. Descriminant, sum and product of the roots.
def quaequ(a,b,c):
    print("The roots of the quadratic equation are: ",(-b+d**0.5)/(2*a),"and",(-b-d**0.5)/(2*a))
    print("The sum of the roots is: ",-b/a)
    print("The product of the roots is: ",c/a)
    print("The discriminant is: ",d)

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
d=(b*b)-(4*a*c) 
quaequ(a,b,c)
#c.Write a program to define a function using default arguments.
"""
default arguments are those arguments which are used to assign the default values to the parameters of the function.
"""
def default(a=10,b=20):
    return a+b
print(default())
#D.Write a program to create a string and use inbuild python functions for strings.
"""
1. len() : It is used to find the length of the string.
2. upper() : It is used to convert the string into upper case.
3. lower() : It is used to convert the string into lower case.  
4. title() : It is used to convert the string into title case.
5. capitalize() : It is used to convert the first character of the string into upper case.
6. swapcase() : It is used to convert the string into opposite case.
7. count() : It is used to count the number of occurences of the character in the string.
8. find() : It is used to find the index of the character in the string.
9. replace() : It is used to replace the character in the string.
10. split() : It is used to split the string.
11. join() : It is used to join the string.
12. strip() : It is used to remove the white spaces from the string.
13. lstrip() : It is used to remove the white spaces from the left side of the string.
14. rstrip() : It is used to remove the white spaces from the right side of the string.
15. isalpha() : It is used to check whether the string is alphabetic or not.
16. isdigit() : It is used to check whether the string is digit or not.
17. isalnum() : It is used to check whether the string is alphanumeric or not.
18. isspace() : It is used to check whether the string is space or not.
19. istitle() : It is used to check whether the string is title or not.
20. isupper() : It is used to check whether the string is upper case or not.
21. islower() : It is used to check whether the string is lower case or not.
22. startswith() : It is used to check whether the string is starting with the given character or not.
23. endswith() : It is used to check whether the string is ending with the given character or not.
24. center() : It is used to center the string.
28. format() : It is used to format the string.
29. isidentifier() : It is used to check whether the string is identifier or not.
30. isprintable() : It is used to check whether the string is printable or not.
31. splitlines() : It is used to split the string into lines.   
32. index() : It is used to find the index of the character in the string.
"""
string="Hello World"
print(len(string))
print(string.upper())
print(string.lower())
print(string.title())
print(string.capitalize())
print(string.swapcase())
print(string.count("l"))
print(string.find("l"))
print(string.replace("l","L"))
print(string.split(" "))
print(" ".join(string))
print(string.strip())
print(string.lstrip())
print(string.rstrip())
print(string.isalpha())
print(string.isdigit())
print(string.isalnum())
print(string.isspace())
print(string.istitle())
print(string.isupper())
print(string.islower())
print(string.startswith("H"))
print(string.endswith("d"))
print(string.center(20))
print(string.format())
print(string.isidentifier())
print(string.isprintable())
print(string.splitlines())
print(string.index("l"))
#E.Write a program to to access characters in a string through index operator.
string="Hello World"
print(string[0])
print(string[1])
print(string[2])
print(string[3])
print(string[4])
print(string[5])
print(string[6])
print(string[7])
print(string[8])
print(string[9])
print(string[10])
#negative indexing in string is also possible in python which means that the string can be accessed from the last character of the string as -1 .
print(string[-1])
print(string[-2])
print(string[-3])
print(string[-4])
print(string[-5])
print(string[-6])
print(string[-7])
print(string[-8])
print(string[-9])
print(string[-10])
print(string[-11])
#F.Write a program to traverse all the elements of string using for loop and check if two strings are anargms or not.
string1="Hello World"
len = len(string1)
for i in range (1, len+1):
    print(string1[len-i], end=" ")
#G.Write a program that takes a sentence as an input parameter and displays the number of words init.
string="welcome to python programming language"
print(string.split(" "))
my_list = string.split(" ")
for item in my_list:
    print(item, end=" ")








