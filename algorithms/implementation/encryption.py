#!/bin/python

import sys
import math


s = raw_input().strip()

floor = math.floor(math.sqrt(len(s)))
ceil = math.ceil(math.sqrt(len(s)))

if len(s) > floor * ceil:
    floor = ceil

encrypt = [] # store all words
for count in range(int(floor)):
    if len(s) >= ceil:
        #extract and print ceil-values from s:
        #modify s
        word = s[:int(ceil)]
        encrypt.append(word)
        s = s[int(ceil):]

    else:
        #print remaining s
        encrypt.append(s)
index = 0
while index < ceil:
    final = ""
    for word in encrypt:
        if index < len(word):
            final = final + word[index] #make the final encrypted word
    print final,
    index += 1
