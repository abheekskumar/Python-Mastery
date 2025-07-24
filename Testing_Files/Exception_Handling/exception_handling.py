# exception handling in python
try:
    print(5/0)
    print("This should be printed as long as the interpreter doesn't run into an error before this line.")
except ZeroDivisionError:
    print("Don't devide by zero.")

else:
    print("This is printed as long as there is no exception thrown")
finally:
    print("This is always executed no matter what.")


print("This is just normal flow of control.")
import traceback
print(5/0)