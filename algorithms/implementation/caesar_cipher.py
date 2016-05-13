import sys
import string


n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())



l_case = list(string.ascii_lowercase)
u_case = list(string.ascii_uppercase)
s = list(s)


index = 0
while index < n:
    letter = s[index]
    if letter in l_case or letter in u_case:
        number = ord(letter)
        count = k
        while count > 0:
            if number not in [122,90]:
                number +=1
                count -= 1
            if number == 90 and count > 0:
                number = 65
                count -= 1
            if number == 122 and count > 0:
                number = 97
                count -= 1
        s[index] = chr(number)
    index += 1

answer = ""
for m in s:
    answer = answer + m
print answer
