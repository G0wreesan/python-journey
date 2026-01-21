#learning functions in python 
def say_hello():
    for i in range(3):
        print("Hello User")

say_hello()
say_hello() 


def say_hello(name):
    print("Hello ",name)




say_hello("Alice");

def get_greet():
    print("What is your name? ")
    name= input()
    return "Hello "+name
print(get_greet())



def enter_passord(passord):
    if passord=="sordfish":
        return True
    else:
        return False
    
passord=input("Enter the passord:")
if enter_passord(passord):
    print("Access Granted"*4 )
else:
    print("Access Denied")
# Here the password paramaeter data type can be any type but to work properly it should be string



def get_greeting():
    print('What is your name?')
    name = input()
    return 'Hello, ' + name
# this function returns a greeting string


"""
The Call Stack
The call stack is how Python remembers where to return the execution after each function call. 
The call stack isn’t stored in a variable in your program; rather, it’s a section of your computer’s memory that 
Python handles automatically behind the scenes. When your program calls a function, 
Python creates a frame object on the top of the call stack.

Frame objects store the line number of the original function call so that Python can remember where to return. 
Answer the following questions about the frame objects, the call stack, and function calls.
"""


"""
24. What does a stack frame object represent?

A stack frame object represents a single function call in the call stack, 
containing information about the function's execution context, such as local variables, 
the instruction pointer, and the return address.

25. When is a stack frame object pushed to the top of the call stack?

A stack frame object is pushed to the top of the call stack when a function is called.

26. When is a stack frame object popped off the top of the call stack?

A stack frame object is popped off the top of the call stack when a function returns,
completing its execution.

27. What does the stack frame object at the top of the call stack represent?
The stack frame object at the top of the call stack represents the currently executing function.


28. A call to a function named spam() is made. 
Then, a call to an eggs() function is made. Next, eggs() returns. 
After that, a call to a bacon() function is made. 

What does the call stack look like at this point?
At this point, the call stack would look like this (from bottom to top):
- spam()  (bottom of the stack)
- bacon()  (top of the stack)


29. A program has absolutely no function calls in it. What does the call stack look like while the program runs?

At this point, the call stack would be empty, as there are no function calls to create stack frames.
"""

"""
Local and Global Scopes
Only code within a called function can access the parameters and variables assigned in that function. 
These variables are said to exist in that function’s local scope. 
By contrast, code anywhere in a program can access variables that are assigned outside all functions. 
These variables are said to exist in the global scope. 

30. Are function parameters global variables or local variables?
Function parameters are local variables.

31. A variable in a function is marked with the global statement. Is it a global or local variable?
It is a global variable.

32. Can a variable be both global and local?
No, a variable cannot be both global and local at the same time.

33. If a global spam variable exists, and a function has a spam = 42 assignment statement and no global spam statement, 
is the spam variable in the function local or global?


34. If a global spam variable exists, and a function has a spam = 42 assignment statement as well as a global spam statement,
    is the spam variable in the function local or global?

 global

35. If a global spam variable exists, and a function never assigns spam a value and has no global spam statement,
    the function uses the spam variable (such as in print(spam)). Is the spam variable in the function local or global?
    global

"""

def func(eggs):
    print(spam);

spam='Dog'
func('Cat')

def func():
    spam = 'cat'
spam = 'dog'
func()
print(spam)

#func() only initiates a new local variable called spam and assigns it the value 'cat'
# but the global variable spam remains unchanged as 'dog'
# here  after func called we print spam is 'dog' because the spam is local to func and when we print spam outside func it prints global spam 'dog'

def func():
    global spam
    spam = 'cat'
spam = 'dog'
func()
print(spam)

# here even though global spam is set to dog initially after func() where it set Global spam variable to 'cat'

def func():
    global spam
    print(spam)
    spam = 'cat'
spam = 'dog'
func()
# in func() the global spam variable is passsed in to function 

