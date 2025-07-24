
def most_occur(lyrics):
    x = lyrics.split()
    myDict = {}
    for i in x:
        if i in myDict: # replace if-else clause with for  myDict[i] = myDict.get(i,0) +1
            myDict[i] +=1
        else: 
            myDict[i] = 1
    return myDict


def biggest(myDict):
    results = []
    for key in myDict.keys():
        results.append(len(myDict[key]))
    best = max(results)
    print(best)
    vals = myDict.values()
    best = max(vals,key=len)
    print(best)
    ans = []
    for i in myDict.keys():
        if best == myDict[i]:
            ans.append(key)
    if len(ans) != 0:
        return ans[0]
    else:
        return None
    
def biggestV2(myDict):
    """ Prints the key(letter) which has the largest list of words."""
    maxKey = 0
    maxVal = 0
    maxValLen = 0
    found = False
    
    for k,v in myDict.items():
        if len(v) > maxValLen:
            found = True
            maxVal = v
            maxValLen = len(v)
            maxKey = k
    if found:
        print(maxValLen)
        print(maxVal)
        print(maxKey)
    else:
        print(None)



print(biggest({'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], "d" :['donkey','dog','dingo']}))
biggestV2({'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], "d" :['donkey','dog','dingo']})