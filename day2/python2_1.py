a = 10

if a == 1:
    print("참")
else:
    print("거짓")

if a < 1:
    print("a는 1보다 작다.")
else:
    print("a는 1보다 같거나 크다.")

if a < 1:
    print("a는 1보다 작다.")
else:
    if a == 1:
        print("a는 1이랑 같다.")
    else:
        print("a는 1보다 크다.")
    
if a < 1:
    print("a는 1보다 작다.")
elif a == 1:
    print("a는 1이랑 같다.")
else:
    print("a는 1보다 크다.")

