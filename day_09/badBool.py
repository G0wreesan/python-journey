  # NameError: name 'true' is not defined. Did you mean: 'True'?

def func():
    if true:
        print(" This is true .")
    else:
        print(" This is false .")


def Func():
    if True:
        print(" This is True .")
    else:
        print(" This is False .")

try : 
    func()
except : 
    print(" NameError: name 'true' is not defined. Did you mean: 'True'?")
    Func()

