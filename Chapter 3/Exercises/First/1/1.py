"""Benchmarks a loop."""

problem_size = int(input("Input a problem size: "))
iterations = 0
while problem_size > 0:
    iterations += 1
    problem_size = problem_size // 2
print(iterations)
