def is_perfect_number(n):
    if n <= 0:
        return False
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum == n
n = int(input())
if is_perfect_number(n):
    print(True)
else:
    print(False)
