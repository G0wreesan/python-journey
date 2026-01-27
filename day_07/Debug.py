# what if i press just enter insted of a string value in input 
name = str(input("Enter your name : "))
if name =='' : 
    raise Exception("Name cannot be empty. Please enter a valid name.")
else :
    print("Hello, " + name + "! Welcome to the program.")

num = int(input("Enter a number to divide 100 by: "))

if 100%num !=0 :
    raise Exception (" An error happened. This error message is vague and unhelpful. ")
else :
    print(" this number can divide 100 perfectly " , 100/num )

#  True or false: A raise statement must be inside a try block.
# False. A raise statement can be used outside of a try block to raise exceptions.

def get_name():
    print('Enter your name:')
    name = input()
    if name == '':
        raise Exception('You did not enter a name.')

    return name

try:
    name = get_name()
except:
    name = 'Guido'

print('Hello,', name)