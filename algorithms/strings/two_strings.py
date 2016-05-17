t = raw_input().strip()

for _ in xrange(0,int(t)):
    s_1 = raw_input().strip()
    s_2 = raw_input().strip()
    output = "NO"
    counted = [] #optimized it with this line so it can pass the 4th and 5th test
    for s in s_1:
        if s not in counted:
            counted.append(s)
            if s in s_2:
                output = "YES"
                break
    print output
