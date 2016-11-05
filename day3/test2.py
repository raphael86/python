def sum(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b

def sumAtoB(a, b):
    sum = 0
    for i in range(a, b+1):
        sum = sum + i
    return sum

print(sum(15, 10))
print(sub(15, 10))
print(mul(15, 10))
print(div(100, 10))
print(sumAtoB(1, 10))
print(sumAtoB(1, 100))
