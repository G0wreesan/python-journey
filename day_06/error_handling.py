#Exception handling 


try: 
    print("Enter a number: ")
    n = int(input())
    print("you entered ",n);
    
except : 
    print("Invalid input");


#let's call the same function again to see how it works


def getNum():
    global ink;
    ink=(input(" Enter a valid number : "))
    n=int(ink);
    return n;

def valid_num():
    try:
        num=getNum()
        print("You entered ",num)
    except: 
        tet=str(ink);

        print(" invalid input ? ",tet, " really ? now let's try that again" )
        print(" this time please ... .")

        valid_num()

valid_num();
print ("now the number you entered is : ",ink, "  is Valid son.");

try:
    n=int(input(" Enter a number : "))
    print(" you entered ",n );

except ValueError:
    print(" Invalid input , please enter a valid number .");

try:
    print(" Enter a number : ")
    n=int(input())

    print(" you entered ",n );
    print(" Result of 10 divided by ",n," is : ")
    result=10/n
    print(result);

except ZeroDivisionError:
    print(" Division by zero is not allowed .");





