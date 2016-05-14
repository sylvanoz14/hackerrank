# ----> straight forward
import string

t = raw_input().strip()

for _ in xrange(0,int(t)):
    s = raw_input().strip()
    l_case = list(string.ascii_lowercase) # a list of all alphabets
    remaining = len(s)
    min_count = 0
    start = 0

    while remaining > 1:
        #tk left and right side of string
        left = s[start]
        right = s[-(start + 1)]
        # index of the max in l_case - index of the min
        add  = abs(l_case.index(right) - l_case.index(left))
        min_count += add
        remaining -= 2
        start += 1
    print min_count
