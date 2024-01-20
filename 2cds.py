#2.Decision and control statements
#A.Write a program to check whether the given number is even or odd
a=int(input("Enter the number: "))
if(a%2==0):
    print("The number is even")
else:
    print("The number is odd")
#B.write a program to find the largest among the given numbers.
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if(a>b and a>c):
    print("The largest number is: ",a)
elif(b>a and b>c):
    print("The largest number is: ",b)
else:
    print("The largest number is: ",c)
#C.Write a program to print the sum of all the even numbers in between two numbers.
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
sum=0
for i in range(a,b+1):
    if(i%2==0):
        sum=sum+i
print("The sum of all the even numbers is: ",sum)
#D.Write a program to print the sum of all the odd numbers in between two numbers.  
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
sum=0
for i in range(a,b+1):
    if(i%2!=0):
        sum=sum+i
print("The sum of all the odd numbers is: ",sum)
#E.write a program to determine whether the given number is prime or not.
a=int(input("Enter the number: "))
for i in range(2,a):
    if(a%i==0):
        print("The number is not prime")
        break;
else:
    print("The number is prime")#F.write a program to print the prime numbers in between two numbers.
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
for i in range(a,b+1):
    for j in range(2,i):
        if(i%j==0):
            break;
    else:
        print(i, end=" ")
#write a program to display all the prime numbers upto n
n=int(input("Enter the number: "))
for i in range(2,n+1):
    for j in range(2,i):
        if(i%j==0):
            break;
    else:
        print(i, end=" ")
#write a program to print Patterns
"""
*
**
***
****
*****
"""
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end="")
    print()
""" 
*****
****
***
**
*
"""
n=int(input("Enter the number: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*", end="")
    print()
""" 
    *
   **
  ***
 ****
*****
"""
n=int(input("Enter the number: "))      
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j<=n-i):
            print(" ", end="")
        else:
            print("*", end="")
    print()
"""
*****
 ****
  ***
   **
    *
"""
n=int(input("Enter the number: "))
for i in range(n,0,-1):
    for j in range(1,n+1):
        if(j<=n-i):
            print(" ", end="")
        else:
            print("*", end="")
    print()
"""
     *
    * *
   * * *
  * * * *
"""
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j<=n-i):
            print(" ", end="")
        else:
            print("*", end=" ")
    print()
"""
*****
*   *
*   *
*   *
*****
"""
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==1 or i==n or j==1 or j==n):
            print("*", end="")
        else:
            print(" ", end="")
    print()
#Write a program to print the nth multiplication table.
n=int(input("Enter the number: "))
m=int(input("Enter the number: "))
for i in range(1,m+1):
    print(n,"*",i,"=",n*i)






    




