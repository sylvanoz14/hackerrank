def solution(lst):
    if lst == sorted(lst):
        return "yes"
    for i in xrange(n - 1):
        if lst[i] > lst[i + 1]:
            min_ = min(lst[i + 1:])
            index = lst.index(min_)
            lst[i], lst[index] = lst[index], lst[i]
            if lst == sorted(lst):
                print "yes"
                return "swap %s %s" % (i + 1, index + 1)
            # return the list to its originaal state
            lst[i], lst[index] = lst[index], lst[i]

            if index - i > 1:
                # invert the middle part and check
                if (lst[:i] + (lst[i:index + 1][:: - 1])+ lst[index + 1:]) == sorted(lst):
                    print "yes"
                    return "reverse % s % s" % (i + 1, index + 1)
            return "no"

n = int(raw_input().strip())
lst = map(int, list(raw_input().strip().split(' ')))
print solution(lst)
