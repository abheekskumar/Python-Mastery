"""
Iterations are used to run the same blocks of code multiple times.
There are 2 types of iterations:

for loop - used when the no. of times of iterations is known
while loop - used when the no. of times of iterations is unknown

for loop:
can be used to iterate through a string, list, tuple, and other data sequences
no need to initialize a iterable var

while loop:
you have to initialize a iterable var
you have to ensure that the conditions changes when you're in the loop, other wise you'll 
run into an inf loop

the jump statements:
break - The break statement is used to exit the corresponding loop
continue - The continue statements is used to move to the next iteration  in the corresponding loop

Other variations of the loops:
do-while:
The do while runs the code block atleast once and then checks the 
"while" loop condition. 
If it agrees, it continues, if it doesn't, it stops.

Other Remarks:

Both the loops have else clauses; the implementation is given down below
The else clause is only run on normal flow of control; If there's a break, the else-clause is skipped
"""


l1 = list(range(20))
x = 2
for i in l1:
    if i == x:
        print("Object found at",l1.index(i))
        break # if x found in 25, loop is exited unnaturally
else:
    print("Object not found") # if loop isn't existed naturally, else clause is skipped