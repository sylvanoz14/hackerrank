import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
while len(arr) > 0:
    min_ = min(arr)
    start = 0
    while start < len(arr):
        arr[start] -= min_
        start += 1
    print len(arr)
    arr = [x for x in arr if x != 0] 

#another way to delete multiple items from a list
"""
try:
    a.remove(c)
except ValueError:
    pass
"""
