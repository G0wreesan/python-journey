  # NameError: name 'true' is not defined. Did you mean: 'True'?

def func():
    if true: # change this to ''True'' to fix the error
        print(" This is true .")
    else:
        print(" This is false .")


def Func():
    if True: # this returns no error because True is a boolean value in python and it is case sensitive
        print(" This is True .")
    else:
        print(" This is False .")

try : 
    func()
except : 
    print(" NameError: name 'true' is not defined. Did you mean: 'True'?")
    Func()

