#bad int is like invalid literal for int() with base 10: 'abc' , even a valid number with spaces will also cause this error like '  123  ' , so we need to strip the spaces before converting to int. , also fractions 
def func():
    try:
        n=int(input(" Enter a number : ").strip())
        print(" you entered ",n );
    
    except ValueError:
        print(" Invalid input , please enter a valid number .")
        func();

func();