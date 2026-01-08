

name="Fury"
print(name)
print("type of  name variable is "+ str(type(name)))
age=22
print("age of "+name+ " is "+ str(age))
print("the type of this age "+str(type(age)))

height=167.5
print(str(height)+" cm")
print("type of height variable is "+str(type(height)))

print("for printing the type of variable we use type() function")
print("but to merge it with a string we need to convedr the object(type) to String using str() function")
print()
print("but we can simply use comma(,) to merge different types")

print("name is ", name , " and its type is ", type (name) )
print ("age is ", age, " and age variable type is ", type (age ) )
print ("his height is ", height, " cm and height variable type is ", type(height) )
print()

print("This is how we declare variables in python")
print("let's try to use mathematics to manipulate varibale ")
a=10
b=5
print("a is " , a , " b is ",b)
sum1=a+b
print("sum of ",a," + ",b," is ",sum1)
diff=a-b
print("difference of ",a," - ",b," is ",diff)
prod=a*b
print("product of ",a," * ",b," is ",prod)
quotient=a/b
print("quotient of ",a," / ",b," is ",quotient)
exp=a**b
print("exponent of ",a," ** ",b," is ",exp)
mod=a%b
print("modulus of ",a," % ",b," is ",mod)
mod=b%a
print("modulus of ",b," % ",a," is ",mod)
floordiv=a//b
print("floor division of ",a," // ",b," is ",floordiv)
floordiv=b//a
print("floor division of ",b," // ",a," is ",floordiv)

print()
print(" we can also use range function + sum function to sum up the series of numbers ")
sum2 =sum(range(1,11))
print("sum of first 10 natural numbers is ",sum2)

nephew='yashwanth'
Nephew='thesmith'
print(nephew)
_4="meaning of life"
print(_4)

print("|||||||||||||||||||")
print("python has default names that can not be used as variable names ")
print("these are called keywords or reserved words")
import keyword
print(keyword.kwlist)
print() ,print("|||||||||||||||||||||")


int('42')
str(3.0)
R=round(4.9)
print("round 4.9 is ",R)
print(),print("what the abs() function returns ? ")
print(" returns the absolute value of the number  ")
R=abs(-8.4623)
print("R is -",R,"but in abs() = ",R)
print("1 Byte has ",2**3 , "bits")
decimalValue=8
binaryValue=bin(decimalValue)
print("binary value of decimal ",decimalValue," is ",binaryValue)
