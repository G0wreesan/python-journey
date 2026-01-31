# Name error in python occurs when we try to use a variable or function that has not been defined yet.

# let's say Age variable is not defined and we are trying to print it.

age = input(" enter your human age : ")

if int(age) >= 0 and int(age) <=101:
    print(" your age is : ", Age) # Here Age is not defined, it should be age with small 'a'
else:
    print(" Invalid Age Entered ")

