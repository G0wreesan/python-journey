"""
Tick Tock
The time.sleep() function, which pauses program execution for a specified amount of time, is useful, but rather plain. 
Let’s write our own tick_tock(seconds) function that also pauses for seconds amount of time 
but prints Tick... and Tock... each second while waiting.

For example, calling the function from the interactive shell should look like this 
(with a one-second pause after each line of output):

>>> tick_tock(4)
Tick...
Tock...
Tick...
Tock...
>>> tick_tock(3)
Tick...
Tock...
Tick...
"""

import time 

def tick_tock(seconds): 
    for i in range(seconds):
        if i % 2 == 0:
            print("Tick...")
        else:
            print("Tock...")
        time.sleep(1)

seconds = int(input("Enter the number of seconds to tick-tock: "))
tick_tock(seconds)  

print(" Tick Tock complete. ")