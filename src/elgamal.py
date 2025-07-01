"""
Задача 12.
Схема на ElGamal

"""

p = 101     # Модул - просто число
alpha = 2   # Примитивен елемент
x = 43      # Private Key
m = 26      # Съобщение
k = 3       # Случайно цяло число, за което (k, p-1) = 1

# Разширен Еквлидов алгоритъм
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

# Modular Inverse чрез Разш. Евклидов алгоритъм
def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise "Modular inverse does not exist"
    return x % m

# 1. Изчисляване на публичен ключ
y = pow(alpha, x, p)
print(f"Public key: {y}")

# 2. Изчисляване на r
r = pow(alpha, k, p)
print(f"r = {r}")

# 3. Изчисляване на s; считаме, че хеш функцията е просто h(m)=m
k_inv = modinv(k, p-1)
s = (k_inv * (m - x * r)) % (p - 1)
print(f"s = {s}")

# Извеждане на подписа
signature = (r, s)
print(f"\nПодпис: (r, s) = {signature}")

# 4. Валидиране
u = (pow(y, r, p) * pow(r, s, p)) % p
v = pow(alpha, m, p)

if u == v:
    print("Подписът е валиден.")
else:
    print("Подписът не е валиден.")
