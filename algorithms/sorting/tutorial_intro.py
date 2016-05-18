v = raw_input().strip()
n = raw_input().strip()
ar = list(raw_input().strip().split(' '))

if v in ar:
    print ar.index(v)
