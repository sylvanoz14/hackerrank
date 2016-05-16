t = raw_input().strip()
all_words = []

for _ in xrange(0,int(t)):
    s = raw_input().strip()
    all_words.append(s)
first_word = all_words[0]

all_words_len = len(all_words)
gem_count = 0
counted = ""

for letter in first_word:
    if letter not in counted:
        counted += letter
        letter_count = 0

        for word in all_words:
            if letter in word:
                letter_count += 1

        if letter_count == all_words_len:
            gem_count += 1
