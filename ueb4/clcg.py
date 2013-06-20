from math import sqrt

m1 = 32363.0
a1 = 157.0
m2 = 31727.0
a2 = 146.0
m3 = 31657.0
a3 = 142.0

x1 = 100.0
x2 = 300.0
x3 = 500.0

r = []

for i in range(0, 5):
    x1 = a1 * x1 % m1
    x2 = a2 * x2 % m2
    x3 = a3 * x3 % m3
    x = (x1 - x2 + x3) % (m1 - 1)
    if x > 0:
        r_i = x / m1
    else:
        r_i = (m1 - 1) / m1

    print("{}: {}".format(i, r_i))
    r.append(r_i)

r.sort()
d_plus = max((i + 1) / len(r) - r[i] for i in range(len(r)))
d_minus = max(r[i] - i / len(r) for i in range(len(r)))

print("D+ = {}".format(d_plus))
print("D- = {}".format(d_minus))

d = max(d_plus, d_minus)

print("D  = {}".format(d))

d_alpha = 1.36/sqrt(len(r))
d_alpha = 0.565

if d <= d_alpha:
    print("H0 accepted")
else:
    print("H0 rejected")
