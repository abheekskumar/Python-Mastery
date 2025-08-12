"""
Using memoization, write fibonacci recursive code, with the dictionary being empty: handle
base cases in the function itself.
"""
import json
import traceback
import sys
sys.setrecursionlimit(10000)


def fib(n:int,d:dict) -> int:
    """Recursive fib with memo."""
    if str(n) in d: # checking if number in memo/hash
        return d[str(n)]
    
    # global counter implementation
    global fibCount 
    fibCount +=1
    ans = fib(n-1,d) + fib(n-2,d)
    d[str(n)] = ans
    return ans



try:
    with open("_files/memo_fib.json","r") as fh: # auto closes
        d = json.loads(fh.read())
except Exception as e:
    print(f"{e}")
    print("Opening/Reading Error.")
    print(traceback.format_exc())
    d = {0:1,1:1}

# print(d)

fibCount = 0
print(fib(float(input("Enter a number for it's fib:")),d))
print(f"Hash fib ran {fibCount} times.")


fibCount = 0
print(fib(float(input("Enter a number for it's fib:")),d)) # uses the same dictionary defined above.
print(f"Hash fib ran {fibCount} times.")


# save the dict
try:
    with open("_files/memo_fib.json","w") as fh:
        fh.write((json.dumps(d)))
except Exception as e:
    print(f"{e}")
    print("Closing/Writing Error.")
    print(traceback.format_exc)

