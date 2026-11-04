# Implements the handout's phi(1)=0 rule, prime rule, and coprime product rule.
import math

def phi(n):
    if n == 1:
        return 0, "Rule 1: phi(1) = 0"
    if all(n % divisor for divisor in range(2, int(n ** 0.5) + 1)):
        return n - 1, f"Rule 2: {n} is prime, so phi({n}) = {n}-1"
    for m in range(2, n):
        k = n // m
        if n % m == 0 and math.gcd(m, k) == 1:
            phi_m, step_m = phi(m)
            phi_k, step_k = phi(k)
            value = phi_m * phi_k
            steps = f"Rule 3: {n}={m}x{k}, and gcd({m},{k})=1\n{step_m}\n{step_k}\nphi({n})={phi_m}x{phi_k}={value}"
            return value, steps
    # The first three rules do not cover every composite; count coprime values for those cases.
    value = sum(1 for number in range(1, n) if math.gcd(number, n) == 1)
    return value, f"Fallback: count numbers below {n} that are coprime to {n}"

number = int(input("Enter a positive integer: "))
if number < 1:
    raise ValueError("Enter a positive integer")
result, explanation = phi(number)
print(explanation)
print(f"Final answer: phi({number}) = {result}")
