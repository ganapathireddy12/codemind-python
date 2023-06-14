p, r, t = map(float, input().split())
n = 1  # Assuming interest is compounded annually
A = p * (1 + r / (100 * n)) ** (n * t)
print("{:.2f}".format(A))
