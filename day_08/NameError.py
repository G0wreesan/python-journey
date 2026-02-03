# Name error in python occurs when we try to use a variable or function that has not been defined yet.

# let's say Age variable is not defined and we are trying to print it.

 


try :
    age = input(" enter your human age : "); 
    print(" your age is : ", Age);
except NameError as e:
    print(" NameError occurred : ", e);
    print(" please make sure the variable is defined before using it .");


# To fix the error, we need to use the correct variable name 'age' instead of 'Age'.
# this here is the NameError example.
