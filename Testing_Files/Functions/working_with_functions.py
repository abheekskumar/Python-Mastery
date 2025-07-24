"""
# Scope of a var in functions:

1) Global Scope:
    Life time is program runtime
    defined in __main__
2) Local Scope
    Lifetime is function runtime
    defined in a function
#Name Resolution
LEGB:
- Local namespace:

- Enclosing namespace:
    if in nested loops, this refers to the scope above the local namespace, but before the 
    global namespace
- Global namespace:

- Built-in namespace



Using the "global" statement in a function allows the flow of control
to access the global namespace for that particular variable.
"""