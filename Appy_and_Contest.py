T = int(input())

for _ in range(T):
    N, A, B, K = map(int, input().split())

    problems_A = N // A
    problems_B = N // B
    problems_common = N // (A * B)
    total_problems = problems_A + problems_B - 2 * problems_common

    if total_problems >= K:
        print("Win")
    else:
        print("Lose")
