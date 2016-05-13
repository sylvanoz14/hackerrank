# Enter your code here. Read input from STDIN. Print output to STDOUT

N, K = map(int, raw_input().split())
T = map(int, raw_input().split())

special_question = 0 # final output
x = 0 # for looping via the list (one chapter at a time)
page = 0 # for increasing the pages as we travel via the chapters
while x < N: #trvaelling through each chapter starting from the first
    page += 1 #start each chapter on a new page
    question_count =1 # this makes sure there is no more than K questions per chapter
    chapter_question = 1 # start from question 1 for each chapter
    while chapter_question <= T[x] :
        
        if question_count > K: # if there are K questions on a page, 
                                #start a new page and reset the count
            page += 1
            question_count = 1
        if chapter_question == page: 
            special_question += 1
            
        chapter_question += 1
        question_count += 1
        
    x += 1
print special_question        
            
