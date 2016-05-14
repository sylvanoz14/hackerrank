# was pretty straight forward
import string

s = raw_input().strip()

l_case = list(string.ascii_lowercase)

def pangram(s, l_case):
    for i in l_case:
        if i not in s and i.upper() not in s:
            return "not pangram"
    return "pangram"

print pangram(s, l_case)
