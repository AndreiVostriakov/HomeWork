# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

def gcd(a, b):
    while (b > 0):
        a, b = b, a % b
    return a

def simplify(pair):
    g = gcd(pair[0], pair[1])
    return (pair[0] // g, pair[1] // g)

n = 11
t = []
for num in range(1, n + 1):
    for denom in range(num + 1, n + 1):
        pair = simplify((num, denom))
        t.append(pair)
s = list(set(t))

for q in sorted(s, key = lambda x: x[0] / x[1]):
    print(str(q[0]) + "/" + str(q[1]))