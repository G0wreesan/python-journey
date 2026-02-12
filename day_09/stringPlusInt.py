  
        #  TypeError: can only concatenate str (not "int") to str

def func():
    name = "John"
    age = 30.0
    print(" My name is " + name + " and I am " + str(age) + " years old .")
    # when you put ("  My name is " + name + " and I am " + age + " years old ")
    # here age without converting to string will cause the error because we cannot concatenate a string with an integer directly , we need to convert the integer to string using str() function before concatenating it with other strings.
func();