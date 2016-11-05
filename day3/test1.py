box = ['a', 'b', 'c', 'd']

if 'g' in box:
    print("g가 있네요.") # box 안에 g가 있는 경우 
else:
    print("g가 없네요.") # box 안에 g가 없는 경우



a = 0 
while a < 10:
    a = a+1         # while문을 돌 때마다 a가 증가
    if(a%2 == 0):   # a를 2로 나눈 나머지가 0이면
        continue    # 넘긴다.
    print(a)        # a를 2로 나눈 나머지가 0이 아니라면


marks = [90, 50, 60]
number = 0
for mark in marks:
    number = number + 1
    if(mark < 60):
        print("%d번 학생 분발하세요. 불합격입니다." % number)
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)






    
