"""spam = ['cat', 'dog', 'moose']
for i in spam:
    print(i)
    
    this prints each element in the list spam on a new line
"""

"""
spam = ['cat', 'dog', 'moose']
for i in range(len(spam)):
    print(i)
this here prints the index of each element like 0 , 1 , 2 
    because range(len(spam)) generates a sequence of numbers from 0 to the length of the list minus one,
    which corresponds to the indices of the list elements.
    
"""

"""spam = ['cat', 'dog', 'moose']
for i in range(len(spam)):
    print(spam[i])
Because we use the Print with spame[i] which prints the elements cuz i goes from 0-2 in range(len(spam))
"""
""""
spam = 100
for i in range(5):
    
    spam += 1
print(spam)
 this will print 105
"""
"""
21. spam = spam * 2 || spam*=2

22. bacon = bacon - 3 || bacon -=3

23. eggs = eggs + bacon * 5 || eggs += bacon * 5

24. eggs = eggs * bacon + 5 || eggs *= bacon + 5

25. spam = spam + 'LastName' || spam += 'LastName'
"""

"""
sort() is method

len() is function

append() is method

index() is method

print() is function

input() is function

reverse() is method

33.Both the remove() list method and the del operator can remove items from a list value.
 How do they work differently?
    here the remove is a 'method' that removes the first occurence of the specified value
    but the del operator 'function' removes an item specified by in dex in that list
    
34.If the spam variable contains a list, running sort(spam) causes an error message. Why?
    sort is a method not a function so it must be called correctly as 'object.sort()'
    so the correct term would be 'spam.sort()'
    
35.If the spam variable contains a list, 
    what code would rearrange the items in spam in “ASCIIbetical” order?
    spam.sort() would rearrange in ASCIIbetical order

36.What code could we run so that spam's contents are sorted in alphabetical order?
    spam.sort() would sort in alphabetical order as well

37.>>> spam = ['cat', 'dog', 'moose']
>>> spam.sort()
>>> print(spam)
['cat', 'dog', 'moose']
    The sort() method sorts the list in place, meaning it modifies the original list.

38.>>> spam = ['cat', 'dog', 'moose']
>>> spam.sort(reverse=True)
>>> print(spam)
['moose', 'dog', 'cat']
    The sort() method with the reverse=True argument sorts the list in reverse order, 

39.>>> spam = [3, 99, 86, 42]
>>> spam.reverse()
>>> print(spam)
[42,86,99,3] --> HERE THE REVERSE method only reverses the order of the list not sort them in 
                 decending order


"""

numbers = [10 ,20 , 30 , 40 , 50 ]
print(numbers)
numbers.remove(20)
print(numbers)

del numbers[2]
print(numbers)

"""
True and print("Hello") --> this will print Hello because the print function is executed first and 
then the True is evaluated but it does not affect the output of the print function.
"""

False and print("Hello") 
"""--> this will not print anything because the False value short-circuits the expression, 
meaning that the print function is not executed at all.
"""
True or print("Hello")
"""--> this will not print anything because the True value short-circuits the expression,"""
False or print("Hello")
"""--> this will print Hello because the False value does not short-circuit the expression,"""

print("Hello") and True
""" this returns hello because print executed first then True is evaluated"""

print("hello 2")and False
"""this will print hello too cuz print evaluted even before the false identifiied"""

print("hello 3") or True
""" this will print hello because the print function executed first and then True is evaluated"""

