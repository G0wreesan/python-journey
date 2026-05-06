import sys,time


def zigzag(width):
    indent =0
    indent_increasing=True
    try:
        while True:
            print(' '*indent , end=' ' )
            time.sleep(0.1)
            print("*" * width)

            if indent_increasing:
                indent += 1
                if indent ==10:
                    indent_increasing = False #to change direction
            else:
                indent -= 1
                if indent ==0:
                    indent_increasing = True #to change direction
    except KeyboardInterrupt:
        sys.exit()

print("______________This is a Enter the width you want to see the zigzag pattern(<10)______________")
print("Press ctrl+c to stop the zigzag pattern at any point and exit the program")

width = int(input("Enter the width of the zigzag pattern: "))
if width < 10:
    zigzag(width)
else:
    print("Value exceeeded the limit, program considered as 10")
    zigzag(10)