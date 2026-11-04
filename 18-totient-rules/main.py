def phi(n):
    # Keep the worksheet's stated base case; standard references use phi(1)=1.
    if n == 1:
        return 0, "Rule 1 (worksheet): phi(1) = 0"

    remaining = n
    factors = []
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            exponent = 0
            while remaining % divisor == 0:
                remaining //= divisor
                exponent += 1
            factors.append((divisor, exponent))
        divisor += 1
    if remaining > 1:
        factors.append((remaining, 1))

    prime_power_values = [prime ** (power - 1) * (prime - 1) for prime, power in factors]
    value = 1
    for part in prime_power_values:
        value *= part
    details = [f"Rule: phi(p^k) = p^(k-1)(p-1)"]
    details.extend(f"phi({prime}^{power}) = {prime}^{power - 1}({prime}-1) = {part}"
                   for (prime, power), part in zip(factors, prime_power_values))
    if len(factors) > 1:
        details.append("Rule: phi(ab) = phi(a)phi(b) when gcd(a,b)=1")
        details.append(f"Distinct prime powers are coprime, so phi({n}) = {' x '.join(map(str, prime_power_values))} = {value}")
    elif factors[0][1] == 1:
        details[0] = f"Rule 2: {n} is prime, so phi({n}) = {n}-1 = {value}"
    return value, "\n".join(details)

number = int(input("Enter a positive integer: "))
if number < 1:
    raise ValueError("Enter a positive integer")
result, explanation = phi(number)
print(explanation)
print(f"Final answer: phi({number}) = {result}")
