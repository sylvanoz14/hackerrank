# lessons learned
# before diving into a solution, check aound to see if
#someone has tried to solve this problem and how they went about
#solving it. i saved about 2 hours by just reading the form for about 15 mins
#this problem can be solved similarly to 15 square problem
#https://www.youtube.com/watch?v=TKXiHdgOHaU


t = int(raw_input().strip())

for x in range(t):
    n = int(raw_input().strip())
    lists = map(int, raw_input().split()) #list(raw_input().strip().split(' '))
    check = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if lists[i] > lists[j]:
                check += 1

    print "YES" if check % 2 == 0 else "NO"
