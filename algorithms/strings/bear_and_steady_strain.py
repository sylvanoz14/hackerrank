from collections import defaultdict
"""
def smallest(s1, s2):
    assert s2 != ''
    d = defaultdict(int)
    nneg = [0]  # number of negative entries in d
    def incr(c):
        d[c] += 1
        if d[c] == 0:
            nneg[0] -= 1
    def decr(c):
        if d[c] == 0:
            nneg[0] += 1
        d[c] -= 1
    for c in s2:
        decr(c)
    minlen = len(s1) + 1
    j = 0
    for i in xrange(len(s1)):
        while nneg[0] > 0:
            if j >= len(s1):
                return minlen
            incr(s1[j])
            j += 1
        minlen = min(minlen, j - i)
        decr(s1[i])
    return minlen

print smallest('AAGTGCCT', 'CAT')

#hints https://mydevelopedworld.wordpress.com/2012/12/12/solution-for-minimum-window-in-string-in-on/
#http://stackoverflow.com/questions/2459653/how-to-find-smallest-substring-which-contains-all-characters-from-a-given-string
"""
def walk(s, tosubstractchars,matchSub):
    startIndex = matchSub['start']
    endIndex = matchSub['end']
    ccount = {k:v for k,v in matchSub['ccount'].items()}
    if endIndex >= len(s) - 1:
        return False
    startc = s[startIndex]

    i = startIndex
    while True:
        if tosubstractchars.get(s[i]):
           startIndex = i
           break
        if i > endIndex:
            return False
        i += 1

    i = endIndex + 1
    while True:
        if tosubstractchars.get(s[i]):
            ccount[s[i]] += 1
        if s[i] == startc:
            endIndex = i
            break
        if i >= s_len - 1:
            return False
        i += 1
    i = startIndex
    while True:
        if tosubstractchars.get(s[i]):
            if tosubstractchars[s[i]] < ccount[s[i]]:
                ccount[s[i]] -= 1
            else:
                startIndex = i
                break
        if i >= endIndex:
            break
        i += 1
    matchSub['start'] = startIndex
    matchSub['end'] = endIndex
    matchSub['ccount'] = ccount
    return matchSub

def first(s, tosubstractchars):
    ccount={
        "A":0,
        "T":0,
        "C":0,
        "G":0
    }
    startIndex = 0
    endIndex = 0
    for i in range(len(s)):
        if tosubstractchars.get(s[i]):
            ccount[s[i]] += 1
        if len(filter(lambda x : x < 0, [ccount[k] - v for k, v in tosubstractchars.items()])) == 0:
               endIndex = i
               break
    for i in range(startIndex, endIndex):
        if tosubstractchars.get(s[i]):
            if tosubstractchars[s[i]] < ccount[s[i]]:
                ccount[s[i]] -= 1
            else:
                startIndex = i
                break
    return {
        "start": startIndex,
        "end":endIndex,
        "ccount": ccount
    }


n = int(raw_input().strip())
s = raw_input().strip()
total = {
    "A" : 0,
    "T" : 0,
    "C" : 0,
    "G" : 0
}
for c in s:
    total[c] += 1
s_len = len(s)
tosubstractchars = {}
for k, v in total.items():
    if v > s_len / 4:
        tosubstractchars.update({k: v - s_len / 4})
minresult = sum([v for k,v in tosubstractchars.items()])
if len(tosubstractchars) <= 0:
    print 0
else:
    ms = first(s, tosubstractchars)
    result = ms['end'] - ms['start'] + 1
    while True:
        nextms = walk(s, tosubstractchars, ms)
        if not nextms:
            break
        else:
            ms = nextms
            if ms['end'] - ms['start'] + 1 < result:
                result = ms['end'] - ms['start'] + 1
        if result <= minresult:
            break
    print result

