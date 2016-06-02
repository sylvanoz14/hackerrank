# Enter your code here. Read input from STDIN. Print output to STDOUT
# finally get to use the lambda function.
# the tric is to sort the list before printing it. i used Python's built in sort()
# good exercise :)
N = input()
ar = []
list_pos = 0
for i in xrange(0, N):
    value = (raw_input().strip().split())
    val_zero = int(value[0])
    if list_pos < int(N/2):
        value.append(True)
    else:
        value.append(False)
    ar.append(value)
    list_pos +=1

ar.sort(key=lambda x: int(x[0]))
for pair in ar:
    if pair[2] == True:
        print "-",
    else:
        print pair[1],
