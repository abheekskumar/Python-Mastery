
def most_occur(lyrics):
    x = lyrics.split()
    myDict = {}
    for i in x:
        if i in myDict:
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
print(biggest({'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], "d" :['donkey','dog','dingo']}))