import math
def polysum(n,s):

    return round((((0.25*n*(s**2))/(math.tan((math.pi)/(n))))+((n*s)**2)),4)

if __name__ == "__main__":
    print(polysum(5,2))