"""
Towers of Hanoi:
3 Towers
"n" number of plates, each of different sizes.
The property the plates have is as follows: no plate can sit atop one smaller than itself.

The problem states is to give a set of instructions to the "priests" of Hanoi to move the disks from 
one tower to the other. 

Thinking about the problem in general:
think about move all but one disk to the spare, move the last disk to the desired tower. and then repeat 
this until all the disks are put onto the desired tower.
Base case: when you're at the last disk in the spare, put it onto the desired tower
Recursive case: move all but one disk to a spare tower; move the one disk to the desired tower, repeat

How to implement it one by one:
Move the top disk to the spare, move the 
"""
def print_move(frm,to):
    """
    to print out to console to move from one tower to the other
    """
    print("Move disk from "+str(frm)+" to "+str(to))

def towers(n,frm,to,spr):
    # Base case: when the spare only has one disk, move it into the desired position.
    # to- The desired stack
    # frm - The starting stack
    # spr - The spare stack
    if n == 1:
        print_move(frm,to) # prints instructions to move 1 disk from (frm var) to (to var)
    else:
        towers(n-1, frm, spr,to) # move all but one from starting(frm) to spare(spr)
        towers(1,frm,to,spr) # move the 1 from starting(frm) to desired(to) 
        towers(n-1,spr,to,frm) # move the rest from spare(spr) to desired(to)
    # Recursive case: Move all but one disk to the spare; Move 1 disk(the largest) to the desired tower


if __name__ == "__main__":
    towers(4,"Tower 1","Tower 2","Tower 3") # Tower 1 is Starting; Tower 2 is Desired, Tower 3 is Spare