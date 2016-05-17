# easy
# i learnt to ways to reverse a string
# slicing i.e string[::-1] = gnirts LOOOL
# by using ''.join(reversed(string)) TOO LONG


t = raw_input().strip()
for _ in xrange(0,int(t)):
    s = raw_input().strip()
    s_r = s[::-1]
    start = 1
    end = len(s)
    output = "Funny"
    while start < end:
        if abs(ord(s[start]) - ord(s[start - 1])) != abs(ord(s_r[start]) - ord(s_r[start - 1])):
            output =  "Not Funny"
            break
        start += 1
    print output
