def partition(ar):
    p= ar[0]
    left, right = [], []
    for number in ar:
        if number < p:
            left.append(number)
        else:
            right.append(number)
    for number in left:
        print number,
    for number in right:
        print number,


m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)
