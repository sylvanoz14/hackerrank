string = raw_input()

found = False
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False

counted = []
unpaired = 0
for letter in string:
    if letter not in counted:
        counted.append(letter)
        if string.count(letter) % 2 == 1:
            unpaired += 1

if unpaired < 2:
    found = True


if not found:
    print("NO")
else:
    print("YES")
