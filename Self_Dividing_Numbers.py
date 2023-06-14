def is_self_dividing(num):
    if '0' in str(num):
        return False
    for digit in str(num):
        if num % int(digit) != 0:
            return False
    return True
def self_dividing_numbers(left, right):
    result = []
    for num in range(left, right + 1):
        if is_self_dividing(num):
            result.append(num)
    return result
lower = int(input())
upper = int(input())
self_dividing_nums = self_dividing_numbers(lower, upper)
print(' '.join(map(str, self_dividing_nums)))
