import random

s=int(input("enter the size of the tree"))
for i in range(s):
    print(" "*(s-i-1),end="")
    col=0
    for col in range(2*i+1):
        if random.randint(1,4)==1:
            print("O",end="")
        else:
            print("^",end="");

    print()
print(" "*(s-1),"#")
print(" "*(s-1),"#")

i=0
while i<s:
    print(" "*(S-i-1,end=""))
    col=0
    for col in range(2*i+1)
    