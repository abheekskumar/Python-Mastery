"""
# Good Testing & Debugging Behavior
General:
    Break programs into modules
    Write Docstrings(Document Constraints for inputs...)
    Document the assumptions you made
    Use assertions on inputs.
    Create a set of inputs and expect classes.
    for each input, have the expected output verified from elsewhere(if possible)
    When encountering a bug, don't skip anything. 
    Use an intuition about where bugs might occur, document all of that. 

##Defensive Programming:
    Write specifications for functions/ code blocks
    Modularize program
    Check conditions on inputs/outputs(assertions)

## Testing:

Classes of testing:
    Unit Testing: test each function seperately
    Regression testing: catch reintroduced bugs and errors that were fixed previously
    Integration testing: test the overall program, check the interface between each module

Testing approaches:
    Intuition testing: based on the natural boundaries of the problem & the way the code is written
    Blackbox testing: explores paths through specification
    Glassbox testing: explores paths through code

Black box testing:
    designed without looking at the code.
    just based on documentations/expectations
    and based on inputs/outputs or natural places to look
    check boundaries, check extremes

Glass box testing:
    use the code directly to guide design of test cases
    called path complete if every potential path through code is tested atleast once
    you should still absolutely look at boundary conditions
    guidelines:
        branches
        for loop : look for each case of flow of control
        while loop : look for each case of flow of control

##BUGS:
    isolate the bugs
    retest until the code runs correctly
    check for more bugs introduced

Types of bugs:

Overt vs covert:
    Overt - obvious manifestation of bugs
    Covert - not obvious 

Persitent vs intermittent:
    Persistent - always exists
    Intermittent - harder to spot and get rid of, even with the same input(if it's based on web, time)

Categories of bugs:
    Overt & Persistent:
        Obvious to detect
        Defensive programming
    Overt & Intermittent:
        More frustrating, harder to detect, but if conditions are that prompt the bugs 
        can be identified and reproduced.
    Covert:
        Highly dangerous, as users may not realize answers are incorrect until a long 
        period of time.

Debugging:
    Use tools built in IDLE and anaconda
    python tutor
    print statements(to check flow of control)
    use your brain, be systematic in ways you debug
    use the info mentioned above
    Print:
        when you enter a function
        the inputs/parameters
        the results
        using the bisection method; once again to check flow of control

    Logic Errors:
        Think before writing new code
        draw pictures, take a break
        explain the code
        sketch out your logic
        you cannot "not know" what you were thinking
        be certain

    While debugging:
        ask how that bug occured
        try to test hypothesis where the bug is hit once again.
    
    Debugging as a search:
        treat it as a search problem, looking for an explanation for incorrect behavoir
        study available data, both correct and incorrect cases
        for hypothesis consistent with the data you have
        make test cases for hypothesis; test the hypothesis with a repeatable experiment
        repeat till you narrow down the options
        keep a record of all the experiments run, don't be redundant

        Binary Search: go through and test the flow of control in the program
        at the middle, then at the middle of each of those subsections and so on.

## Other remarks:
    make sure to have version control to have an idea of what the previous code was
    (when you're debugging a massive piece of program)
    ask 'why is the code doing what it is?', not 'why is the code doing not what I want?'
"""