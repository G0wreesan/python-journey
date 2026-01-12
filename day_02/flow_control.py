10.653>7
age=int(input("Enter YOur Age "))
if age<18:
    print("You are a minor")
elif age>=18 and age<65:
    print("You are an adult")
else:
    print("You are a senior citizen")
# Flow control statements: if, elif, else

if 2+2>4 or True:
    print("True")
else:
    print("False");

if 2+2>=4 and True:
    print("True")
else:
    print("False");  

if True and (True or False):
    print("True")
else:
    print("False");
is_raining=True
C=input("Is it raining today? [Y/N] ")

if C=='Y' or C=='y':
    is_raining=True
    print("You can go out without umbrella")
else:
    is_raining=False
    print("Take an umbrella with you");
if is_raining:
 for i in range(1,11):
    print(i,"."," "*i,"It's raining, take an umbrella with you")
else:
    for i in range(1,11):
        print(i,"."),print()*i,print("It's not raining, you can go out freely");

print(10>5)

password = 'swordfish'
if password == 'rosebud':
    print('Access granted.')
elif password == 'swordfish':
    print('That is the old password.')

else:
    print('Access denied.');

