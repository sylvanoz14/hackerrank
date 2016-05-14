# pretty straight forward
t = raw_input().strip()

for _ in xrange(0,int(t)):
    s = raw_input().strip()
    count = 0
    start = 0
    while start < (len(s)-1):
        if s[start] == s[start +1]:
            count +=1
        start += 1
    print count
