p = int(raw_input().strip())
q = int(raw_input().strip())


def kaprekar(n):
    if n == 1:
        return True
    if n * n < 15:
        return False
    l = str(n * n)
    length = len(l)
    return n == int(l[0:length/2]) + int(l[length/2:])
hold = []
for i in range(p,q+1):
    if kaprekar(i):
        hold.append(i)


if len(hold) == 0:
    print "INVALID RANGE"
if len(hold) != 0:
    for x in hold:
        print x,
