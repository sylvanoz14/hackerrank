# good exercise. there are two important concepts here.
# 1. use modulos to make sure u don't do useles rotstions
# 2. dont do any rotation.  find out wich element in the current list
# will be in the q position if it was rotated k % n times.

# simple but very usefull Ex.

n,k,q = map(int, list(raw_input().strip().split(' ')))
lst = list(raw_input().strip().split(' '))

rounds = k % n

for i in xrange(q):
    print lst[int(raw_input().strip()) - rounds]
