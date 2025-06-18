def iter_for_gcd(a,b):
    l = []
    for i in range(1,min(a,b)+1):
        if a%i == 0 and b%i==0:
                l.append(i)
    return max(l)

def iter_while_gcd(a,b):
    l = []
    iter_list = list(range(1,min(a,b)+1))
    i = 0
    while i != len(iter_list):
        x = iter_list[i]
        if a%x == 0 and b%x == 0:
            l.append(x)
        i +=1
    return max(l)

def recur_gcd(a,b):
    #problem can be defined as taking hcf, continuous division based on remainder
    if b ==0:
         return a
    
    # recursive case
    return recur_gcd(b,a%b)


if __name__ == "__main__":
    #print((lambda x,y: print(x*y))(3,5))
    print(iter_for_gcd(9,12))
    print(iter_while_gcd(9,12))

    # recur implementation:
    print(recur_gcd(9,12))
