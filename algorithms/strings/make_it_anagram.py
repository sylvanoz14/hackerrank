s_1 = raw_input().strip()
s_2 = raw_input().strip()



output = 0 # assume strings equal
counted = []
both_s = [s_1, s_2]

for s in both_s:
    for letter in s:
        if letter not in counted:
            counted.append(letter)
            s_1_count = s_1.count(letter)
            s_2_count = s_2.count(letter)
            diff = abs(s_1_count - s_2_count)
            output += diff
print output
