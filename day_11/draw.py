import sys, time

def draw_stripe(height):
   for i in range(1, height + 1):
        print('- ' * (i * i))
        time.sleep(0.5)  
   for i in range(height - 1, 0, -1):
        print('- ' * (i * i))
        time.sleep(0.5)  

height = int(input("Enter the height of the stripe: "))

draw_stripe(height)


        