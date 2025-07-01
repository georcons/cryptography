"""
Задача 9 и 13.
Алгоритъм на Pohlig-Hellman

"""

import math

def find_factors(n):
    factor_dict = {}
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            if divisor in factor_dict:
                factor_dict[divisor] += 1
            else:
                factor_dict[divisor] = 1
            n //= divisor
        divisor += 1
    if n > 1:
        factor_dict[n] = 1
    return factor_dict

def log_for_prime_power(base, target, prime, exponent, modulus):
    group_order = modulus  - 1
    g1 = pow(base, group_order // prime, modulus)
    x = 0
    base_inverse = pow(base, -1,modulus)

    for j in range(exponent):
        reduced_target = (target * pow(base_inverse, x, modulus)) % modulus
        h_j = pow(reduced_target, group_order // (prime**(j + 1)), modulus)
        
        for d in range(prime):
            if pow(g1, d, modulus) == h_j:
                x += d * (prime **j)
                break

    return x

def chinese_rem_theorem(congruences):
    total_mod = math.prod([mod for _, mod in congruences])
    result = 0

    for remainder, mod_i in congruences:
        partial_prod = total_mod // mod_i
        inverse = pow(partial_prod, -1, mod_i)
        result += remainder * partial_prod * inverse

    return result % total_mod

def pohlig_hellman(base,target,modulus):
    order = modulus-1
    factors = find_factors(order)

    congruences = []
    for prime, exp in factors.items():
        subgroup_mod = prime ** exp
        x_i = log_for_prime_power(base, target, prime, exp, modulus)
        congruences.append((x_i, subgroup_mod))

    return chinese_rem_theorem(congruences)

def compute(p, g, h):
    result = pohlig_hellman(g, h, p)
    print(f"Discrete logarithm of {h} with base {g} in Z_{p}* is {result}.\n")

if __name__ == "__main__":
    print("Задача 9.")
    compute(101, 2, 66)

    print("Задача 13.")
    compute(353, 3, 135)
