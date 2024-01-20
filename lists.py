#4.Lists
#list is a collection of items in a particular order and it is mutable
"""A. Write a program to create a list and perform the following operations:
i. + ii. * iii. Slicing iv. del"""
#i. +
a=[1,2,3,4,5]
b=[6,7,8,9,10]
print(a+b)
#ii. *
a=[1,2,3,4,5]
print(a*2)
#iii. Slicing
a=[1,2,3,4,5]
print(a[1:3])
#iv. del
a=[1,2,3,4,5]
del a[1]
print(a)
"""
list can take any data type as its element
"""
#B. Write a program to demonstrate the following list functions:
"""
1.len():returns the length of the list
2.max():returns the maximum element of the list
3.min():returns the minimum element of the list
4.list():converts a tuple into list
5.append():adds an element at the end of the list
6.insert():inserts an element at the specified position
7.remove():removes the specified element
8.pop():removes the element at the specified position
9.clear():removes all the elements from the list
10.index():returns the index of the specified element
11.count():returns the number of elements with the specified value
12.sort():sorts the list
13.reverse():reverses the list
14.copy():returns a copy of the list
15.extend():adds the elements of a list(or any iterable),to the end of the current list
16.sum():returns the sum of all elements in the list
17.all():returns true if all elements of the list are true
18.any():returns true if any element of the list is true
19.ascii():returns a readable version of any object
20.bool():returns the boolean value of the specified object
"""
a = [1,2,3,4,5]
print(len(a))
print(max(a))
print(min(a))
a.append(6)
print(a)
a.insert(2,7)
print(a)
a.remove(7)
print(a)
a.pop(2)
print(a)
a.clear()
print(a)
a = [66,89,2,3,4,5]
print(a.index(4))
print(a.count(4))
a.sort()
print(a)
a.reverse()
print(a)
b = a.copy()
print(b)    
c = [6,7,8,9,10]
a.extend(c)
print(a)
print(sum(a))
print(all(a))
print(any(a))
print(ascii(a))
print(bool(a))
#C.write a program to describe n*n matrix.
a=[]
n=int(input("Enter the value of n:"))
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(int(input("Enter the value of element:")))
print(a)    
#D.Write a program to print m*n matrix.
a=[]
m=int(input("Enter the value of m:"))
n=int(input("Enter the value of n:"))
for i in range(m):
    a.append([])
    for j in range(n):
        a[i].append(int(input("Enter the value of element:")))
print(a)
#E. Write a program to print even and odd numbers in a list.
a=[1,2,3,4,5,6,7,8,9,10]
b=[]
c=[]
for i in a:
    if i%2==0:
        b.append(i)
    else:
        c.append(i)
print(b)
print(c)
#Write a program to calculate the length of each element in a list using map function in python.
a=["apple","ball","cat","dog"]
b=list(map(len,a))
print(b)
#map function is used to apply a function to all the elements of a list



