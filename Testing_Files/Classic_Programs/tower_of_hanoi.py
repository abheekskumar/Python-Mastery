"""
Towers of Hanoi:
3 Towers
"n" number of plates, each of different sizes.
The property the plates have is as follows: no plate can sit atop one smaller than itself.

The problem states is to give a set of instructions to the "priests" of Hanoi to move the disks from 
one tower to the other. 
"""
def print_move(frm,to):
    """
    to print out to console to move from one tower to the other
    """
    print("Move disk from "+str(frm)+" to "+str(to))

def tower(n,):
    # How to think of this problem: 
    # Move 
    # base case: when it's the last tower(biggest), print out the command


    # recursive case: Otherwise, move  
