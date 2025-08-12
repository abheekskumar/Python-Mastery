import pdb

"""
pdb- python debugger
in terminal running python -m pdb [file_name].py allows us to run the debugger from the first line
of the program


some debugger commmands:
c - continue
b lineno.- breakpoint at line number
q - quit
n - next line(passing over functions)
s - move into a function

With python 3.7, you can also add breakpoints with breakpoint()
"""
print(2)
breakpoint() # also adds a breakpoint
pdb.set_trace() # adds a breakpoint

print(5)