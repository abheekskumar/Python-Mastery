x =1
def f(x):
    x = x+2
    print(x)

def f_global(y):
    global x
    x = x+y
    print(x)


if __name__ == "__main__":
    pass
    f_global(2)
