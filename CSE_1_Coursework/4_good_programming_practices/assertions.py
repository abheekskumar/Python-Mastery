"""
Assertions - used to enforce the assumptions on state of computation are as expected.
use an assert statement to raise AssertionError exception if assumptions are not met
it's an example of good defensive programming


Assertions are just used to halt the execution of a program.
They don't allow the programmer to control response to unexpected conditions
Typically used to check inputs to function procedures, but can be used elsewhere too
Can be used to check outuputs of a function to avoid propogating bad values
can make it easier to locate a source of a bug


Where to use assertions:

Goal is to spot bugs as soon as introduced and make clear where they happened.
use as a supplement to testing
raise exceptions if users supplies bad data input

Use assertions to:
    check types of arguments or values
    check that invariants on data structures are met
    check constraints on return values
    check for violations of constraints on procedure(eg no duplicates in list)
"""

def main1():
    def avg(grades):
        assert len(grades) != 0, "no grades data"  # assert <condition> , <statement>; 
        #assert checks the condition and moves on if true, stops if false
        # this raises an AssertionError
        return sum(grades)/len(grades)


if __name__ == "__main__":
    main1()