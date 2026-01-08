#this is a comment 
# we use loops to print shapes here 

height=5
width=input("enter the width of the rectangle : ")


for i in range(height):

    print('O'*int(width));

print("this is a rectangle with height = ",height," width = ",width)

height=int(input("enter the height of the triangle : "))
for i in range(1,height+1):

    print('O'*i);
print("this is a triangle with height = ",height)

height=int(input("enter the height of the rectangle : "))
width=int(input("enter the width of the rectangle : "))
for i in range(height):

    print('O'*width);   

print("this is a rectangle with height = ",height," width = ",width)
