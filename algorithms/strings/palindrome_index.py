#start with head=0, tail=len(s)-1. You loop thru increasing head and decreasing tail. If they match or #head>tail, it's already a palindrome, print -1.
#If you find a difference (s[head] != s[tail]). There are three test cases. If head+1 == tail (you are # # #overlapping indeces), then you can pick either #head or tail. If not, you check the rest of the string to #see if s from head to tail-1 is a palindrome, if so, tail is the index. Otherwise, head is the index.



def check_palindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

n = int(raw_input().strip())
for _ in range(n):
    s = raw_input().strip()
    length = len(s)

    head = 0
    tail = length - 1

    while True:
        if head >= tail:
            print -1
            break

        if s[head] != s[tail]:
            if head+1 == tail:
                print head
                break
            elif check_palindrome(s, start=head, end=tail-1):
                print tail
            else:
                print head
            break
        head += 1
        tail -= 1
