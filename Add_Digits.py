def add(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

num = int(input())
result = add(num)
print(result)
