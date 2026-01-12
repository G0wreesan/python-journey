import random ,sys

"""
52. What does the sys.exit() function do?
        controls the termination of a program . 
        you can terminate the program before it reaches the end of the code 

53. What instruction must your program run before you can call the sys.exit() function?
    import sys 
    it's important to import sys module at the beginning of your program
    
"""

s = int(input("enter the size of the tree"))

for i in range(s):
    print(" "*(s-i-1),"^"*(2*i+1))

print(" "*(s-1),"|")
print(" "*(s-1),"|")
print(" "*(s-3),"---Tree---")

