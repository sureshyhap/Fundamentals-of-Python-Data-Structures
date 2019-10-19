"""
Calculates pi.
"""
def main():
    """Uses Leibniz's infinite series definition of pi to
    calculate it based on a a number of terms."""
    iterations = int(input("How many terms should be used in the approximation? "))
    pi_div_4 = 0
    denom = 1
    neg_term = False
    for i in range(iterations):
        if not neg_term:
            pi_div_4 += (1 / denom)
        else:
            pi_div_4 -= (1 / denom)
        neg_term = not neg_term
        denom += 2
    pi = pi_div_4 * 4
    print(pi)
    


if __name__ == "__main__":
    main()
