def firstTowersOfHanoi(n,t,s1,s2):
    # problem
    # 
    # base case: n=64(the largest), move to target
    if len(s1) ==0 and len(s2) ==0: # base case, both the spare towers have to be empty
        return t
    else: # recursive case
        if len(s1) > len(s2):
            s2.extend(s1[0:n-1])
            return firstTowersOfHanoi(n,t,s1,s2)
        else: 
            s1.extend(s2[0:n-1])
            return firstTowersOfHanoi(n,t,s1,s2)

def secondTowerOfHanoi():
    def printMove(fr,to):
        print("Move from "+ str(fr) + " to " + str(to))
    def Towers(n,fr,to,spare):
        if n==1:
            printMove(fr,to)
        else:
            Towers(n-1,fr,spare,to)
            Towers(1,fr,to,spare)
            Towers(n-1,spare,to,fr)
    
    print(Towers(4,"P1","P2","P3"))


if __name__ == "__main__":
    secondTowerOfHanoi()