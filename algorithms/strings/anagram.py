# Enter your code here. Read input from STDIN. Print output to STDOUT
# get t
# use for to get long string one at a time:
#   for every long sting find out if its even:
#       if even:
#           divide word in two halves, a and b
#           for all letters in b:
#               count how many are in b, abd add to counted. count howmany are in a and add diff to output
#       if not even:
#           return -1

t = raw_input().strip()
for _ in xrange(0,int(t)):
    s = raw_input().strip()
    if len(s) % 2 == 1:
        print -1
    else:
        counted = []
        output = 0
        a = s[0: (len(s)/2)]
        b = s[len(s)/2 :]
        for letter in b:
            if letter not in counted:
                counted.append(letter)
                b_count = b.count(letter)
                a_count = a.count(letter)
                #print letter, b_count, a_count
                if b_count > a_count:
                    output += b_count - a_count
        print output
