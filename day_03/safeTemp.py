"""
The following program reports whether a given temperature is safe. 
It asks the user to enter a temperature in two parts. First, they should enter C or F to indicate the Celsius or Fahrenheit scale; second, they should enter the number of degrees. 
If the temperature is between 16 and 38 degrees Celsius (inclusive of 16 and 38) or between 60.8 and 100.4 degrees Fahrenheit (inclusive of 60.8 and 100.4), 
the program prints Safe. 
Outside of these temperature ranges, the program prints Dangerous.

This program has bugs, however. Rewrite the code to fix the errors. 
You may assume the user always enters valid inputs and not, say, X for the scale or hello for the number of degrees.
"""

scale = input("Enter C or F to indicate celcius or farenheit scale [C/F]: ")
temperature = float(input("Enter the temperature: "))

if scale == 'C' or scale == 'c':
    if temperature>=16 and temperature<=38:
        print("Safe")
    else:
        print("Dangerous");
elif scale == 'F' or scale == 'f':
    if temperature>=60.8 and temperature<=100.4:
        print("Safe")
    else:
        print("Dangerous");
else :
    print("Invalid scale entered.");

print("-------------------Single Line Conditional Statement-------------------");

#single line conditional statement

if (scale=='C' or scale=='c') and (temperature>=16 and temperature<=38) or (scale=='F' or scale=='f') and (temperature>=60.8 and temperature<=100.4):
    print("Safe");
else:
    print("Dangerous");


