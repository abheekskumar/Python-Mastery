# control flow statements

if 5>6: # conditional statement
    print("This is a test.")
elif 5<6:
    print("This will print.")
else:
    print("what the test.")

for i in range(5,7): # iterarive statement used for a know number of iterations
    print(i)
    if i == 6:    
        continue
else:
    print("This should be printed after all the iterative statements")

while True: # conditional iterative. Used for an unknown number of iterations.
    for i in range(1,100):
        if i != 50:
            print(i)
            continue
        else:
            print("Halfway there.")
            

    print("This is an infinite loop")
    break


