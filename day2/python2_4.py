# 0부터 10까지 출력하고 싶을 때
for i in range(11):
    print(i)

# 5부터 10까지 출력하고 싶을 때
for i in range(5, 11):
    print(i)

# 0부터 10까지 합을 구하고 싶을 때
sum = 0;
for i in range(11):
    sum = sum + i
print(sum)

# 5부터 10까지 합을 구하고 싶을 때
sum = 0;
for i in range(5, 11):
    sum = sum + i
print(sum)

# for문을 5번 돌리고 싶을 때
for i in range(5):
    print(str(i) + "번째 돌았다.")
